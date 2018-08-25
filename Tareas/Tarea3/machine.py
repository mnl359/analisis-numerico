#!/bin/python3

class Machine:

    def __init__(self, mantissa, exponent):
        self.mantissa = mantissa
        self. exponent = exponent
        bits = 16

    def biggest(self):
        one = '1' * self.mantissa
        binary = '0b1' + one
        expo = "0b" + ("1"*self.exponent)
        decimal = "0." + str(int(binary,2)) + "e+" + str(int(expo,2))
        return decimal
        
    def lowest(self):
        exp = self.mantissa + 1 
        decimal = 2**(-exp)
        return decimal
        
    def positive(self):
        pass

    def epsilon(self):
        pass

    def machineNumber(self, number):
        if number[0] is "-":
            symbol = "0"
            number.pop(0)
        else:
            symbol = "1"
        if "," in number:
            number = number.split(",")
        else:
            binary = bin(int(number))
            length = bin(len(binary)-2)
            binary = binary[2:]
            length = length[2:]
            if len(length) < self.exponent:
                exp = self.exponent - len(length)
                length = ("0"*exp) + length
            if len(binary) < self.mantissa:
                man = self.mantissa - len(binary)
                binary = binary + ("0"*man)
            final = str(symbol)+"1"+str(binary)+str(length)
        return final

    def decimalNumber(self):
        pass
