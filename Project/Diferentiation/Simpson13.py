import Evaluator
import sympy

class Simpson13:
    evaluator = Evaluator.Evaluator()
    def simpson13(self, a, b):
        h = float((b - a))/2
        x1 = a + h
        fa = self.evaluator.evaluate(funtion, a)
        fb = self.evaluator.evaluate(funtion, b)
        fx1 = self.evaluator.evaluate(funtion, x1)
        w = ((float(h) / 3) * (fa + (4 * fx1) + fb))
        print "El resultado sin restar el error es: ", w

simpson13 = Simpson13()
x = sympy.symbols('x')
funtion = sympy.exp(x)-2*x
a = 1
b = 2
simpson13.simpson13(a, b)
