import sympy, Evaluator

class ReglaCompuestaTrapecio:
    evaluator = Evaluator.Evaluator()

    def compuestaTrapecio(self, a, b, n):
        x = sympy.symbols('x')
        f = sympy.exp(x) - 2*x #Funcion a integrar
        h = float(b - a)/n
        s = 0
        xi = a + h
        for i in range(1, n):
            s += self.evaluator.evaluate(f, xi)
            xi+=h
        fa = self.evaluator.evaluate(f, a)
        fb = self.evaluator.evaluate(f, b)
        print (float(h)/2)*(fa+(2*s)+fb)

rc = ReglaCompuestaTrapecio()
a = 1 # Limite superior integral
b = 2 # Limite inferior integral
n = 10
rc.compuestaTrapecio(a, b, n)