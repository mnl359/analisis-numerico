#!/bin/python3

from numpy import negative
from sys import argv

class Machine:

    def __init__(self, mantissa, exponent):
        self.mantissa = mantissa
        self. exponent = exponent
        self.bits = 12

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
    
    def machine_number(self, number):
        if number[0] is "-":
            symbol = "0"
            number = number[1:]
        else:
            symbol = "1"
        if "." in number:
            number = number.split(".")
            ent = bin(int(number[0]))[2:]
            dec = int(number[1])
            bin_dec = ""
            man_length = 0
            temp = dec
            while man_length < (self.mantissa):
                if str(temp)[0] is "1":
                    bin_dec += "1"
                    dec = str(temp)
                    dec = float("0" + dec[1:])
                else:
                    bin_dec += "0"
                    dec = temp
                man_length += 1
                temp = dec * 2
            mantissa = ent + bin_dec
            exp = len(ent)
            while mantissa[0] == "0":
                mantissa = mantissa[1:]
                exp -= 1
            if negative(exp):
                symbol_exp = "0"
                exp = str(exp)[1:]
            else:
                symbol_exp="1"
            exp = (bin(int(exp)))[2:]

        else:
            mantissa = bin(int(number))[2:]
            exp = len(mantissa)
            while mantissa[0] == "0":
                mantissa = mantissa[1:]
                exp -= 1
            if negative(exp):
                symbol_exp = "0"
            else:
                symbol_exp="1"
            exp = bin(exp)[2:]
        if len(mantissa) <= self.mantissa:
            mantissa = mantissa[1:] + ("0" * (self.mantissa - (len(mantissa)-1)))
        if len(exp) <= self.exponent:
            exp = ("0" * (self.exponent - len(exp))) + exp
        print(exp)
        machine = symbol + symbol_exp + exp[:self.exponent] + mantissa[:self.mantissa]
        return machine

    def decimalNumber(self, number):
        j = 0
        while j < self.bits:
            if number[j] != "0" and number[j] != "1":
                print("Error")
                exit(-1)
                #break
            j+=1

        aux = self.exponent + 2
        expo = number[2:aux]
        mant = '1' + number[aux:]

        sigExp = ''
        sigMant = ''

        if number[1] == '0':
            sigExp = '-'
        else:
            sigExp = '+'

        if number[0] == '0':
            sigMant = '-'
        else:
            sigMant = '+'

        decExpo = int(expo, 2)

        if sigExp == '+':
            aux1 = decExpo - len(mant)

            if len(mant) <= decExpo:
                newMant = mant + ("0" * aux1)
                decMant = int(newMant, 2)
            else:
                newMant = int(mant[:decExpo], 2)

                decPart = mant[decExpo:]

                count = 0
                i = 0

                while i < len(decPart):
                    if decPart[i] == '1':
                        count += 2 **(-(i+1))
                    i += 1

                decMant = newMant + count

        else:
            newMant = str((0 * decExpo)) + mant

            decMant = '0,' + str(int(newMant, 2))
        return sigMant + str(decMant)


def main(argv):
    mantissa = 5
    exponent = 5
    machine = Machine(int(mantissa), int(exponent))
    print(machine.decimalNumber("000011001010"))
    print(machine.machine_number("544"))


if __name__ == '__main__':
    main(argv)

