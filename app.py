# Imports the Google Cloud client library
from google.cloud import storage

# Download GCS Blop files locally
client = storage.Client()
bucket = client.get_bucket('20180503sr')
blob = storage.Blob('G0023157.JPG', bucket)
with open('staging/1', 'wb') as file_obj:
    blob.download_to_file(file_obj)

# Creates the new bucket
#storage_client = storage.Client()
#bucket_name = '100-days-of-sunrise'
#bucket = storage_client.create_bucket(bucket_name)
#print('Bucket {} created.'.format(bucket.name))

