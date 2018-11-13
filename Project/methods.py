from sympy import *
from decimal import Decimal
class Methods:

    def __init__(self, function, gunction=''):
        self.func = function
        if gunction:
            self.gunction = gunction

    def f(self, number):
        init_printing(use_unicode=True)
        x = symbols('x')
        fx = eval(self.func)
        function = fx.evalf(subs={x: number})
        dfx = Derivative(fx, x).doit()
        derivative = dfx.evalf(subs={x: number})
        dfx2 = Derivative(dfx, x).doit()
        derivative2 = dfx2.evalf(subs={x: number})
        return (function, derivative, derivative2)

    def g(self, number):
        x = symbols('x')
        gx = eval(self.gunction)
        return gx

    def newton(self, x0, tolerance, iterations):
        table = [['Iteration', 'Xn', 'f(Xn)', 'df(Xn)', 'Error']]
        fx = self.f(x0)[0]
        dfx = self.f(x0)[1]
        cont = 0
        error = tolerance + 1
        table.append([cont, x0, fx, dfx, 'Doesnt exist'])
        while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
            x1 = x0 - (fx / dfx)
            fx = self.f(x1)[0]
            dfx = self.f(x1)[1]
            error = abs((x1 - x0) / x1)
            x0 = x1
            cont += 1
            table.append([cont, x1, fx, dfx, '%.2E' % Decimal(str(error))])
        if fx == 0:
            root = (x0, '%.2E' % Decimal(str(error)))
        elif error < tolerance:
            root = (x1, '%.2E' % Decimal(str(error)))
        elif dfx == 0:
            root = (x1, "Multiple root")
        else:
            root = None
        print(table)
        return 0, root, table, cont

    def stephensen(self, xn, tolerance, iterations):
        table = [['Iteration', 'Xn', 'Error Absoluto']]
        fxn = self.f(xn)[0]
        root = 0
        if fxn == 0:
            root = xn
        else:
            cont = 0
            error = tolerance + 1
            table.append([cont, xn, 'Doesnt exist'])

            while cont < iterations and error > tolerance:

                fxn = self.f(xn)[0]
                den = self.f(xn + fxn)[0] - fxn  # Denominator
                if den == 0:
                    print ("The denominator became 0.")
                    break
                xn1 = xn - (fxn ** 2) / den

                error = abs((xn1 - xn))  # Abs error
                cont += 1
                table.append([cont, xn1, '%.2E' % Decimal(str(error))])
                xn = xn1
                # prev = aux

            if error < tolerance:
                root = (xn1, '%.2E' % Decimal(str(error)))
            else:
                if (cont == iterations):
                    return(1, "Method failed in %d iterations" %cont)
                else:
                    root = (xn1, '%.2E' % Decimal(str(error)))
        return 0, root, table, cont

    def secant(self, x0, x1, tolerance, iterations):
        fx0 = self.f(x0)[0]
        root = 0
        if fx0 == 0:
            root = x0
        else:
            fx1 = self.f(x1)[0]
            cont = 0
            error = tolerance + 1
            den = fx1 - fx0
            table = [[cont, x0, '%.2E' % Decimal(str(fx0)), 'Doesnt exist']]
            cont += 1
            table.append([cont, x1, '%.2E' % Decimal(str(fx1)), 'Doesnt exist'])
            while error > tolerance and fx1 != 0 and den != 0 and cont < iterations:
                cont += 1
                x2 = x1 - ((fx1 * (x1 - x0)) / den)
                error = abs((x2 - x1))
                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = self.f(x1)[0]
                den = fx1 - fx0
                table.append([cont, x1, '%.2E' % Decimal(str(fx1)), '%.2E' % Decimal(str(error))])
            if fx1 == 0:
                root = x1
            elif error < tolerance:
                root = (x1, '%.2E' % Decimal(str(error)))
            elif den == 0:
                return(1, "Multiple roots")
            else:
                return(1, "Method failed in %d iterations" %cont)
        return (0, root, table, cont)

    def bisection(self, xi, xs, tolerance, iterations):
        fxi = self.f(xi)[0]
        fxs = self.f(xs)[0]
        root = 0
        rows = [['Iteration', 'Xinf', 'Xsup', 'Xmi', 'f(Xmi)', 'Error']]
        if fxi == 0:
            root = xi
        elif fxs == 0:
            root = xs
        elif fxi * fxs < 0:
            xm = (xi + xs) / 2
            fxm = self.f(xm)[0]
            cont = 1
            error = tolerance + 1
            row = [cont, xi, xs, xm, fxm, 'Doesnt exist']
            rows.append(row)
            while error > tolerance and fxm != 0 and cont < iterations:
                if fxi * fxm < 0:
                    xs = xm
                    fxs = fxm
                else:
                    xi = xm
                    fxi = fxm
                aux = xm
                xm = (xi + xs) / 2
                fxm = self.f(xm)[0]
                error = abs(xm - aux)
                cont += 1
                row = [cont, xi, xs, xm, fxm, '%.2E' % Decimal(str(error))]
                rows.append(row)
            if fxm == 0:
                root = xm
            elif error < tolerance:
                root = (xm, '%.2E' % Decimal(str(error)))
            else:
                return(1, "Method failed in %d iterations\n\
                Try with a closest interval or more iterations" %cont)
        else:
            return(1, "There is no change in this interval")
        return (0, root, rows, cont)

    def falseRule(self, xi, xs, tolerance, iterations):
        fxi = self.f(xi)[0]
        fxs = self.f(xs)[0]
        si = xi - xs
        helper = fxi - fxs
        root = 0
        rows = [['Iteration', 'Xinf', 'Xsup', 'Xmi', 'f(Xmi)', 'Error']]
        if fxi == 0:
            root = xi
        elif fxs == 0:
            root = xs
        elif fxi * fxs < 0:
            if helper != 0:
                xm = xi - ((fxi * si) / helper)
                fxm = self.f(xm)[0]
                cont = 1
                error = tolerance + 1
                rows.append([cont, xi, xs, xm, fxm, 'Doesnt exist'])
                while error > tolerance and fxm != 0 and cont < iterations:
                    if fxi * fxm < 0:
                        xs = xm
                        fxs = fxm
                    else:
                        xi = xm
                        fxi = fxm
                    aux = xm
                    si = xi - xs
                    helper = fxi - fxs
                    if helper == 0:
                        break
                    xm = xi - ((fxi * si) / helper)
                    fxm = self.f(xm)[0]
                    error = abs(xm - aux)
                    cont += 1
                    rows.append([cont, xi, xs, xm, fxm, '%.2E' % Decimal(str(error))])
                if fxm == 0:
                    root = xm
                elif error < tolerance:
                    root = (xm, '%.2E' % Decimal(str(error)))
                else:
                    return(1, "Method failed in %d iterations" %cont)
                #print(rows)
            else:
                root = False #NO RECUERDO LO QUE SIGNIFICA ESTO
        else:
            return(1, "There is no change in this interval")
        return (0, root, rows, cont)

    def fixedPoint(self, xa, tolerance, iterations):
        table = [['Iteration', 'Xn', 'f(Xn)', 'Error']]
        fx = self.f(xa)[0]
        cont = 0
        error = tolerance + 1
        table.append([cont, xa, fx, 'Doesnt exist'])
        while fx != 0 and error > tolerance and cont < iterations:
            xn = self.g(xa)
            fx = self.f(xn)[0]
            error = abs(xn - xa)
            xa = xn
            cont += 1
            table.append([cont, xn, fx, '%.2E' % Decimal(str(error))])
        if fx == 0:
            root = xa
        elif error < tolerance:
            root = (xa, '%.2E' % Decimal(str(error)))
        else:
            return(1, "Method failed in %d iterations" %cont)
        return (0, root, table, cont)

    # Este método no retorna tabla. 
    # Retorna 0 (exitoso), 
    def incremental_searches(self, x0, delta, iterations):
        fx = self.f(x0)[0]
        root = 0
        roots = [['Roots']]
        if fx == 0:
            root = x0
            roots.append(x0)
        else:
            x1 = x0 + delta
            cont = 1
            fx1 = self.f(x1)[0]
            while cont < iterations:
                if fx1 == 0:
                    root = x1
                    roots.append(x1)
                elif fx * fx1 < 0:
                    root = (x0, x1)
                    roots.append(root)
                else:
                    root = None
                x0 = x1
                fx = fx1
                x1 = x0 + delta
                fx1 = self.f(x1)[0]
                cont += 1
        return 0, roots, cont

    def multipleRoots(self, x0, tolerance, iterations):
        table = [['Iteration', 'Xn', 'f(Xn)', 'df(Xn)', 'd(2)f(Xn)', 'Error']]
        fx = self.f(x0)[0]
        dfx = self.f(x0)[1]
        dfx2 = self.f(x0)[2]
        cont = 0
        error = tolerance + 1
        table.append([cont, x0, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)), 'Doesnt exist'])
        while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
            numerator = fx * dfx
            denominator = (dfx ** 2) - (fx * dfx2)
            x1 = x0 - (numerator / denominator)
            fx = self.f(x1)[0]
            dfx = self.f(x1)[1]
            dfx2 = self.f(x1)[2]
            error = abs(x1 - x0)
            x0 = x1
            cont += 1
            table.append([cont, x1, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)), '%.2E' % Decimal(str(error))])

        if fx == 0:
            root = x0
        elif error < tolerance:
            root = (x1, '%.2E' % Decimal(str(error)))
        elif dfx == 0 and fx == 0 and dfx2 != 0:
            root = x1
        else:
            return(1, "Method failed in %d iterations" %cont)
        #print(table)
        return (0, root, table, cont)

    def aitken(self, x0, tolerance, iterations):
        table = [['Iteration', 'Xn', 'Absolute Error']]
        fx0 = self.f(x0)[0]
        root = 0
        if fx0 == 0:
            root = x0
        else:
            cont = 0
            error = tolerance + 1
            table.append([cont, x0, 'Doesnt exist'])
            prev = x0

            while cont < iterations and error > tolerance:
                x1 = self.f(x0)[0]
                x2 = self.f(x1)[0]

                if (x2 - x1) - (x1 - x0) == 0:
                    break
                aux = x2 - (((x2 - x1) ** 2) / ((x2 - x1) - (x1 - x0)))
                if aux == 0:
                    break
                error = abs((aux - prev))  # Error absoluto
                cont += 1
                table.append([cont, aux, '%.2E' % Decimal(str(error))])
                x0 = x1
                prev = aux

            if error < tolerance:
                root = (aux, '%.2E' % Decimal(str(error)))
            else:
                return(1, "Method failed in %d iterations" %cont)

            #print(table)
        return (0, root, table, cont)

    def bis(self, a, b):
        fa = self.f(a)[0]
        x = (a + b) / 2.0
        fx = self.f(x)[0]
        if (fa * fx) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2.0
        return a, b, x

    def aitken_bis(self, a, b, tolerance, iterations):
        table = [['Iteration', 'Xn', 'Absolute Error']]
        x0 = (a + b) / 2.0
        fa = self.f(a)[0]
        fb = self.f(b)[0]
        fx0 = self.f(x0)[0]
        root = 0
        if fx0 == 0:
            root = x0
        elif fa == 0:
            root = a
        elif fb == 0:
            root = b
        else:
            cont = 0
            error = tolerance + 1
            table.append([cont, x0, 'Doesnt exist'])
            prev = x0

            while cont < iterations and (error > tolerance or error == 0):
                a1, b1, x1 = self.bis(a, b)
                a2, b2, x2 = self.bis(a1, b1)
                den = (x2 - x1) - (x1 - x0)
                if den == 0:
                    print("The denominator became 0.")
                    break
                xn = x2 - (((x2 - x1) ** 2) / den)
                if xn == prev:
                    a, b, x0 = a1, b1, x1
                    prev = xn
                    continue
                error = abs(xn - prev)  # Error absoluto
                cont += 1
                table.append([cont, xn, '%.2E' % Decimal(str(error))])
                a, b, x0 = a1, b1, x1
                prev = xn

            if error < tolerance:
                root = (xn, '%.2E' % Decimal(str(error)))
            else:
                #print (error)
                return(1, "Method failed in %d iterations" %cont)

            #print(table)
        return (0, root, table, cont)

    def muller(self, x0, x1, tolerance, iterations):
        table = [['Iteration', 'X1', 'X2', 'X3', 'Absolute Error']]
        x2 = (x1 - x0) / 2.0  # We get the third value using bisection
        fx0 = self.f(x0)[0]
        fx1 = self.f(x1)[0]
        fx2 = self.f(x2)[0]
        root = 0
        if fx0 == 0:
            root = x0
        elif fx1 == 0:
            root = x1
        if fx2 == 0:
            root = x2
        else:
            cont = 0
            error = tolerance + 1
            table.append([cont, x0, x1, x2, 'Doesnt exist'])

            while cont < iterations and error > tolerance:
                h0 = x1 - x0
                h1 = x2 - x1
                if (h0 == 0) | (h1 == 0):
                    print ("h0 or h1 became 0.")
                    break
                delta0 = (fx1 - fx0) / h0
                delta1 = (fx2 - fx1) / h1
                if h1 - h0 == 0:
                    print ("h1 - h0 became 0.")
                    break
                a = (delta1 - delta0) / (h1 - h0)
                b = a * h1 + delta1
                c = fx2
                # Solving the quadratic equation
                den = 1
                if b < 0:
                    den = b - sqrt(b ** 2 - 4 * a * c)
                else:
                    den = b + sqrt(b ** 2 - 4 * a * c)
                x3 = x2 + (-2 * c) / den

                error = abs(x3 - x2)  # Abs error
                cont += 1
                table.append([cont, x1, x2, x3, '%.2E' % Decimal(str(error))])
                x0 = x1
                x1 = x2
                x2 = x3
                fx0 = fx1
                fx1 = fx2
                fx2 = self.f(x3)[0]

            if error < tolerance:
                root = (x3, '%.2E' % Decimal(str(error)))
            else:
                if (cont == iterations):
                    #print ("The method failed.")
                    return(1, "Method failed in %d iterations" %cont)
                else:
                    root = (x3, '%.2E' % Decimal(str(error)))

            #print(table)
        return (0, root, table, cont)
