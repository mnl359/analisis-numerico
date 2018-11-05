import Evaluator
import sympy

class Simpson13compuesto:
    evaluator = Evaluator.Evaluator()
    def simpson13compuesto(self, a, b, n):
        if (n%2!=0):
           print ("El numero de intervalos debe ser par")
        else:
            h = float((b - a))/n
            integ = self.evaluator.evaluate(funtion, a)
            suma1 = 0
            suma2 = 0
            for i in range(1, n):
                if (i%2==1):
                    fa = self.evaluator.evaluate(funtion, (a+i*h))
                    suma1 += fa
                else:
                    fa = self.evaluator.evaluate(funtion, (a+i*h))
                    suma2 += fa
            integ += 4*suma1
            integ += 2*suma2
            fb = self.evaluator.evaluate(funtion, b)
            integ += fb
            result = (float(h) / 3) * integ
            print "El resultado es: ", result

simpson13compuesto = Simpson13compuesto()
x = sympy.symbols('x')
funtion = sympy.exp(x)-2*x
a = 1
b = 2
n = 10 #numero de intervalos
simpson13compuesto.simpson13compuesto(a, b, n)
