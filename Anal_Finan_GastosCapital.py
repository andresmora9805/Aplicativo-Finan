# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:35:00 2024

@author: ASUS
"""
#from Anal_Finan_GD_DI import *
#from Anal_Finan_GD_CR import *
#from Anal_Finan_OM import *

reemplazoEquipo=10 #Año 
costoReemplazo=250 #COP/Watt
reemplazoEquipoDos=20
costoReemplazoDos=200 

Acelerada=costoReemplazo*C_InstaladaDC*1000
resReemplazoEquipos=[]
vidaUtil=0
balanceFinal=[]
reservaDeuda=[]
reservaDeuda.append(inicialOM+cuotaInicialReserva)
interesDeuda=[]
totalIngresos=[]
EBITDA=[]
EBITDAAcumulado=[]
EBITDAux=0
DSCR=[]
ingresosSinInteres=[]
ingresosAntesImpuestos=[]
reservaCapitalTrabajo=[]
reservaServicioDeuda=[]

for i in range(0,25):
    if i<reemplazoEquipo-1:
        resReemplazoEquipos.append((Acelerada)/((reemplazoEquipo-1)))
        balanceFinal.append(reservaDeuda[i]+resReemplazoEquipos[i])
        reservaDeuda.append(balanceFinal[i])
        interesDeuda.append(((balanceFinal[i]+reservaDeuda[i])/2)*(interesReserva/100))
        reservaCapitalTrabajo.append(0)
        reservaServicioDeuda.append(0)
        #print(i)
    elif i==reemplazoEquipo-1:
            resReemplazoEquipos.append(-Acelerada)
            balanceFinal.append(reservaDeuda[i]+resReemplazoEquipos[i])
            reservaDeuda.append(balanceFinal[i])
            interesDeuda.append(((balanceFinal[i]+reservaDeuda[i])/2)*(interesReserva/100))
            reservaCapitalTrabajo.append(0)
            reservaServicioDeuda.append(0)
            #print(i)
    elif i>reemplazoEquipo-1 and i<reemplazoEquipoDos-1:
        resReemplazoEquipos.append((vidaUtil)/(reemplazoEquipoDos-reemplazoEquipo-1))
        if i==vidaUtil-1:
            reservaCapitalTrabajo.append(inicialOM)
        else:
            reservaCapitalTrabajo.append(0)
        if i==plazoDeuda:
            reservaServicioDeuda.append(cuotaInicialReserva)
        else:
            reservaServicioDeuda.append(0)
        if i<plazoDeuda:
            balanceFinal.append(reservaDeuda[i]+resReemplazoEquipos[i])
        else:
            balanceFinal.append(0)
        reservaDeuda.append(balanceFinal[i])
        interesDeuda.append(((balanceFinal[i]+reservaDeuda[i])/2)*(interesReserva/100))
        #print(i)
    else:
        if i<24:
            reservaDeuda.append(0)
        resReemplazoEquipos.append(0)
        interesDeuda.append(0)
        reservaCapitalTrabajo.append(0)
        reservaServicioDeuda.append(0)
    totalIngresos.append(ingresoVentaAutAG[i]+ingresoExcAG[i]+ingresoCeret[i]+interesDeuda[i])
    EBITDA.append(totalIngresos[i]-totalEgresos[i])
    EBITDAux=EBITDAux+EBITDA[i]
    EBITDAAcumulado.append(EBITDAux)
    ingresosSinInteres.append(EBITDA[i]-interesDeudaList[i])
    ingresosAntesImpuestos.append(ingresosSinInteres[i]-capitalDeudaList[i]-resReemplazoEquipos[i]+reservaCapitalTrabajo[i]-reservaServicioDeuda[i])
    if i<plazoDeuda:
        DSCR.append((EBITDA[i]-resReemplazoEquipos[i])/R)
    else:
        DSCR.append("N/A")


#print(ingresosSinInteres)
print(ingresosAntesImpuestos)
print(ingresosSinInteres[15])
print(capitalDeudaList[15])
print(resReemplazoEquipos[15])
print(reservaServicioDeuda[15])
print(ingresosSinInteres[15]-capitalDeudaList[15]-resReemplazoEquipos[15]+reservaServicioDeuda[15])


#print(len(reservaCapitalTrabajo))
#print(len(ingresosSinInteres))
#print(len(capitalDeudaList))
#print(len(reservaServicioDeuda))

"""Flujo de caja antes de impuestos"""






