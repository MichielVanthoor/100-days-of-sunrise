import urllib2
from time import sleep

def start_timelapse():
    # Make sure to be connected to right Wifi & GoPro is on!

    # Go to time lapse mode
    urllib2.urlopen('http://10.5.5.9/camera/CM?t=17461234&p=%03')

    # Start the time lapse recording
    sleep(3)
    urllib2.urlopen('http://10.5.5.9/bacpac/SH?t=17461234&p=%01')


def stop_timelapse():
    # Make sure to be connected to right Wifi!
    # Stop the time lapse recording
    urllib2.urlopen('http://10.5.5.9/bacpac/SH?t=17461234&p=%00')

def dowload_files(url):
    urllib.urlretrieve('http://site.com/', filename='filez.txt')

if __name__ == "__main__":
    start_timelapse()
    sleep(10)
    stop_timelapse()


### Wasteland
    # Turn GoPro on
    #urllib2.urlopen('http://10.5.5.9/bacpac/PW?t=17461234&p=%01')

    # Turn GoPro off
    #urllib2.urlopen('http://10.5.5.9/bacpac/PW?t=17461234&p=%00')
