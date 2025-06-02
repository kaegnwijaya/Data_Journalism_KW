import json

f1 = open("data/data_cleansed.csv", "r")
lines = f1.readlines()

data = {}

for i in range(0, len(lines)): 
    line = lines[i].strip().split(",")
    year = int(line[0])
    state = line[1]
    num1 = float(line[2])
    num2 = float(line[3])

    if year not in data:
        data[year] = {}
    if state not in data[year]:
        data[year][state] = {}

    data[year][state]["num1"] = num1
    data[year][state]["num2"] = num2

f1.close()

f2 = open("data/data.json", "w")
json.dump(data, f2, indent=4)
f2.close()
