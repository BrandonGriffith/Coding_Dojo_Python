import requests
from urllib.parse import urlencode


class Google_maps:
    def __init__(self):
        self.api_key = 'AIzaSyCEDhiHaU2a4aVHM78GeSPU8P8Tud9B9g0'
        self.lat = ''
        self.lng = ''
    api_key = 'AIzaSyCEDhiHaU2a4aVHM78GeSPU8P8Tud9B9g0'

    @classmethod
    def extract_lat_lng(cls, data):
        loc_query = data
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": loc_query, "key": cls.api_key }
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

