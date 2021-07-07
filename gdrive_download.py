# pip install python-dotenv
from dotenv import dotenv_values
config = dotenv_values(".env") 
file_id = config['colab_notebook_id']
file_name = './colab/'+config['colab_notebook_filename']

# pip install googledrivedownloader
from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id=file_id,
                                    dest_path=file_name,
                                    overwrite=True)