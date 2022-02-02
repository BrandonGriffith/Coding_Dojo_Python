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
        loc_query = data
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": loc_query, "key": API_KEY }
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200, 299): 
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"), latlng.get("lng")
        cls.lat = lat
        cls.lng = lng
        return lat, lng

