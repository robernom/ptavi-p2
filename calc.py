#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

def divide(op1, op2):
    """ Function to divide the operands """
    try:
        return op1 / op2
    except ZeroDivisionError:
        sys.exit("Error: Division by zero is not allowed")
        
def multiply(op1, op2):
    """ Function to multiply the operands """
    return op1 * op2        

if __name__ == "__main__":
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
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = divide(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = multiply(operando1, operando2)
    else:
        sys.exit('Commands are suma, resta, multiplica y divide')

    print(result)
