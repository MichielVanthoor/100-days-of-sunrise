# 100-days-of-sunrise

## Configuring Raspberry Pi to schedule and ingest GoPro footage
* Boot Raspberry Pi with Raspbian Strech Lite
* Connect to (internet-enabled) WiFi using [these instructions](https://www.raspberrypi.org/forums/viewtopic.php?t=191252)
* Configure the same for your GoPro WiFi
* Install dependencies
  * `sudo apt-get update`
  * `sudo apt-get upgrade`
  * Install git (`sudo apt-get install git`)
  * Install pip (`sudo apt-get install python-pip`)
  * Install [schedule](https://github.com/dbader/schedule) (`pip install schedule`)
  * Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)(`sudo apt-get install python-bs4`)
* Clone this repo to your Raspberry Pi (`git clone https://github.com/MichielVanthoor/100-days-of-sunrise`)
* Run the ingestion application (`python 100-days-of-sunrise/ingestion/ingestion.py`)
