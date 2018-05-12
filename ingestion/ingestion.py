import urllib2
import schedule
import time
import datetime
import json
import os

from bs4 import BeautifulSoup
from google.cloud import storage

def switch_to_SSID(ssid):
    if ssid in ['C&M']:
        os.system('connmanctl connect wifi_b827eb4107d1_43264d_managed_psk')
    elif ssid in ['goprohotspot']:
        os.system('connmanctl connect wifi_b827eb4107d1_676f70726f686f7473706f74_managed_psk')
    else:
        print('WiFi network not configured')

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
    switch_to_SSID('goprohotspot')
    time.sleep(10)
    start_timelapse()
    time.sleep(10)#TODO
    stop_timelapse()
    time.sleep(5)
    dowload_latest_file('staging/{}_sunrise.mp4'.format(filename))
    switch_to_SSID('C&M')
    time.sleep(10)
    upload_to_gcs('{}_sunrise.mp4'.format(filename))

def schedule_start_time():
    print('Starting time is being scheduled')
    # Get today's date
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # Get sunrise through API
    sunrise_api = 'https://api.sunrise-sunset.org/json?lat=52.377956&lng=4.897070&date={}'.format(today)
    response = urllib2.urlopen(sunrise_api)
    data = json.load(response) 
    sunrise_time_string = data['results']['sunrise']
    
    # Convert to time format to do math
    sunrise_time = time.strptime(sunrise_time_string, '%I:%M:%S %p') 

    #TODO
    # Calculate start time & convert to string
    offset_minutes = 15
    #start_time = sunrise_time - offset_minutes*60
    #start_time_string = time.strftime(start_time, '%I:%M')
    start_time_string = '09:37'

    schedule.every().day.at(start_time_string).do(create_timelapse(today))

if __name__ == "__main__":
    # Schedule and run job
    #TODO
    schedule.every(1).day.at("09:35").do(schedule_start_time)
    while 1:
        schedule.run_pending()
        time.sleep(1)



