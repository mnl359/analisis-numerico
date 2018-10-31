import os
from flask import Flask, redirect, url_for, request, render_template, make_response
# from machine import Machine
from methods import Methods
import json
app = Flask(__name__)


user = "userdeprueba20172804"
passw = "contrasena"

state = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lineardimension')
def lineardimension():
    return render_template('lineardimension.html')

@app.route('/linear', methods=['POST'])
def linear():
    n = int(request.form['n'])
    narray = [None]*n
    return render_template('linear.html', dimension=narray)

@app.route('/nonlinear')
def nonlinear():
    return render_template('index.html')

@app.route('/bisection', methods=['POST'])
def bisection():
    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.bisection(xi, xs, tolerance,iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[3])
        aproximacionesy.append(row[4])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/stephensen', methods=['POST'])
def stephensen():
    func = request.form['function']
    xn = float(request.form['xn'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.stephensen(xn, tolerance,iterations)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/fixed', methods=['POST'])
def fixed():

    func = request.form['function']
    gunc = request.form['gunction']
    xa = float(request.form['xa'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func, gunc)
    table = methods.fixedPoint(xa, tolerance,iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[1])
        aproximacionesy.append(row[2])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/falseRule', methods=['POST'])
def falseRule():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.falseRule(xi, xs, tolerance,iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[3])
        aproximacionesy.append(row[4])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


### ESTO HAY QUE ARREGLARLO
@app.route('/incremental', methods=['POST'])
def incremental():

    func = request.form['function']
    x0 = float(request.form['x0'])
    delta = float(request.form['delta'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.incremental_searches(x0, delta,iterations)


    return render_template('resultsTable.html', results=table, func=func.replace("**", "^"))

@app.route('/multiple', methods=['POST'])
def multiple():

    func = request.form['function']
    x0 = float(request.form['x0'])
    tolerance = float(request.form['tolerance'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.multipleRoots(x0, tolerance,iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[1])
        aproximacionesy.append(row[2])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


## X, Y??????
@app.route('/aitken', methods=['POST'])
def aitken():

    func = request.form['function']
    x0 = float(request.form['x0'])
    tolerance = float(request.form['tolerance'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.aitken(x0, tolerance,iterations)


    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

### X, Y???
@app.route('/aitken_bisection', methods=['POST'])
def aitken_bisection():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.aitken_bis(xi, xs, tolerance,iterations)


    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/muller', methods=['POST'])
def muller():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.muller(xi, xs, tolerance,iterations)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/secant', methods=['POST'])
def secant():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.secant(xi, xs, tolerance,iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[1])
        aproximacionesy.append(row[2])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)