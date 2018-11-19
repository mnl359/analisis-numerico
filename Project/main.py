import os
from flask import Flask, redirect, url_for, request, render_template, make_response
# from machine import Machine
from methods import Methods
from Systems_of_linear_equations.gauss import Gauss
from Systems_of_linear_equations.pivoting import Pivoting
from Systems_of_linear_equations.totalPivoting import Total_pivoting
from Systems_of_linear_equations.LUGauss import LU_gauss
from Systems_of_linear_equations.LUPivoting import LU_pivoting
from Systems_of_linear_equations import jacobi, jacobiSOR, cholesky, doolittle, crout, gauss_seidel, bandMatrix, gauss_seidelSOR
from Polynomial_Interpolation import lagrange, newton, vandermonde
from Splines import splines_1, splines_2, splines_3
import json, decimal, sympy
app = Flask(__name__)


user = "userdeprueba20172804"
passw = "contrasena"

state = None

def decimal_default(obj):
    # print(obj)
    try:
        val = float(obj)
        return val
    except (ValueError, TypeError) as e:
        print(str(obj), "That's not a float")
        if isinstance(obj, tuple(sympy.core.all_classes)):
            return str(obj)

    # raise TypeError


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
    return render_template('nonlinear.html')

@app.route('/polynomialdim')
def polynomialdim():
    return render_template('lineardimension.html', section="polynomial")

@app.route('/polynomial', methods=['POST'])
def polynomial():
    n = int(request.form['n'])
    narray = [None]*n
    return render_template('polynomial.html', dimension=narray)

@app.route('/splinesdimension')
def splinesdimension():
    return render_template('lineardimension.html', section="splines")

@app.route('/splines', methods=['POST'])
def splines():
    n = int(request.form['n'])
    narray = [None]*n
    return render_template('splines.html', dimension=narray)

@app.route('/bisection', methods=['POST', 'GET'])
def bisection():
    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.bisection(xi, xs, tolerance, iterations)
    print(list(table))

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[3]))
        aproximacionesy.append(float(row[4]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"),
                               aprox=aproximacionesx, aproy=aproximacionesy)



@app.route('/stephensen', methods=['POST', 'GET'])
def stephensen():
    func = request.form['function']
    xn = float(request.form['xn'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.stephensen(xn, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"),
                           aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/newtonon', methods=['POST', 'GET'])
def newtonon():
    func = request.form['function']
    xn = float(request.form['xi'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.newton(xn, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[1]))
        aproximacionesy.append(float(row[2]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"),
                           aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/fixed', methods=['POST', 'GET'])
def fixed():

    func = request.form['function']
    gunc = request.form['gunction']
    xa = float(request.form['xa'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func, gunc)
    table = methods.fixedPoint(xa, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[1]))
        aproximacionesy.append(float(row[2]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)

@app.route('/falseRule', methods=['POST', 'GET'])
def falseRule():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.falseRule(xi, xs, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[3]))
        aproximacionesy.append(float(row[4]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


@app.route('/incremental', methods=['POST', 'GET'])
def incremental():

    func = request.form['function']
    x0 = float(request.form['x0'])
    delta = float(request.form['delta'])
    iterations = int(request.form['iterations'])

    methods = Methods(func)
    table = methods.incremental_searches(x0, delta,iterations)
    print(table[1])

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[1], func=func.replace("**", "^"), aprox=[], aproy=[])

@app.route('/multiple', methods=['POST', 'GET'])
def multiple():

    func = request.form['function']
    x0 = float(request.form['x0'])
    tolerance = float(request.form['tolerance'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.multipleRoots(x0, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[1]))
        aproximacionesy.append(float(row[2]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)
    print(func)
    print(aproximacionesy)
    # print(aproximacionesx)

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


@app.route('/aitken', methods=['POST', 'GET'])
def aitken():

    func = request.form['function']
    x0 = float(request.form['x0'])
    tolerance = float(request.form['tolerance'])
    iterations = float(request.form['iterations'])

    methods = Methods(func)
    table = methods.aitken(x0, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)

    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=[], aproy=[])

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

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=[], aproy=[])

@app.route('/muller', methods=['POST', 'GET'])
def muller():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.muller(xi, xs, tolerance,iterations)

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"),  aprox=[], aproy=[])

@app.route('/secant', methods=['POST', 'GET'])
def secant():

    func = request.form['function']
    xi = float(request.form['xi'])
    xs = float(request.form['xs'])
    iterations = float(request.form['iterations'])
    tolerance = float(request.form['tolerance'])

    methods = Methods(func)
    table = methods.secant(xi, xs, tolerance,iterations)
    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    aproximacionesx = []
    aproximacionesy = []
    for row in table[2][1:]:
        aproximacionesx.append(float(row[1]))
        aproximacionesy.append(float(row[2]))
    aproximacionesx.pop(0)
    aproximacionesy.pop(0)

    if request.form.get('prueba', None):
        return json.dumps(table, default=decimal_default)
    return render_template('resultsTable.html', results=table[2], func=func.replace("**", "^"), aprox=aproximacionesx, aproy=aproximacionesy)


##################LINEAAAAAAAAAAAR######################

@app.route('/bandmatrix', methods=['POST', 'GET'])
def bandmat():

    a = []
    b = []
    c = []
    d = []
    astr = request.form.getlist('n0')
    bstr = request.form.getlist('n1')
    cstr = request.form.getlist('n2')
    dstr = request.form.getlist('n3')
    # Llenas V
    for item in astr:
        a.append(float(item))
    for item in bstr:
        b.append(float(item))
    for item in cstr:
        c.append(float(item))
    for item in dstr:
        d.append(float(item))
    results = bandMatrix.main(a, b, c, d)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsGauss.html',  results=results[1])


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
    results = g.main(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsGauss.html', results=results[2], matrix=A)

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
    results = g.main(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results)
    return render_template('resultsGauss.html', results=results[2], matrix=A)

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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsLU.html', results=results[3], l_matrix=results[1], u_matrix=results[2])

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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsLU.html', results=results[4], l_matrix=results[1], u_matrix=results[2])

@app.route('/cholesky', methods=['POST', 'GET'])
def choleskyy():

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
    results = cholesky.cholesky(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsLU.html', results=results[3], l_matrix=results[1], u_matrix=results[2])

@app.route('/doolittle', methods=['POST', 'GET'])
def doolittlee():

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
    results = doolittle.doolittle(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsLU.html', l_matrix=results[1], u_matrix=results[2])

@app.route('/crout', methods=['POST', 'GET'])
def croutt():

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
    results = crout.crout(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsLU.html', l_matrix=results[1], u_matrix=results[2])

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
    results = g.main(A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsGauss.html', results=results[3], matrix=results[1])

@app.route('/jacobi', methods=['POST', 'GET'])
def jaco():
    tolerance = float(request.form['tolerance'])
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

    x0 = []
    xstr = request.form.getlist('x0')
    # Llenas x0
    for item in xstr:
        x0.append(float(item))
    results = jacobi.jacobi(tolerance, x0, iterations, A, v)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[2], aprox=[], aproy=[])

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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[2], aprox=[], aproy=[])

@app.route('/gausSOR', methods=['POST', 'GET'])
def gausSOR():
    tolerance = float(request.form['tolerance'])
    w = float(request.form['w'])
    iterations = float(request.form['iterations'])
    A = []
    v = []
    x = []
    vstr = request.form.getlist('v')
    xstr = request.form.getlist('x')
    print(xstr)
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

    results = gauss_seidelSOR.gaussSeidel(tolerance, x, iterations, A, v, w)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[2], aprox=[], aproy=[])

@app.route('/gaussseidel', methods=['POST', 'GET'])
def gaussseidel():
    tolerance = float(request.form['tolerance'])
    x0 = []
    xstr = request.form.getlist('x0')
    # Llenas x0
    for item in xstr:
        x0.append(float(item))
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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[2], aprox=[], aproy=[])

############POLYNOMIAL INTERPOLATION#################

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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
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
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsPoly.html', result=results[0], poli=results[1], x=x)

@app.route('/vandermonde', methods=['POST', 'GET'])
def vandermonda():
    x = float(request.form['x'])
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = vandermonde.main(A, x)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsPoly.html', result=results[3], poli=results[4], x=x)

@app.route('/spline1', methods=['POST', 'GET'])
def spline1():
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = splines_1.spline1(A)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[1])

@app.route('/spline2', methods=['POST', 'GET'])
def spline2():
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = splines_2.spline2(A)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[1])

@app.route('/spline3', methods=['POST', 'GET'])
def spline3():
    A = []
    # Llenar A
    for i in range(int(request.form['dimension'])):
        aux = []
        arstr = request.form.getlist('n' + str(i))
        for j in range(2):
            aux.append(float(arstr[j]))
        A.append(aux)

    results = splines_3.spline3(A)
    if request.form.get('prueba', None):
        return json.dumps(results, default=decimal_default)
    return render_template('resultsTable.html', results=results[1])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)