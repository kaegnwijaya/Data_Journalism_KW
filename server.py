# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    f = open("data/data.json", "r")
    
    return render_template('about.html')

@app.route('/micro')
def micro():
    f = open("data/data.json", "r")
    
    return render_template('micro.html')

  


app.run(debug=True)
