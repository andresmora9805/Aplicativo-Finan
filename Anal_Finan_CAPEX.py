# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:44:11 2024

@author: ASUS
"""

"""Costos por MW"""

from Ejemplos import *
import math 


Valor_trackers=0
valor_Terreno=0
Equip_Gen_Total=0
BOS_Total=0
Valor_conexion=0
Total_Interconexion=0
Capex=0
C_InstaladaMW=valorCapacidad.get()
C_InstaladakW=C_InstaladaMW*1000
C_InstaladaDC=C_InstaladakW*1.2
Area_Proyecto=C_InstaladaMW*2
TasaDolar=3965
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
regaliasTotal=[]
costosFijos=[]
costosVariables=[]
gerenciayAdministracion=[]
arrTierra=[]
seguroList=[]
totalEgresos=[]
Periodo=1
valorArriendoTotal=valorArriendoHa.get()*Area_Proyecto
administracion=valorAdministracionOyM.get()

"""El costo de legalización por MW es de 50000 dolares"""

costoMWRTB=TasaDolar*50000
costoLegalizacion=costoMWRTB*C_InstaladaMW

"""Reservas y costo de financiamiento"""

ReservaCostoFinan=0
ReservaCostoFinan=valorTarifaPrestamista.get()*valorPorcenCostosDuros.get()

if var.get()=='Parcialmente plano':
    valor_Terreno=50000000
elif var.get()=='Con pendiente superior al 10%':
    valor_Terreno=65000000
elif var.get()=='Con vegetación':
    valor_Terreno=75000000
elif var.get()=='No es uniforme presenta protuberancias':
    valor_Terreno=100000000
else:
    valor_Terreno=50000000

if track.get()==1:
    Valor_trackers=850000000 
else:
    Valor_trackers=0

Equipos_Generacion={
    "Paneles_Solares":1401620000,
    "Inversores":69333333.3333333,
    }

BOS={
     "Cableado_DC":133333333.333333,
     "Cableado_AC_BT":150000000,
     "Sistema_Monitoreo":4666666.66666667,
     "Trackers": Valor_trackers,
     "Tuberias_conducciones": 116666666.666667,
     "Cerramiento":66666666.6666667,
     "SPT": 100000000,
     "Otros_materiales":166666666.666667,
     "Alquiler_maquinaria": 93333333.3333333,
     "Adecuacion_terrenos": valor_Terreno,
     "Instalación": 300000000,
     "Imprevistos": 133333333.333333,
     "Ingenieria_detalle": 60000000,
     "Estudio_suelos": 6666666.66666667,
     "Estudio_topograficos": 6666666.66666667,
     "Estudio_resistividad": 16666666.6666667,
     "Pruebas_campo": 5000000,
     "Campamento": 33333333.3333333,
     "SPDA": 60000000,
     }

#Costos_Linea_Conexión
Costos_LC={
    "Poste 12m-1050kg retencion": 7242621,
    "Poste 12m-510kg suspension":5509945,
    "ACSR 4 AWG": 18797225,
    "ACSR 2 AWG":21160588,
    "ACSR 1/0 AWG":22936110,
    "ACSR 2/0 AWG": 25388593,
    "ACSR 3/0 AWG": 28530033,
    "ACSR 4/0 AWG": 37373366,
    "ACSR 266 kcmil": 50239045,
    "ACSR 336 kcmil": 59884448,
    "ACSR 397 kcmil": 68948864,
    "ACSR 477 kcmil": 81187283,
    "ACSR 605 kcmil": 95211507,
    "ACSR 795 kcmil": 124576172,
    "Puesta a tierra": 462733
    }

#Costo total línea conexión
Metros=varLC.get()
MetrosAux=Metros.split('-')
MetrosAux2=MetrosAux[1]
MetrosAux3=MetrosAux2.replace('m','')
CantidadPostes=((int(MetrosAux3)/25)+1)
CantidadPostesSuspension=CantidadPostes*0.75
CantidadPostesSuspension=round(CantidadPostesSuspension,0)
CantidadPostesRetencion=-CantidadPostesSuspension+CantidadPostes
Valor_conexion=Costos_LC['Poste 12m-1050kg retencion']*CantidadPostesRetencion+Costos_LC['Poste 12m-510kg suspension']*CantidadPostesSuspension+(int(MetrosAux3)/1000)*Costos_LC[varCLC.get()]+(CantidadPostes/3)*Costos_LC['Puesta a tierra']

Interconexion={
    "Transformadores": 83333333.3333333,
    "Protecciones_MT": 31666666.6666667,
    "Medidores": 5000000,
    "Linea_Conexion": Valor_conexion,
    }

for clave in Equipos_Generacion:
    Equip_Gen_Total+=Equipos_Generacion[clave]
for clave in BOS:
    BOS_Total+=BOS[clave]
for clave in Interconexion:
    Total_Interconexion+=Interconexion[clave]
    
Equip_Gen_Total=Equip_Gen_Total*C_InstaladaDC/1000
BOS_Total=BOS_Total*C_InstaladaDC/1000
Total_Interconexion=Total_Interconexion*C_InstaladaDC/1000
Capex=Equip_Gen_Total+BOS_Total+Total_Interconexion+costoLegalizacion

"""Intereses durante la construcción"""

InteresConstruccion=Capex*(valorPeriodoFinanciacion.get()/12)*((valorTasaInteres.get()/100)/2)

"""Calculo de R y el pago del prestamo"""
porcenCostosDuros=valorPorcenCostosDuros.get()
plazoDeuda=valorPlazoDeuda.get()
interesDeuda=valorInteresDeuda.get()
tarifaPrestamista=valorTarifaPrestamista.get()
DCSRrequerido=valorDCSRminimo.get()
deudaAcapital=Capex*porcenCostosDuros/100
interesDeudaList=[]
capitalDeudaList=[]
exponente=math.pow((1+interesDeuda/100),-plazoDeuda)
Ani=(1-exponente)/(interesDeuda/100)
R=deudaAcapital/Ani
costoFinanAux=Capex
valorSeguro=Capex*valorSeguroOyM.get()/100


for j in range(0,25):
    if j<plazoDeuda:
        interesDeudaList.append(costoFinanAux*interesDeuda/100)
        capitalDeudaList.append(R-interesDeudaList[j])
        costoFinanAux=costoFinanAux-capitalDeudaList[j]
    else:
        interesDeudaList.append(0)
        capitalDeudaList.append(0)
        
        
        
"""Ingresos"""

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
        
        
"""Egresos"""

for i in range(0,25):
    if (valorRegalias.get()>0):
        regaliasTotal.append((ingresoVentaAutAG[i]+ingresoExcAG[i]+ingresoCeret[i])*valorRegalias.get()/100)
    else:
        regaliasTotal.append(0)
        if i<=(valorPeriodoInflacionOyM.get()-1):
            costosFijos.append((valorGastosOyM.get()*Periodo*C_InstaladaDC)-valorAporteCliente.get()*Periodo)
            costosVariables.append((valorGastosVarOyM.get()/100)*listaEnergia[i]*Periodo)
            gerenciayAdministracion.append(administracion*Periodo)
            arrTierra.append(valorArriendoTotal*Periodo)
            seguroList.append(valorSeguro*Periodo)
            totalEgresos.append(costosFijos[i]+costosVariables[i]+gerenciayAdministracion[i]+arrTierra[i]+seguroList[i]+regaliasTotal[i])
            Periodo=Periodo*(1+valorInflacionOyM.get()/100)
        else:
            if i>(valorPeriodoInflacionOyM.get()-1):
                costosFijos.append((valorGastosOyM.get()*Periodo*C_InstaladaDC)-valorAporteCliente.get()*Periodo)
                costosVariables.append((valorGastosVarOyM.get()/100)*listaEnergia[i]*Periodo)
                gerenciayAdministracion.append(administracion*Periodo)
                arrTierra.append(valorArriendoTotal*Periodo)
                seguroList.append(valorSeguro*Periodo)
                totalEgresos.append(costosFijos[i]+costosVariables[i]+gerenciayAdministracion[i]+arrTierra[i]+seguroList[i]+regaliasTotal[i])
                Periodo=Periodo*(1+valorInflacionOyM_dos.get()/100)



"""Debito inicial cuenta de reserva"""

nMesesCreserva=valorNumeroServicioDeuda.get()
cuotaInicialReserva=R*nMesesCreserva/12
nMesesCreservaExpense=valorNumeroDeMesesGastoOyM.get()
inicialOM=(totalEgresos[0]/12)*nMesesCreservaExpense
interesReserva=valorInteresCuentaReserva.get()

"""Reservas y costo de financiamiento"""
ReservaCostoFinan=0
ReservaCostoFinan=valorTarifaPrestamista.get()*valorPorcenCostosDuros.get()*(Equip_Gen_Total+BOS_Total+Total_Interconexion+costoLegalizacion)-InteresConstruccion-cuotaInicialReserva-inicialOM

"""Costo total instalado"""
CostoTotalInstalado=-1*ReservaCostoFinan+Capex
CTotalMW=CostoTotalInstalado/C_InstaladaDC/1000


"""De la ventana costos de capital"""

reemplazoEquipo=valorReemplazoEquipo.get() #Año
costoReemplazo=valorCostoReemplazoEquipo.get() #COP/Watt
reemplazoEquipoDos=valorReemplazoEquipo_dos.get()
costoReemplazoDos=valorCostoReemplazoEquipo_dos.get() 

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


print(DSCR)
print(ingresoExcAG)
print(ingresoCeret)



