# Imports the Google Cloud client library
from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename('staging/'+destination_file_name)

def dowload_blobs_in_bucket(bucket_name):
    """Download all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    for blob in blobs:
        download_blob(bucket_name, blob.name, blob.name)

if __name__ == "__main__":
    # Download GCS Blop files locally
    dowload_blobs_in_bucket('20180503sr')

# Creates the new bucket
#storage_client = storage.Client()
#bucket_name = '100-days-of-sunrise'
#bucket = storage_client.create_bucket(bucket_name)
#print('Bucket {} created.'.format(bucket.name))

