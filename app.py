# Imports the Google Cloud client library
from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def dowload_blobs_in_bucket(bucket_name):
    """Download all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        download_blob(bucket_name, blob, blo)

if __name__ == "__main__":
    # Download GCS Blop files locally
    client = storage.Client()
    bucket = client.get_bucket('20180503sr')
    list_blobs()
    blob_name = 'G0023157.JPG'
    blob = storage.Blob(blob_name, bucket)
    with open('staging/'+blob_name, 'wb') as file_obj:
        blob.download_to_file(file_obj)

# Creates the new bucket
#storage_client = storage.Client()
#bucket_name = '100-days-of-sunrise'
#bucket = storage_client.create_bucket(bucket_name)
#print('Bucket {} created.'.format(bucket.name))

