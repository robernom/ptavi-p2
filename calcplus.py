#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    calc3 = calcoohija.CalculadoraHija()

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
                result = calc3.Selector(lista[0], result, int(elemento))
        except ValueError:
            """ If the parameters are not integers, it may be floats """
            try:
                result = float(lista[1])
                for elemento in lista[2:]:
                    result = calc3.Selector(lista[0], result, float(elemento))
            except ValueError:
                sys.exit('Error: Non numerical parameters')
        print(result)

        fich.close()
