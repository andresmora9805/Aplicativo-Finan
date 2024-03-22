# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:09:37 2024

@author: ASUS
"""

"""Financiación"""

#from Anal_Finan_OM import *
from Ejemplos import *
import math


porcenCostosDuros=valorPorcenCostosDuros.get()
plazoDeuda=valorPlazoDeuda.get()
interesDeuda=valorInteresDeuda.get()
tarifaPrestamista=valorTarifaPrestamista.get()
DCSRrequerido=valorDCSRminimo.get()
costoExcluyendocostoFinanc=5128630570
deudaAcapital=costoExcluyendocostoFinanc*porcenCostosDuros/100
interesDeudaList=[]
capitalDeudaList=[]
exponente=math.pow((1+interesDeuda/100),-plazoDeuda)
Ani=(1-exponente)/(interesDeuda/100)
R=deudaAcapital/Ani

costoFinanAux=costoExcluyendocostoFinanc

for j in range(0,25):
    if j<plazoDeuda:
        interesDeudaList.append(costoFinanAux*interesDeuda/100)
        capitalDeudaList.append(R-interesDeudaList[j])
        costoFinanAux=costoFinanAux-capitalDeudaList[j]
    else:
        interesDeudaList.append(0)
        capitalDeudaList.append(0)


"""Cuentas de reserva"""






print(R)
print(len(capitalDeudaList))
print(tarifaPrestamista)
