from pathlib import Path
from src import log 
from src.data_ingestion import DataIngestion
from src.prepare import main

dataIngestion = DataIngestion()
dataIngestion.download_file()
main(Path('src'))