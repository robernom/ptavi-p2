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

    if sys.argv[2] == "suma":
        result = calc2.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calc2.minus(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = calc2.division(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calc2.multiplication(operando1, operando2)
    else:
        sys.exit('Commands are suma, resta, multiplica y divide')

    print(result)
