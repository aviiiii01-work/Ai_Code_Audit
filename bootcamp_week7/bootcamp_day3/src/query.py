from src.query_engine.image_query_engine import ImageQueryEngine
from src.retriever.image_retriever import ImageRetriever

def main():
    retriever = ImageRetriever(embedding_dim=512)
    query_engine = ImageQueryEngine(retriever)

    print("\nTEXT → IMAGE")
    for r in query_engine.text_to_image("World Population"):
        print(r["path"], "|", r["caption"])

    print("\nIMAGE → IMAGE")
    for r in query_engine.image_to_image("src/data/query/query.png"):
        print(r["path"])

    print("\nIMAGE → TEXT")
    for r in query_engine.image_to_text("src/data/query/query.png"):
        print(r["caption"])

if __name__ == "__main__":
    main()
