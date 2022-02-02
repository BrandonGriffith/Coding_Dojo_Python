from flask import render_template, request
from flask_app import app
from flask_app.models.google_map import Google_map
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("API_KEY")


@app.route("/")
def index():
    return render_template("index.html", api_key=API_KEY)

@app.route("/location",methods=["POST"])
def get_location():
    location = Google_map.extract_lat_lng(request.form)
    return render_template("index2.html", location=location, api_key=API_KEY)
