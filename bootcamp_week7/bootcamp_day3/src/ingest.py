from src.pipelines.image_ingest import ImageIngest

def main():
    ingestor = ImageIngest()
    ingestor.process_folder("src/data/images")

if __name__ == "__main__":
    main()
