import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")


class Google_map:
    def __init__(self):
        self.lat = ''
        self.lng = ''

    @classmethod
    def extract_lat_lng(cls, data):
        api_url = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": data, "key": API_KEY }
        url_params = urlencode(params)
        url = f"{api_url}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200, 299): 
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"), latlng.get("lng")
        return lat, lng

