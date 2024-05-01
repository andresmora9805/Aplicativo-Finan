# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:28:31 2024

@author: ASUS
"""

CapacidadCorriente={
        
        "ACSR 4 AWG": 140,
        "ACSR 2 AWG":185,
        "ACSR 1/0 AWG":240,
        "ACSR 2/0 AWG": 275,
        "ACSR 4/0 AWG": 360,
        "ACSR 266 kcmil": 450,
        "ACSR 336 kcmil": 520,
        
        }

Impedancia={
    
    "ACSR 4 AWG":[1.653,0.465], 
    "ACSR 2 AWG":[1.040,0.447],
    "ACSR 1/0 AWG":[0.654,0.430],
    "ACSR 2/0 AWG": [0.519,0.421],
    "ACSR 4/0 AWG": [0.327,0.404],
    "ACSR 266 kcmil": [0.263,0.377],
    "ACSR 336 kcmil": [0.209,0.368],
       
    }

cosTeta=0.95
senTeta=0.31

def regulacionTension(conductorElegido,I, distancia, tension):
    Z=Impedancia[conductorElegido][0]*cosTeta+Impedancia[conductorElegido][1]*senTeta
    Tension_fn=(distancia/1000)*Z*I
    Tension_ff=1.732*Tension_fn
    CaidaTension=((Tension_ff/1000)/tension)*100
    return CaidaTension


def calculoCalibre(capacidadPlanta,tension, distancia):
    I=(capacidadPlanta)/((1.732)*tension/1000)
    I=I*1.25
    conductorElegido=''
    for conductores in CapacidadCorriente:
        if CapacidadCorriente[conductores]>I:
            conductorElegido=conductores
            CaidaTension=regulacionTension(conductorElegido,I,distancia,tension)
            if CaidaTension<3:
                conductorElegido=conductores
                break
    return conductorElegido
    
        

   

print(calculoCalibre(4.99,34.5,6000))

