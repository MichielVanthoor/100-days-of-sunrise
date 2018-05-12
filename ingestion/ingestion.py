import urllib2
import schedule
import time
import datetime
import json

from bs4 import BeautifulSoup
from google.cloud import storage

def start_timelapse():
    # Go to time lapse mode
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/sub_mode?mode=0&sub_mode=1')
    # Start the time lapse recording
    time.sleep(5)
    # Set interval time
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
    soup = BeautifulSoup(response, 'lxml')

    # Get the name and URL of the most recent recording
    video_name = soup.find_all('a')[-2].string
    url = video_server_url+video_name

    # Save file in local directory
    file = urllib2.urlopen(url)
    data = file.read()
    with open(filename, "w+") as code:
      code.write(data)

def upload_to_gcs(filename):
    client = storage.Client()
    bucket = client.get_bucket('100-days-of-sunrise')
    blob = bucket.blob(filename)
    blob.upload_from_filename('staging/{}'.format(filename))

def create_timelapse(filename):
    start_timelapse()
    time.sleep(2*60*60)
    stop_timelapse()
    time.sleep(5)
    dowload_latest_file('staging/{}_sunrise.mp4'.format(filename))
    upload_to_gcs('{}_sunrise.mp4'.format(filename))

def get_sun_details(day):
    sun_api = 'https://api.sunrise-sunset.org/json?lat=52.377956&lng=4.897070&date={}'.format(day)
    response = urllib2.urlopen(sun_api)
    sun_details = json.load(response)['results']

    return sun_details

def get_sunrise_start_time(day):
    # Get sunrise
    sun_details = get_sun_details(day)
    sr_time_string = sun_details['sunrise']

    # Convert to time format to do math
    sr_time = datetime.datetime.strptime(sr_time_string, '%I:%M:%S %p')

    # Calculate start time & convert to string
    sr_start_time = sr_time - datetime.timedelta(minutes=15)
    sr_start_time_string = datetime.datetime.strftime(sr_start_time, '%H:%M')

    return sr_start_time_string

def get_sunset_start_time(day):
    # Get sunset
    sun_details = get_sun_details(day)
    ss_time_string = sun_details['sunset']

    # Convert to time format to do math
    ss_time = datetime.datetime.strptime(ss_time_string, '%I:%M:%S %p')

    # Calculate start time & convert to string
    ss_start_time = ss_time - datetime.timedelta(minutes=105)
    ss_start_time_string = datetime.datetime.strftime(ss_start_time, '%H:%M')

    return ss_start_time_string

def schedule_start_times():
    # Get today's date
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    print('Starting times are being scheduled for {}'.format(today))

    # Get sunrise and sunset starttimes
    sr_start_time = get_sunrise_start_time(today)
    ss_start_time = get_sunset_start_time(today)

    schedule.every().day.at(sr_start_time).do(create_timelapse,today)
    schedule.every().day.at(ss_start_time).do(create_timelapse,today)
    print('Sunrise start set for {}'.format(sr_start_time))
    print('Sunset start set for {}'.format(ss_start_time))

if __name__ == "__main__":
    # Schedule and run job
    schedule.every(1).day.at("00:05").do(schedule_start_times)
    while True:
        schedule.run_pending()
        time.sleep(1)



