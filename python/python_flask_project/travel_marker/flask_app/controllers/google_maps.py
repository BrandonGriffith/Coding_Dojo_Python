from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.google_map import Google_map
from flask_app.models.wiki import *
from dotenv import load_dotenv
import os
load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


@app.route("/")
def index():
    return render_template("index.html", google_api_key=GOOGLE_API_KEY)

@app.route("/location",methods=["POST"])
def get_location():
    location = Google_map.extract_lat_lng(request.form)
    if location[0] == None:
        return redirect("/")
    wiki_sum = wiki_summary(request.form['location'])
    return render_template("index2.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum)
