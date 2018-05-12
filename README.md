# 100-days-of-sunrise

Work in progress

## Concept
GoPro will automatically create a timelapse every morning based on the time of sunrise.
These timelapses will be stored in Google Cloud Storage, and can than be used for display on websites etc.

## Requirements
* GoPro Hero 4
* Raspberry Pi 3
* Additional WiFi Adapter
* Optional, direct power supply for your GoPro

## Configuring Raspberry Pi to schedule and ingest GoPro footage
* Boot Raspberry Pi with Raspbian Strech Lite
* Set the timezone to UTC
  * `sudo dpkg-reconfigure tzdata`
  * Select 'None of the above' and after that 'UTC'
* Configure both your GoPro Network as well as your internetenabled network (example [here](http://www.processthings.com/post/66023171876/how-to-connect-your-raspberry-pi-to-two-wi-fi))
* Install dependencies
  * `sudo apt-get update`
  * `sudo apt-get upgrade`
  * Install git (`sudo apt-get install git`)
  * Install pip (`sudo apt-get install python-pip`)
  * Install [schedule](https://github.com/dbader/schedule) (`pip install schedule`)
  * Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)(`pip install beautifulsoup4`)
  * [Install gcloud following these steps](https://cloud.google.com/sdk/docs/quickstart-linux)
  * Install and configure [Google Cloud Platform Client Library](https://cloud.google.com/compute/docs/tutorials/python-guide) (`pip install --upgrade google-api-python-client`)
* Clone this repo to your Raspberry Pi (`git clone https://github.com/MichielVanthoor/100-days-of-sunrise`)
* Run the ingestion application
  * `cd 100-days-of-sunrise/ingestion`
  * `python ingestion.py`
