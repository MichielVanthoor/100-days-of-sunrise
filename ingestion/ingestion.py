import urllib2
from time import sleep

def switch_to_SSID(ssid):
    return

def start_timelapse():
    # Make sure to be connected to right Wifi & GoPro is on!

    # Go to time lapse mode
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/sub_mode?mode=0&sub_mode=1')

    # Start the time lapse recording
    sleep(5)
    # Set interval fime
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/setting/5/6')
    sleep(1)
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=1')

def stop_timelapse():
    # Make sure to be connected to right Wifi!
    # Stop the time lapse recording
    urllib2.urlopen('http://10.5.5.9/gp/gpControl/command/shutter?p=0')

def dowload_files(url):
    urllib.urlretrieve('http://site.com/', filename='filez.txt')

if __name__ == "__main__":
    start_timelapse()
    sleep(10)
    stop_timelapse()