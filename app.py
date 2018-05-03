from google.cloud import storage
import os

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

def dowload_blobs_in_bucket(bucket_name):
    """Download all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    for blob in blobs:
        download_blob(bucket_name, blob.name, 'staging/'+blob.name)

if __name__ == "__main__":
    bucket = '20180503sr'

    # Download the images from GCS locally
    dowload_blobs_in_bucket(bucket)

    # Create the timelapse
    video_name = 'sunrise.mp4'
    timelapse_command = 'ffmpeg -r 15 -start_number 23157 -i staging/G00%d.JPG -s 1280x720 -vcodec libx264 '+video_name
    os.system('cd /home/michielvanthoor/100-days-of-sunrise/staging')
    os.system(timelapse_command)

    # Upload the timelaps video to GCS
    upload_blob(bucket,'staging/'+video_name,video_name)