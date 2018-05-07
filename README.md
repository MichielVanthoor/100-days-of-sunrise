# 100-days-of-sunrise

## Configuring Google Cloud Platform bucket

## Configuring Raspberry Pi to schedule and ingest GoPro footage
* Boot Raspberry Pi with Raspbian Strech Lite
* Set the timezone to UTC 
* Insert your network parameters Wifi config files
  * Enter your gopro wifi password`sudo nano gopro`
  * Copy to the wpa_supplicant directory (`sudo cp gopro /etc/wpa_supplicant/`)
  * Enter you internetenabled WiFi `sudo nano internet`
  * Copy to the wpa_supplicant directory (`sudo cp gopro /etc/wpa_supplicant/`)
  * Give executing rights to switchwifi script (`chmod +x switchwifi`)
* Install dependencies
  * `sudo apt-get update`
  * `sudo apt-get upgrade`
  * Install git (`sudo apt-get install git`)
  * Install pip (`sudo apt-get install python-pip`)
  * Install [schedule](https://github.com/dbader/schedule) (`pip install schedule`)
  * Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)(`pip install beautifulsoup4`)
  * [Install gcloud following these steps](https://cloud.google.com/sdk/docs/quickstart-linux)
  * Install [Google Cloud Platform Client Library](https://cloud.google.com/compute/docs/tutorials/python-guide) (`pip install --upgrade google-api-python-client`)
* Clone this repo to your Raspberry Pi (`git clone https://github.com/MichielVanthoor/100-days-of-sunrise`)
* Run the ingestion application (`python 100-days-of-sunrise/ingestion/ingestion.py`)
