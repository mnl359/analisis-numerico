import os
from flask import Flask, redirect, url_for, request, render_template, make_response
from machine import Machine
app = Flask(__name__)


user = "userdeprueba20172804"
passw = "contrasena"

state = None

@app.route('/')
def home():
    machine = Machine(8, 8)
    maximo = machine.biggest()
    minimo = machine.lowest()
    return render_template('home.html', maximo=maximo, minimo=minimo)

@app.route('/machine', methods=['POST'])
def machine():

    if request.form['mantissa'] != '' and request.form['exponent'] != '':
        mantissa = request.form['mantissa']
        exponent = request.form['exponent']
    else:
        mantissa = request.cookies.get('mantissa')
        exponent = request.cookies.get('exponent')

    if int(mantissa) + int(exponent) == 10:

        machine = Machine(int(mantissa), int(exponent))
        maximum = machine.biggest()
        minimum = machine.lowest()
        positive = machine.positive()
        resp = make_response(render_template('machine.html', maximum=maximum, minimum=minimum, binary=0, positive=positive))
        resp.set_cookie('exponent', value=exponent, max_age=90)
        resp.set_cookie('mantissa', value=mantissa, max_age=90)

        return resp
    else:
        return mantissa+exponent

@app.route('/number', methods=['POST'])
def number():
    number = request.form['number']
    exponent = request.cookies.get('exponent')
    mantissa = request.cookies.get('mantissa')
    machine = Machine(int(mantissa), int(exponent))
    maximum = machine.biggest()
    minimum = machine.lowest()
    epsilon = machine.epsilon()
    binary = machine.machine_number(number)
    positive = machine.positive()
    return render_template('machine.html', maximum=maximum, minimum=minimum, binary=binary, decimal=number, epsilon=epsilon, positive=positive)

@app.route('/binary', methods=['POST'])
def binary():
    binary = request.form['binary']
    exponent = request.cookies.get('exponent')
    mantissa = request.cookies.get('mantissa')
    machine = Machine(int(mantissa), int(exponent))
    maximum = machine.biggest()
    minimum = machine.lowest()
    epsilon = machine.epsilon()
    decimal = machine.decimalNumber(binary)
    positive = machine.positive()
    return render_template('machine.html', maximum=maximum, minimum=minimum, binary=binary, decimal=decimal, epsilon=epsilon, positive=positive)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)