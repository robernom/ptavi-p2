#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


def division(op1, op2):
    """ Function to divide the operands """
    try:
        return op1 / op2
    except ZeroDivisionError:
        sys.exit("Error: Division by zero is not allowed")


def multiplication(op1, op2):
    """ Function to multiply the operands """
    return op1 * op2


def Selector(operator, op1, op2):
    if operator == "suma":
        return plus(op1, op2)
    elif operator == "resta":
        return minus(op1, op2)
    elif operator == "divide":
        return division(op1, op2)
    elif operator == "multiplica":
        return multiplication(op1, op2)
    else:
        sys.exit('Commands are suma, resta, multiplica, divide')


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
    result = Selector(sys.argv[2], operando1, operando2)

    print(result)
