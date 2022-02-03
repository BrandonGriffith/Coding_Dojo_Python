from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.google_map import Google_map
from flask_app.models.wiki import *
from flask_app.models.fav import *
from dotenv import load_dotenv
import os
load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


@app.route("/")
def index():
    location = Google_map.extract_lat_lng([('location', 'Mountain View, CA')])
    wiki_sum = wiki_summary("Google Maps")
    print(session)
    if "user_id" not in session:
        return render_template("index.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum)
    user_favs = get_fav(session)
    return render_template("user_home_page.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum, user_favs=user_favs)

@app.route("/location",methods=["POST"])
def get_location():
    session["location"] = request.form['location']
    location = Google_map.extract_lat_lng(request.form)
    if location[0] == None:
        return redirect("/")
    wiki_sum = wiki_summary(request.form['location'])
    print(session)
    if "user_id" not in session:
        return render_template("index2.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum)
    user_favs = get_fav(session)
    return render_template("user_home_page.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum, user_favs=user_favs)

@app.route("/user_home")
def user_home():
    location = Google_map.extract_lat_lng([('location', 'Mountain View, CA')])
    wiki_sum = wiki_summary("Google Maps")
    if "user_id" not in session:
        return render_template("index2.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum)
    user_favs = get_fav(session)
    return render_template("user_home_page.html", location=location, google_api_key=GOOGLE_API_KEY, wiki_sum=wiki_sum, user_favs=user_favs)


