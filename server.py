# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    average = []
    for i in data["Mexico"].keys():
        average.append((float(data["Mexico"][i]) + float(data["United States"][i]) + float(data["Canada"][i]))/3)




    return render_template('index.html', data = data, years = data["Mexico"].keys(), mexico = data["Mexico"].values(), usa = data["United States"].values(), canada = data["Canada"].values(), average = average)

@app.route('/year')
def year(): 
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    selected_year = request.args.get('year')
    mexicoVal = float(data["Mexico"][selected_year])
    usaVal = float(data["United States"][selected_year])
    canadaVal = float(data["Canada"][selected_year])
    allVal = [mexicoVal, usaVal, canadaVal]

    legend = [(a, 81.92 - a / 16.73) for a in range(0, 500, 50)]

    closest_a_values = []

    for val in allVal:
        closest = min(legend, key=lambda pair: abs(val - pair[1]))
        closest_a_values.append(closest[0])  


    return render_template('year.html', mex = mexicoVal, am = usaVal, can = canadaVal, mexicoVal = closest_a_values[0], usaVal = closest_a_values[1], canadaVal = closest_a_values[2], year = selected_year, data = data, years = data["Mexico"].keys())

    


app.run(debug=True)
