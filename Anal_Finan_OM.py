# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:37:29 2024

@author: ASUS
"""

"""Operación y mantenimiento"""

#from Anal_Finan_GD_DI import *
#from Anal_Finan_CAPEX import * 


CAPEX=5212553801.73
ValorDolar=3965
GastosOyM=ValorDolar*5
GastosVarOyM=ValorDolar*3/100
inflacion=8
periodoInicial=10
inflacionDespues=4
seguro=0.3
valorSeguro=CAPEX*seguro/100
administracion=80000000
impuestoSobrePropiedad=2000000
ajusteImpuestoPropiedad=5
valorArriendoHa=5000000
valorArriendoTotal=valorArriendoHa*Area_Proyecto
costoTierra=0
costoTotalTierra=costoTierra*Area_Proyecto
participacionCliente=0
aporteCliente=0
regalias=0   #Porcentaje
regaliasTotal=[]
Periodo=1
costosFijos=[]
costosVariables=[]
gerenciayAdministracion=[]
arrTierra=[]
seguroList=[]
totalEgresos=[]

for i in range(0,25):
    if (regalias>0):
        regaliasTotal.append((ingresoVentaAutAG[i]+ingresoExcAG[i]+ingresoCeret[i])*regalias/100)
    else:
        regaliasTotal.append(0)
        if i<=(periodoInicial-1):
            costosFijos.append((GastosOyM*Periodo*C_InstaladaDC)-aporteCliente*Periodo)
            costosVariables.append((GastosVarOyM/100)*listaEnergia[i]*Periodo)
            gerenciayAdministracion.append(administracion*Periodo)
            arrTierra.append(valorArriendoTotal*Periodo)
            seguroList.append(valorSeguro*Periodo)
            totalEgresos.append(costosFijos[i]+costosVariables[i]+gerenciayAdministracion[i]+arrTierra[i]+seguroList[i]+regaliasTotal[i])
            Periodo=Periodo*(1+inflacion/100)
        else:
            if i>(periodoInicial-1):
                costosFijos.append((GastosOyM*Periodo*C_InstaladaDC)-aporteCliente*Periodo)
                costosVariables.append((GastosVarOyM/100)*listaEnergia[i]*Periodo)
                gerenciayAdministracion.append(administracion*Periodo)
                arrTierra.append(valorArriendoTotal*Periodo)
                seguroList.append(valorSeguro*Periodo)
                totalEgresos.append(costosFijos[i]+costosVariables[i]+gerenciayAdministracion[i]+arrTierra[i]+seguroList[i]+regaliasTotal[i])
                Periodo=Periodo*(1+inflacionDespues/100)
                




print(GastosOyM)


#print(totalEgresos)   
    

"""Egresos"""




