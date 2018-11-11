import os
from flask import Flask, redirect, url_for, request, render_template, make_response
# from machine import Machine
from methods import Methods
from Systems_of_linear_equations.gauss import Gauss
from Systems_of_linear_equations.pivoting import Pivoting
from Systems_of_linear_equations.totalPivoting import Total_pivoting
from Systems_of_linear_equations.LUGauss import LU_gauss
from Systems_of_linear_equations.LUPivoting import LU_pivoting
from Systems_of_linear_equations import jacobi, jacobiSOR, cholesky, doolittle, crout, gauss_seidel
from Polynomial_Interpolation import lagrange, newton, vandermonde
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
    return render_template('lineardimension.html', section="linear")

@app.route('/linear', methods=['POST'])
def linear():
    n = int(request.form['n'])
    narray = [None]*n
    return render_template('linear.html', dimension=narray)

@app.route('/nonlinear')
def nonlinear():
    return render_template('index.html')

@app.route('/polynomialdim')
def polynomialdim():
    return render_template('lineardimension.html', section="polynomial")

@app.route('/polynomial', methods=['POST'])
def polynomial():
    n = int(request.form['n'])
    narray = [None]*n
    return render_template('polynomial.html', dimension=narray)

@app.route('/bisection', methods=['POST', 'GET'])
def bisection():
    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.bisection(xi, xs, tolerance, iterations)

    aproximacionesx = []
    aproximacionesy = []
    for row in table[1]:
        aproximacionesx.append(row[3])
        aproximacionesy.append(row[4])
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)
    if request.method == 'POST':
        return json.dumps(table)
    else:
        return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"),
                               aprox=aproximacionesx, aproy=aproximacionesy)



@app.route('/stephensen', methods=['POST', 'GET'])
def stephensen():
    func = request.form['function']
    xn = float(request.form['xn'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.stephensen(xn, tolerance,iterations)
    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/fixed', methods=['POST', 'GET'])
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

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/falseRule', methods=['POST', 'GET'])
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

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


### ESTO HAY QUE ARREGLARLO
@app.route('/incremental', methods=['POST', 'GET'])
def incremental():

    func = request.form['function']
    x0 = float(request.form['x0'])
    delta = float(request.form['delta'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.incremental_searches(x0, delta,iterations)

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table, func=func.replace("**", "^"))

@app.route('/multiple', methods=['POST', 'GET'])
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

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


## X, Y??????
@app.route('/aitken', methods=['POST', 'GET'])
def aitken():

    func = request.form['function']
    x0 = float(request.form['x0'])
    tolerance = float(request.form['tolerance'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.aitken(x0, tolerance,iterations)


    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

### X, Y???
@app.route('/aitken_bisection', methods=['POST', 'GET'])
def aitken_bisection():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.aitken_bis(xi, xs, tolerance,iterations)

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/muller', methods=['POST', 'GET'])
def muller():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.muller(xi, xs, tolerance,iterations)

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"))

@app.route('/secant', methods=['POST', 'GET'])
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

    if request.method == 'POST':
        return json.dumps(table)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


##################LINEAAAAAAAAAAAR######################

@app.route('/gauss', methods=['POST', 'GET'])
def gauss():

    g = Gauss()
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = g.clear(g.stepped(A, v), len(A))
    return render_template('resultsGauss.html', results=results, matrix=A)

@app.route('/pivoting', methods=['POST', 'GET'])
def pivoting():

    g = Pivoting()
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = g.clear(g.stepped(A, v), len(A))
    return render_template('resultsGauss.html', results=results, matrix=A)

@app.route('/lugauss', methods=['POST', 'GET'])
def lugauss():

    g = LU_gauss()
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = g.lu_gauss(A, v)
    return render_template('resultsLU.html', results=results[2], l_matrix=results[0], u_matrix=results[1])

@app.route('/lupivoting', methods=['POST', 'GET'])
def lupivoting():

    g = LU_pivoting()
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = g.lu_pivoting(A, v)
    return render_template('resultsLU.html', results=results[2], l_matrix=results[0], u_matrix=results[1])

@app.route('/cholesky', methods=['POST', 'GET'])
def cholesky():

    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = cholesky.cholesky(A)
    return render_template('resultsLU.html', l_matrix=results[0], u_matrix=results[1])

@app.route('/doolittle', methods=['POST', 'GET'])
def doolittle():

    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = doolittle.doolittle(A)
    return render_template('resultsLU.html', l_matrix=results[0], u_matrix=results[1])

@app.route('/crout', methods=['POST', 'GET'])
def crout():

    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = crout.crout(A)
    return render_template('resultsLU.html', l_matrix=results[0], u_matrix=results[1])

@app.route('/totalpivoting', methods=['POST', 'GET'])
def totalpivoting():

    g = Total_pivoting()
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)
    results = g.clear(g.stepped(A, v), [])
    return render_template('resultsGauss.html', results=results, matrix=A)

@app.route('/jacobi', methods=['POST', 'GET'])
def jaco():
    tolerance = float(request.form['tolerance'])
    x0 = float(request.form['x0'])
    iterations = float(request.form['iterations'])
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = jacobi.jacobi(tolerance, x0, iterations, A, v)
    return render_template('resultsTable.html', results=results)

@app.route('/lagrange', methods=['POST', 'GET'])
def lag():
    x = float(request.form['x'])
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = lagrange.lagrange(x, A)
    return render_template('resultsPoly.html', result=results[0], poli=results[1], x=x)

@app.route('/newton', methods=['POST', 'GET'])
def newt():
    x = float(request.form['x'])
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = newton.newton(x, A)
    return render_template('resultsPoly.html', result=results[0], poli=results[1], x=x)

@app.route('/jacobiSOR', methods=['POST', 'GET'])
def jacoSOR():
    tolerance = float(request.form['tolerance'])
    w = float(request.form['w'])
    iterations = float(request.form['iterations'])
    A = []
    v = []
    x = []
    vstr = request.form.getlist('v')
    xstr = request.form.getlist('x')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenas X
    for item in xstr:
        x.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = jacobiSOR.jacobi_SOR(A, v, x, w, iterations, tolerance)
    return render_template('resultsTable.html', results=results)

@app.route('/gaussseidel', methods=['POST', 'GET'])
def gaussseidel():
    tolerance = float(request.form['tolerance'])
    x0 = float(request.form['x0'])
    iterations = float(request.form['iterations'])
    A = []
    v = []
    vstr = request.form.getlist('v')
    # Llenas V
    for item in vstr:
        v.append(float(item))
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(int(request.form['dimension'])):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = gauss_seidel.gaussSeidel(tolerance, x0, iterations, A, v)
    return render_template('resultsTable.html', results=results)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)