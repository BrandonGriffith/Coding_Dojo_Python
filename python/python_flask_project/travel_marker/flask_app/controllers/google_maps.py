from flask import render_template, request
from flask_app import app
from flask_app.models.google_map import Google_maps



@app.route("/location",methods=["POST"])
def get_location():
    location = Google_maps.extract_lat_lng(request.form)
    api_key = "AIzaSyCEDhiHaU2a4aVHM78GeSPU8P8Tud9B9g0"
    return render_template("index2.html", location=location, api_key=api_key)



