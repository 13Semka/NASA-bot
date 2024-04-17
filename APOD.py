import requests
from config_reader import config
from wget import download
import re

down_dir = "./down_dir"

def get_APOD():
    APOD_response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={config.API_KEY.get_secret_value()}").json()
    APOD_title = APOD_response["title"]
    APOD_explanation = APOD_response["explanation"]
    APOD_copyright = APOD_response["copyright"]
    APOD_hdurl = APOD_response["hdurl"]


    APOD_url = APOD_response["url"]
    pattern = r'\/([^\/?#]+\.[^\/?#]+)$'
    match = re.search(pattern, APOD_url)
    filename = match.group(1)

    download(APOD_url, down_dir)

    return APOD_title, APOD_explanation, APOD_hdurl, APOD_copyright, filename
