from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html', dojos = dojo.Dojo.list_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.addNinja(request.form)
    return redirect('/')
