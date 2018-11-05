import sympy 
class Evaluator:

    def evaluate(self, f, x0):
        x = sympy.symbols('x')
        return f.evalf(subs={x:x0})

