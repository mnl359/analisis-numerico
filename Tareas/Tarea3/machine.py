#!/bin/python3

class Machine:

    def __init__(self, mantissa, exponent):
        self.mantissa = mantissa
        self. exponent = exponent
        bits = 12

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
        positive = 2**((int('0b' + ('1'*self.exponent), 2)+1)*-1)
        return positive
      
    def epsilon(self):
        pass
    
    def machineNumber(self, number):
        if number[0] is "-":
            symbol = "0"
            number.pop(0)
        else:
            symbol = "1"
        if "." in number:
            number = number.split(".")
            whole = bin(int(number[0]))[2:]
            dec = float("0." + number[1])
            man_length = len(whole)-1
            bin_dec = ""
            while man_length < self.mantissa:
                temp = dec*2
                if str(temp)[0] is "1":
                    bin_dec += "1"
                else:
                    bin_dec += "0"
                man_length += 1
            if number[0] is not "0":
                exp = bin(len(whole))[2:]
                if len(exp) < self.exponent:
                    exp = ("0"*(self.exponent-len(exp))) + exp
                final = symbol + "1" + exp + whole + bin_dec
            else:
                pass
                    
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
                binary = binary[1:] + ("0"*man)
            # La manera de retornar es signo mantisa - signo exp - exponente - mantisa
            final = str(symbol)+"1"+str(length)+str(binary)
        return final

    def decimalNumber(self):
        pass
