from sympy import *

class Methods:

    def __init__(self, function, gunction):
        self.func = function
        if gunction:
            self.gunction = gunction

    def f(self, number):
        sympy.init_printing(use_unicode=True)
        x = sympy.symbols('x')
        fx = eval(self.func)
        function = fx.evalf(subs={x: number})
        dfx = sympy.Derivative(fx, x).doit()
        derivative = dfx.evalf(subs={x: number})
        dfx2 = sympy.Derivative(dfx, x).doit()
        derivative2 = dfx2.evalf(subs={x: number})
        return (function, derivative, derivative2)

    def g(self, number):
        x = sympy.symbols('x')
        gx = eval(self.gunction)
        return gx

    def bisection(self, xi, xs, tolerance, iterations):
        table = PrettyTable(['Iteration', 'Xinf', 'Xsup', 'Xmi', 'f(Xmi)', 'Error'])
        fxi = self.f(xi)[0]
        fxs = self.f(xs)[0]
        root = 0
        rows = []
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
            table.add_row(row)
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
                table.add_row(row)
                rows.append(row)
            if fxm == 0:
                root = xm
            elif error < tolerance:
                root = (xm, '%.2E' % Decimal(str(error)))
            else:
                root = (None, iterations)
            print(table)
        else:
            root = None
        return (root, rows)

    def falseRule(self, xi, xs, tolerance, iterations):
        table = PrettyTable(['Iteration', 'Xinf', 'Xsup', 'Xmi', 'f(Xmi)', 'Error'])
        fxi = self.f(xi)
        fxs = self.f(xs)
        si = xi - xs
        helper = fxi - fxs
        root = 0
        if fxi == 0:
            root = xi
        elif fxs == 0:
            root = xs
        elif fxi * fxs < 0:
            if helper != 0:
                xm = xi - ((fxi * si) / helper)
                fxm = self.f(xm)
                cont = 1
                error = tolerance + 1
                table.add_row([cont, xi, xs, xm, fxm, 'Doesnt exist'])
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
                    fxm = self.f(xm)
                    error = abs(xm - aux)
                    cont += 1
                    table.add_row([cont, xi, xs, xm, fxm, '%.2E' % Decimal(str(error))])
                if fxm == 0:
                    root = xm
                elif error < tolerance:
                    root = (xm, '%.2E' % Decimal(str(error)))
                else:
                    root = (None, iterations)
                print(table)
            else:
                root = False
        else:
            root = None
        return root

    def fixedPoint(self, xa, tolerance, iterations):
        table = PrettyTable(['Iteration', 'Xn', 'f(Xn)', 'Error'])
        fx = self.f(xa)
        cont = 0
        error = tolerance + 1
        table.add_row([cont, xa, fx, 'Doesnt exist'])
        while fx != 0 and error > tolerance and cont < iterations:
            xn = g(xa)
            fx = self.f(xn)
            error = abs((xn - xa) / xn)
            xa = xn
            cont += 1
            table.add_row([cont, xn, fx, '%.2E' % Decimal(str(error))])
        if fx == 0:
            root = xa
        elif error < tolerance:
            root = (xa, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)
        print(table)
        return root

    def incremental_searches(self, x0, delta, iterations):
        fx = self.f(x0)
        root = 0
        roots = []
        if fx == 0:
            root = x0
            roots.append(x0)
        else:
            x1 = x0 + delta
            cont = 1
            fx1 = self.f(x1)
            while cont < iterations:
                x0 = x1
                fx = fx1
                x1 = x0 + delta
                fx1 = self.f(x1)
                cont += 1
                if fx1 == 0:
                    root = x1
                    roots.append(x1)
                elif fx * fx1 < 0:
                    root = (x0, x1)
                    roots.append(root)
                else:
                    root = None
        return roots

    def multipleRoots(self, x0, tolerance, iterations):
        table = PrettyTable(['Iteration', 'Xn', 'f(Xn)', 'df(Xn)', 'd(2)f(Xn)', 'Error'])
        fx = self.f(x0)[0]
        dfx = self.f(x0)[1]
        dfx2 = self.f(x0)[2]
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)),
                       'Doesnt exist'])
        while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
            numerator = fx * dfx
            denominator = (dfx ** 2) - (fx * dfx2)
            x1 = x0 - (numerator / denominator)
            fx = self.f(x1)[0]
            dfx = self.f(x1)[1]
            dfx2 = self.f(x1)[2]
            error = abs((x1 - x0) / x1)
            x0 = x1
            cont += 1
            table.add_row([cont, x1, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)),
                           '%.2E' % Decimal(str(error))])

        if fx == 0:
            root = x0
        elif error < tolerance:
            root = (x1, '%.2E' % Decimal(str(error)))
        elif dfx == 0 and fx == 0 and dfx2 != 0:
            root = x1
        else:
            root = None
        print(table)
        return root