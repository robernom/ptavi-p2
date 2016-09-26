#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def plus(self, op1, op2):
        return op1 + op2

    def minus(self, op1, op2):
        return op1 - op2

if __name__ == "__main__":

    calc = Calculadora()

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
        result = calc.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calc.minus(operando1, operando2)
    else:
        sys.exit('Commands are suma y resta')

    print(result)
