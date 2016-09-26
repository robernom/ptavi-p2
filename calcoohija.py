#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def division(self,op1,op2):
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")

    def multiplication(self,op1,op2):
        return op1 * op2

    def Selector(self, operator, op1, op2):
        if operator == "suma":
            return self.plus(op1, op2)
        elif operator == "resta":
            return self.minus(op1, op2)
        elif operator == "divide":
            return self.division(op1, op2)
        elif operator == "multiplica":
            return self.multiplication(op1, op2)
        else:
            sys.exit('Commands are suma, resta, multiplica, divide') 

if __name__ == "__main__":

    calc2 = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        try:
            operando1 = float(sys.argv[1])  # In this way, float are covered
            operando2 = float(sys.argv[3])
        except ValueError:
            sys.exit("Error: Non numerical parameters")

    result = calc2.Selector(sys.argv[2],operando1,operando2)

    print(result)
