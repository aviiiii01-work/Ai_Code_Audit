class ImageQueryEngine:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def query(self, question: str):
        contexts = self.retriever.search(question, k=3)

        if not contexts:
            return (
                "I don't know. The answer is not present in the retrieved image context.",
                []
            )

        context_text = "\n".join(c["text"] for c in contexts)

        prompt = f"""
    You are an image-based assistant.

    Context:
    {context_text}

    Question:
    {question}

    Answer ONLY from the context.
    If the answer is not present, say "I don't know".
    """

        answer = self.llm.generate(prompt)
        return answer, [c["text"] for c in contexts]
