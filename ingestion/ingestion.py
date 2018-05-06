import urllib2
from time import sleep
from BeautifulSoup import BeautifulSoup

def switch_to_SSID(ssid):
    return

def start_timelapse():
    # Go to time lapse mode
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/sub_mode?mode=0&sub_mode=1')

    # Start the time lapse recording
    sleep(5)
    # Set interval fime
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/setting/5/6')
    sleep(1)
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
    return

if __name__ == "__main__":
    # Make sure to be connected to right Wifi!

    #switch_to_SSID('goprohotspot') 
    start_timelapse()
    sleep(10)
    stop_timelapse()
    sleep(5)
    dowload_latest_file('date_sunrise.mp4')
    #switch_to_SSID('goprohotspot') 

