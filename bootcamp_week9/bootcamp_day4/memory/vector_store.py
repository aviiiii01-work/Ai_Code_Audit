import faiss
import numpy as np
import os
import pickle
from sentence_transformers import SentenceTransformer
from autogen_core.memory import Memory, MemoryContent, MemoryMimeType, MemoryQueryResult, UpdateContextResult
from autogen_core.models import SystemMessage, UserMessage

class FAISSVectorMemory(Memory):
    def __init__(self, index_path="data/vector_index.faiss"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = 384
        self.index_path = index_path
        
        if os.path.exists(index_path) and os.path.getsize(index_path) > 0:
            self.index = faiss.read_index(index_path)
            with open(index_path + ".metadata", "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

    async def add(self, content: MemoryContent) -> None:
        embedding = self.model.encode([content.content]).astype('float32')
        self.index.add(embedding)
        self.metadata.append(content.content)
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".metadata", "wb") as f:
            pickle.dump(self.metadata, f)

    async def query(self, query: str | MemoryContent, k: int = 2, **kwargs) -> MemoryQueryResult:
        if self.index.ntotal == 0:
            return MemoryQueryResult(results=[])
        
        query_str = query.content if isinstance(query, MemoryContent) else query
        query_vec = self.model.encode([query_str]).astype('float32')
        distances, indices = self.index.search(query_vec, k)
        
        results = []
        for idx in indices[0]:
            if idx != -1:
                results.append(MemoryContent(content=self.metadata[idx], mime_type=MemoryMimeType.TEXT))
        return MemoryQueryResult(results=results)

    async def update_context(self, model_context) -> UpdateContextResult:
        messages = await model_context.get_messages()
        if not messages:
            return UpdateContextResult(memories=MemoryQueryResult(results=[]))
            
        last_query = messages[-1].content
        query_results = await self.query(last_query)
        
        if query_results.results:
            context_str = "\n".join([f"- {r.content}" for r in query_results.results])
            
        
            memory_hint = UserMessage(
                content=f"[MEMORY RETRIEVED: The following facts might be relevant]\n{context_str}",
                source="memory_system"
            )
            await model_context.add_message(memory_hint)
            
        return UpdateContextResult(memories=query_results)

    async def clear(self): pass
    async def close(self): pass