#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

calc4 = calcoohija.CalculadoraHija()

with open(sys.argv[1],'r') as fich: # Cuando acaba el with, se cierra fich
    lineas = csv.reader(fich)
    for lista in lineas:
        try:
            result = int(lista[1])
            for elemento in lista[2:]:
                result = calc4.Selector(lista[0],result,int(elemento))
        except ValueError:
            """ If the parameters are not integers, it may be floats """
            try:
                result = float(lista[1])
                for elemento in lista[2:]:
                    result = calc4.Selector(lista[0],result,float(elemento))
            except ValueError:
                sys.exit('Error: Non numerical parameters')
        print(result)