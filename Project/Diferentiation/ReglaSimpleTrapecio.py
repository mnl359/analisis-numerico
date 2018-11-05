import sympy, Evaluator

class ReglaSimpleTrapecio:
    evaluator = Evaluator.Evaluator()

    def simpleTrapecio(self, a, b):
        x = sympy.symbols('x')
        f = sympy.exp(x) - 2*x
        h = b - a
        fa = self.evaluator.evaluate(f, a)
        fb = self.evaluator.evaluate(f, b)
        print (float(h)/2)*(fa+fb)

rs = ReglaSimpleTrapecio()
a = 1
b = 2
rs.simpleTrapecio(a, b)