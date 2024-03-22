# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:08:40 2024

@author: ASUS
"""

from Ejemplos import * 
#from Anal_Finan_GastosCapital import *



tarifaEnergiaLista=[]
tarifacostoPPAlista=[]
CERElista=[]
costoPPAAGlista=[]
C_InstaladaMW=valorCapacidad.get()
C_InstaladakW=C_InstaladaMW*1000
C_InstaladaDC=C_InstaladakW*1.2
vidaUtil=25
Area_Proyecto=C_InstaladaMW*2
Irradiancia=valorIrradiancia.get()
energiaPrimerAno=C_InstaladaDC*Irradiancia*365
autoconsumoUsuario=valorAutoconsumo.get()
demandaUsuarioSinAG=valorDemanda.get()
hIndisponibilidad=76.2
degradacionEnergia=1
listaEnergia=[]
listaEnergia.append(energiaPrimerAno)
ENFICC=valorENFICC.get()/100
ENFICCkW=0
ENFICCkWlista=[]
ENFICCkWlista.append(energiaPrimerAno*ENFICC)
perdidasIndis=[]
perdidasIndis.append(energiaPrimerAno*hIndisponibilidad/365/24)
TasaCTFE=1
tarifaEnergiaLista.append(valorTarifaEnergiaRed.get())
costoPPA=valorCostoEnergiaPPA.get()
costoPPAAG=valorCostoEnergiaPPAgen.get()
tarifacostoPPAlista.append(costoPPA)
CERE=valorCERE.get()
CERElista.append(CERE)
costoPPAAGlista.append(costoPPAAG)
ElectrPagadaUsuario=[]
ElectrPagadaUsuario.append(valorTarifaEnergiaRed.get()*demandaUsuarioSinAG)
ElectrPagadaUsuarioAG=[]
ElectrPagadaUsuarioAG.append(valorTarifaEnergiaRed.get()*autoconsumoUsuario)




for i in range(0,29):
    if i<=23:
        degradacionEnergia=degradacionEnergia*(1-0.005)
        #print("año "+str(i+2)+str(" ")+str(degradacionEnergia))
        listaEnergia.append(degradacionEnergia*energiaPrimerAno)
        ENFICCkWlista.append(degradacionEnergia*energiaPrimerAno*ENFICC)
        perdidasIndis.append(degradacionEnergia*energiaPrimerAno*hIndisponibilidad/365/24)
        #TasaCTFE=TasaCTFE*(1+(tariffRateEscalated*tariffEscalationRate))
        TasaCTFE=TasaCTFE*(1+((valorPorcentajeIncrementoTarifa.get()/100)*(valorTasaTarifaCostos.get()/100)))
        tarifaEnergiaLista.append(valorTarifaEnergiaRed.get()*TasaCTFE)
        tarifacostoPPAlista.append(costoPPA*TasaCTFE)
        CERElista.append(CERE*TasaCTFE)
        costoPPAAGlista.append(costoPPAAG*TasaCTFE)
        ElectrPagadaUsuario.append(valorTarifaEnergiaRed.get()*TasaCTFE*demandaUsuarioSinAG)
        ElectrPagadaUsuarioAG.append(valorTarifaEnergiaRed.get()*TasaCTFE*autoconsumoUsuario)
              
    else:
        listaEnergia.append(0)

"""Ingresos"""

#Ingreso por venta de energía autoconsumo. 
ingresoVentaAutAG=[]
ingresoVentaAutAG.append(costoPPAAG*autoconsumoUsuario)
#Ingreso por venta de excedentes a la red
ingresoExcAG=[]
ingresoExcAG.append(costoPPA*(energiaPrimerAno-energiaPrimerAno*hIndisponibilidad/365/24-autoconsumoUsuario))
#Ingreso por cargo de confiabilidad
ingresoCeret=[]
ingresoCeret.append(energiaPrimerAno*ENFICC*CERE)
#totalIngresos=[]
#totalIngresos.append(ingresoVentaAutAG[0]+ingresoExcAG[0]+ingresoCeret[0]+interesDeuda[0])
for j in range(1,len(tarifacostoPPAlista)):
    ingresoVentaAutAG.append(autoconsumoUsuario*costoPPAAGlista[j])
    ingresoExcAG.append((listaEnergia[j]-perdidasIndis[j]-autoconsumoUsuario)*tarifacostoPPAlista[j])
    ingresoCeret.append(ENFICCkWlista[j]*CERElista[j])
    



print(TasaCTFE)
print(tarifaEnergiaLista)
#print(len(tarifacostoPPAlista))
#print(len(ingresoCeret))
#print(CERElista)