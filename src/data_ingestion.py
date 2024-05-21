import os
import urllib.request as request
import tarfile
from . import log
import requests 

class DataIngestion:
    def __init__(self):
        pass 

    
    def download_file(self):
        if not os.path.exists('src/data/raw/imagenette2-160.tgz'):
            os.makedirs('src/data/raw', exist_ok=True)
            filename, headers = request.urlretrieve(
                url = 'https://osf.io/d6qbz/download',
                filename = 'src/data/raw/imagenette2-160.tgz'
            )
            if filename:
                log.info(f'Data file downloaded {filename} with {headers}')
                self.extract_zip_file()
        else:
            log.warning(f"File already exists ")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = 'src/data/raw'
        # os.makedirs(unzip_path, exist_ok=True)
        with tarfile.open('src/data/raw/imagenette2-160.tgz', 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            log.info(f'Data exrated to {unzip_path}')
  