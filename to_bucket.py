import os
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
# Imports the Google Cloud client library
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


file_source = "/home/dswanstrom/CanvasDataWork/unpackedFiles/"
canvas_data_txts = []


for root, dirs, files in os.walk(file_source):
    for file in files:
        if file.endswith('.txt'):
            canvas_data_txts.append(file)


for file in canvas_data_txts:
    upload_blob('canvas-data-csv-ecasd', file_source + file, 'canvasdata/'+ file)
