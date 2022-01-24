from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.list_all()
    return render_template("index.html", dojos = dojos)

@app.route('/new/dojo',methods=['POST'])
def new_dojo():
    Dojo.add(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo = Dojo.get_ninjas(data))
