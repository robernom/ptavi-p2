#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    calcplus = calcoohija.CalculadoraHija()

    try:
        fich = open(sys.argv[1], 'r')
    except IndexError:
        sys.exit("Error: file not found")

    lineas = fich.readlines()

    for linea in lineas:
        lista = linea.split(',')
        try:
            result = int(lista[1])
            for elemento in lista[2:]:
                if lista[0] == "suma":
                    result = calcplus.plus(result, int(elemento))
                elif lista[0] == "resta":
                    result = calcplus.minus(result, int(elemento))
                elif lista[0] == "divide":
                    result = calcplus.division(result, int(elemento))
                elif lista[0] == "multiplica":
                    result = calcplus.multiplication(result, int(elemento))
                else:
                    sys.exit('Commands are suma, resta, multiplica y divide')
        except ValueError:
            try:
                result = float(lista[1])
                for elemento in lista[2:]:
                    if lista[0] == "suma":
                        result = calcplus.plus(result, float(elemento))
                    elif lista[0] == "resta":
                        result = calcplus.minus(result, float(elemento))
                    elif lista[0] == "divide":
                        result = calcplus.division(result, float(elemento))
                    elif lista[0] == "multiplica":
                        result = calcplus.multiplication(result, float(elemento))
                    else:
                        sys.exit('Commands are suma, resta, multiplica y divide')
            except ValueError:
                sys.exit('Error: Non numerical parameters')
        print(result)     


