# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:09:37 2024

@author: ASUS
"""

"""Financiación"""

#from Anal_Finan_OM import *


def Funcion(numeroA, numeroB):
    calculo=numeroA-numeroB
    calculodos=numeroA+numeroB
    
    diccionario={
        "Clave": [calculo, calculodos]
        
        }
    
    return diccionario




hola=Funcion(2,5)

print(hola.values())