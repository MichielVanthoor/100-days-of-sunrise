import urllib2
import schedule
import time
import json
from bs4 import BeautifulSoup
from google.cloud import storage


def switch_to_SSID(ssid):
    return

def start_timelapse():
    # Go to time lapse mode
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/sub_mode?mode=0&sub_mode=1')

    # Start the time lapse recording
    time.sleep(5)
    # Set interval fime
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/setting/5/6')
    time.sleep(1)
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=1')

def stop_timelapse():
    # Stop the time lapse recording
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=0')

def dowload_latest_file(filename):
    # Get URL of latest video
    video_server_url = 'http://10.5.5.9:8080/videos/DCIM/100GOPRO/'
    response = urllib2.urlopen(video_server_url)
    soup = BeautifulSoup(response)

    # TODO
    video_name = soup.title.string
    url = video_server_url+video_name

    # Save file in local directory
    file = urllib2.urlopen(url)
    data = file.read()
    with open(filename, "wb") as code:
      code.write(data)

def upload_to_gcs(filename):
    client = storage.Client()
    bucket = client.get_bucket('100-days-of-sunrise')
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename='/local/path.txt')

def create_timelapse():
    # TODO
    #switch_to_SSID('goprohotspot') 
    start_timelapse()
    time.sleep(120*60)#run for 2 hours
    stop_timelapse()
    time.sleep(5)
    dowload_latest_file('date_sunrise.mp4')
    #switch_to_SSID('goprohotspot') 
    #upload_to_gcs('date_sunrise.mp4')   

def schedule_start_time():
    # Get sunrise through API
    sunrise_api = 'https://api.sunrise-sunset.org/json?lat=52.377956&lng=4.897070&date=today'
    response = urllib2.urlopen(sunrise_api)
    data = json.load(response) 
    sunrise_time_string = data['results']['sunrise']
    
    # Convert to time format to do math
    sunrise_time = time.strptime(sunrise_time_string, '%I:%M:%S %p') 

    # Calculate start time & convert to string
    offset_minutes = 15
    #TODO
    #start_time = sunrise_time - offset_minutes*60
    start_time_string = time.strftime(start_time, '%I:%M')


    schedule.every().day.at(start_time_string).do(create_timelapse)

if __name__ == "__main__":
    # Do everything in UTC time!
    # Schedule and run job
    schedule.every(1).day.at("00:05").do(schedule_start_time)
    while 1:
        schedule.run_pending()
        time.sleep(1)



