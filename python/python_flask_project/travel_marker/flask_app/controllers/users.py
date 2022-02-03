from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.fav import *
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/register",methods=["POST"])
def register():
    if not User.validate(request.form):
        return redirect("/")
    data ={ 
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    session["user_id"] = User.add(data)
    return redirect("/")

@app.route("/login",methods=["POST"])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("email not found","login")
        return redirect("/")
    elif not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("password is wrong","login")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/")

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/fav_it",methods=["POST"])
def fav_it():
    if "user_id" not in session:
        return redirect("/")
    session["location"] = request.form['location']
    fav1 = add_fav(session)
    return redirect("/user_home")

