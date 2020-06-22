from flask import Flask,Blueprint,render_template

core = Blueprint('__name__',core)

@core.route('/')
def home():
    return render_template('core/home.html')