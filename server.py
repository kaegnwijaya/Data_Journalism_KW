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
    diff = 0
    steps = []
    for year in years:
        for state in states:
            if data[year][state]["num2"] > max:
                max = data[year][state]["num2"]
            if data[year][state]["num2"] < min:
                min = data[year][state]["num2"]

    diff = max - min
    diff = diff/10

    for i in range(0, 10, 1):
        steps.append(max - (i * diff))

    


    
    return render_template('macro.html', query = "ageadjusted", diff = diff, steps = steps, max = max, min = min, data = data, abbs = abbs, states = states, years = years, year = selected_year)

@app.route('/newyork')
def newyork():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    ny = []
    us = []
    num = 0
    years = data.keys()
    states = data["2014"].keys() 
    for i in years:
        ny.append(data[i][".ny"]["num1"])
        num = 0
        for k in data[i]:
            num = num + (data[i][k]["num1"])/50
        us.append(num)

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
    diff = diff/13

    for i in range(0, 14, 1):
        steps.append(round(max - (i * diff)))

    avg = 0
    for i in ny:
        avg = avg + i
    avg = avg/len(ny)
    avg = round(avg)

    avgTot = 0
    for i in us:
        avgTot = avgTot + i
    avgTot = avgTot/len(us)
    avgTot = round(avgTot)

    if(avg > avgTot):
        which = "higher"
    else:
        which = "lower"

    return render_template('micro.html', which = which,avg = avg, avgTot = avgTot,steps =steps,ny = ny, us = us, years = years, query = "NY")

@app.route('/florida')
def florida():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    fl = []
    us = []
    num = 0
    years = data.keys()
    states = data["2014"].keys() 
    for i in years:
        fl.append(data[i][".fl"]["num1"])
        num = 0
        for k in data[i]:
            num = num + (data[i][k]["num1"])/50
        us.append(num)

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
    diff = diff/13

    for i in range(0, 14, 1):
        steps.append(round(max - (i * diff)))

    avg = 0
    for i in fl:
        avg = avg + i
    avg = avg/len(fl)
    avg = round(avg)

    avgTot = 0
    for i in us:
        avgTot = avgTot + i
    avgTot = avgTot/len(us)
    avgTot = round(avgTot)

    if(avg > avgTot):
        which = "higher"
    else:
        which = "lower"
    
    return render_template('micro.html',which = which,avg = avg, avgTot = avgTot, steps =steps,fl = fl, us = us, years = years, query = "FL")

@app.route('/california')
def california():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    fl = []
    us = []
    num = 0
    years = data.keys()
    states = data["2014"].keys() 
    for i in years:
        fl.append(data[i][".ca"]["num1"])
        num = 0
        for k in data[i]:
            num = num + (data[i][k]["num1"])/50
        us.append(num)

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
    diff = diff/13

    for i in range(0, 14, 1):
        steps.append(round(max - (i * diff)))

    avg = 0
    for i in fl:
        avg = avg + i
    avg = avg/len(fl)
    avg = round(avg)

    avgTot = 0
    for i in us:
        avgTot = avgTot + i
    avgTot = avgTot/len(us)
    avgTot = round(avgTot)

    if(avg > avgTot):
        which = "higher"
    else:
        which = "lower"
    
    return render_template('micro.html',which = which,avg = avg, avgTot = avgTot, steps =steps,fl = fl, us = us, years = years, query = "CA")

@app.route('/wyoming')
def wyoming():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    fl = []
    us = []
    num = 0
    years = data.keys()
    states = data["2014"].keys() 
    for i in years:
        fl.append(data[i][".wy"]["num1"])
        num = 0
        for k in data[i]:
            num = num + (data[i][k]["num1"])/50
        us.append(num)

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
    diff = diff/13

    for i in range(0, 14, 1):
        steps.append(round(max - (i * diff)))

    avg = 0
    for i in fl:
        avg = avg + i
    avg = avg/len(fl)
    avg = round(avg)

    avgTot = 0
    for i in us:
        avgTot = avgTot + i
    avgTot = avgTot/len(us)
    avgTot = round(avgTot)

    if(avg > avgTot):
        which = "higher"
    else:
        which = "lower"
    
    return render_template('micro.html',which = which,avg = avg, avgTot = avgTot, steps =steps,fl = fl, us = us, years = years, query = "WY")

@app.route('/texas')
def texas():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    fl = []
    us = []
    num = 0
    years = data.keys()
    states = data["2014"].keys() 
    for i in years:
        fl.append(data[i][".tx"]["num1"])
        num = 0
        for k in data[i]:
            num = num + (data[i][k]["num1"])/50
        us.append(num)

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
    diff = diff/13

    for i in range(0, 14, 1):
        steps.append(round(max - (i * diff)))

    avg = 0
    for i in fl:
        avg = avg + i
    avg = avg/len(fl)
    avg = round(avg)

    avgTot = 0
    for i in us:
        avgTot = avgTot + i
    avgTot = avgTot/len(us)
    avgTot = round(avgTot)

    if(avg > avgTot):
        which = "higher"
    else:
        which = "lower"
    
    return render_template('micro.html', which = which,avg = avg, avgTot = avgTot, steps =steps,fl = fl, us = us, years = years, query = "TX")

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
    maxE = 0
    minE = 999999
    maxPep = 0
    minPep = 999999
    total = 0
    maxState = "";
    minState = "";
    diff = 0
    steps = []
    

    if(selected_year is not None):
        maxState = max(data[selected_year], key=lambda k: data[selected_year][k]["num1"])
        minState = min(data[selected_year], key=lambda k: data[selected_year][k]["num1"])
        maxState = maxState.strip(".").upper()
        minState = minState.strip(".").upper()
        for state in states:
            total = total + data[selected_year][state]["num1"]
            if data[selected_year][state]["num1"] > maxPep:
                maxPep = data[selected_year][state]["num1"]
            if data[selected_year][state]["num1"] < minPep:
                minPep = data[selected_year][state]["num1"]

    

    for year in years:
        for state in states:
            if data[year][state]["num1"] > maxE:
                maxE = data[year][state]["num1"]
            if data[year][state]["num1"] < minE:
                minE = data[year][state]["num1"]



    diff = maxE - minE
    diff = diff/10

    for i in range(0, 10, 1):
        steps.append(maxE - (i * diff))

    steps = steps[::-1]

    


    
    return render_template('macro.html',total = int(total),maxPep = int(maxPep), minPep = int(minPep),maxState = maxState, minState = minState, query = "macro", diff = diff, steps = steps, max = maxE, min = minE, data = data, abbs = abbs, states = states, years = years, year = selected_year)

  


app.run(debug=True)
