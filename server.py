# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    
    return render_template('about.html')

@app.route('/ageadjusted')
def ageadjust():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data.keys()
    states = data["2014"].keys() 
    abbs = [
    ".ak", ".al", ".ar", ".az", ".ca", ".co", ".ct", ".de", ".fl", ".ga",
    ".hi", ".ia", ".id", ".il", ".in", ".ks", ".ky", ".la", ".ma", ".md",
    ".me", ".mi", ".mn", ".mo", ".ms", ".mt", ".nc", ".nd", ".ne", ".nh",
    ".nj", ".nm", ".nv", ".ny", ".oh", ".ok", ".or", ".pa", ".ri", ".sc",
    ".sd", ".tn", ".tx", ".ut", ".va", ".vt", ".wa", ".wi", ".wv", ".wy"
    ]
    selected_year = request.args.get('year')
    max = 0
    min = 999999
    for year in years:
        for state in states:
            if data[year][state]["num1"] > max:
                max = data[year][state]["num1"]
            if data[year][state]["num1"] < min:
                min = data[year][state]["num1"]

    


    
    return render_template('macro.html',max = max, min = min,data = data, abbs = abbs, states = states, years = years, year = selected_year, query = "ageadjusted")


@app.route('/micro')
def micro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    
    return render_template('micro.html')

@app.route('/macro')
def macro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data.keys()
    states = data["2014"].keys() 
    abbs = [
    ".ak", ".al", ".ar", ".az", ".ca", ".co", ".ct", ".de", ".fl", ".ga",
    ".hi", ".ia", ".id", ".il", ".in", ".ks", ".ky", ".la", ".ma", ".md",
    ".me", ".mi", ".mn", ".mo", ".ms", ".mt", ".nc", ".nd", ".ne", ".nh",
    ".nj", ".nm", ".nv", ".ny", ".oh", ".ok", ".or", ".pa", ".ri", ".sc",
    ".sd", ".tn", ".tx", ".ut", ".va", ".vt", ".wa", ".wi", ".wv", ".wy"
    ]
    selected_year = request.args.get('year')
    max = 0
    min = 999999
    diff = 0
    steps = []
    for year in years:
        for state in states:
            if data[year][state]["num1"] > max:
                max = data[year][state]["num1"]
            if data[year][state]["num1"] < min:
                min = data[year][state]["num1"]

    diff = max - min
    diff = diff/10

    for i in range(0, 10, 1):
        steps.append(max - (i * diff))

    


    
    return render_template('macro.html', steps = steps, max = max, min = min, data = data, abbs = abbs, states = states, years = years, year = selected_year)

  


app.run(debug=True)
