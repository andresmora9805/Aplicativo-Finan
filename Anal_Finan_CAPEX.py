# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:44:11 2024

@author: ASUS
"""

"""Costos por MW"""

from Ejemplos import *
import numpy_financial as npf
import math 
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl.styles import NamedStyle
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
import matplotlib.ticker as ticker


"""Una posible solución al problema es envíar los datos de entrada dentro de una función creada en este archivo"""

def format_y_ticks(value, pos):
    # Formatear el valor con separadores de miles
    return '{:,.0f}'.format(value)

def reporteExcel():
    book=Workbook()
    sheet = book.active
    sheet.title='Resumen Proyecto'
    sheet['A1'] = "Costo nivelado de energía" 
    sheet['A1'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A1'].font=Font(italic=True, bold=True)
    sheet.column_dimensions['A'].width=44
    sheet.column_dimensions['B'].width=12
    sheet.column_dimensions['C'].width=17
    sheet['B1'] = "$/kWh"
    sheet['B1'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B1'].font=Font(italic=True, bold=True)
    sheet['C1'] = LCOE
    sheet['C1'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A2'] = "Tipo de tecnología"
    sheet['A2'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A2'].font=Font(italic=True, bold=True)
    sheet['B2'] = "Fotovoltaica"
    sheet['B2'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B2'].font=Font(italic=True, bold=True)
    sheet["A3"] = "Capacidad del generador"
    sheet['A3'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A3'].font=Font(italic=True, bold=True)
    sheet["B3"] = "kWp"
    sheet['B3'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B3'].font=Font(italic=True, bold=True)
    sheet["C3"] = C_InstaladaDC
    sheet['C3'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A4"] = "Producción de energía"
    sheet['A4'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A4'].font=Font(italic=True, bold=True)
    sheet["B4"] = "kWh-año"
    sheet['B4'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B4'].font=Font(italic=True, bold=True)
    sheet["C4"] = energiaPrimerAno
    sheet['C4'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A5"] = "Vida útil proyecto"
    sheet['A5'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A5'].font=Font(italic=True, bold=True)
    sheet["B5"] = "años"
    sheet['B5'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B5'].font=Font(italic=True, bold=True)
    sheet["C5"] = 25
    sheet['C5'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A6"] = "Costo total instalación"
    sheet['A6'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A6'].font=Font(italic=True, bold=True)
    sheet["B6"] = "$/watt"
    sheet['B6'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B6'].font=Font(italic=True, bold=True)
    sheet['C6'].style=NamedStyle(name='contable', number_format='_-* #,##0.00_-;-* #,##0.00_-;_-* "-"??_-;_-@_-')
    sheet["C6"] = CostoTotalInstalado
    sheet['C6'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A7"] = "Gastos operativos"
    sheet['A7'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A7'].font=Font(italic=True, bold=True)
    sheet["B7"] ="$"
    sheet['B7'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B7'].font=Font(italic=True, bold=True)
    sheet['C7'].number_format='#,##0.00'
    sheet["C7"] = totalEgresos[0]
    sheet['C7'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A8"] = "Valor unitario de costos operacionales"
    sheet['A8'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A8'].font=Font(italic=True, bold=True)
    sheet["B8"] = "$/kWh"
    sheet['B8'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B8'].font=Font(italic=True, bold=True)
    sheet['C8'].number_format='#,##0.00'
    sheet["C8"] = valorUnitario
    sheet['C8'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A9"] = "Total Ingresos"
    sheet['A9'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A9'].font=Font(italic=True, bold=True)
    sheet["B9"] = "$"
    sheet['B9'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B9'].font=Font(italic=True, bold=True)
    sheet['C9'].number_format='#,##0.00'
    sheet["C9"] = totalIngresos[0]
    sheet['C9'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A10"] = "Porcentaje de costos duros"
    sheet['A10'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A10'].font=Font(italic=True, bold=True)
    sheet["B10"] = "%"
    sheet['B10'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B10'].font=Font(italic=True, bold=True)
    sheet["C10"] = 100-valorPorcenCostosDuros.get()
    sheet['C10'].alignment=Alignment(horizontal='center', vertical='center')
    sheet["A11"] = "Inversión de capital"
    sheet['A11'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A11'].font=Font(italic=True, bold=True)
    sheet["B11"] = "$"
    sheet['B11'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B11'].font=Font(italic=True, bold=True)
    sheet['C11'].number_format='#,##0.00'
    sheet["C11"] = Inversion
    sheet['C11'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A12'] = "Tir después de impuestos"
    sheet['A12'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A12'].font=Font(italic=True, bold=True)
    sheet['B12'] = "%"
    sheet['B12'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B12'].font=Font(italic=True, bold=True)
    sheet['C12'] = valorEquityTIR.get()
    sheet['C12'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A13'] = "% de los costos duros financiados mediante deuda"
    sheet['A13'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A13'].font=Font(italic=True, bold=True)
    sheet['B13'] = "%"
    sheet['B13'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B13'].font=Font(italic=True, bold=True)
    sheet['C13'] = valorPorcenCostosDuros.get()
    sheet['C13'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A14'] = "Plazo de la deuda"
    sheet['A14'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A14'].font=Font(italic=True, bold=True)
    sheet['B14'] = "Años"
    sheet['B14'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B14'].font=Font(italic=True, bold=True)
    sheet['C14'] = plazoDeuda
    sheet['C14'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A15'] ="Es el propietario sujeto a impuestos"
    sheet['A15'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A15'].font=Font(italic=True, bold=True)
    sheet['C15'].alignment=Alignment(horizontal='center', vertical='center')
    if impuestos.get()==0:
        sheet['C15']= "Sí"
    else:
        sheet['C15']='No'
    sheet['A16'] = "TIR antes de impuestos"
    sheet['A16'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A16'].font=Font(italic=True, bold=True)
    sheet['B16'] = "%"
    sheet['B16'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B16'].font=Font(italic=True, bold=True)
    sheet['C16'] = TIR*100
    sheet['C16'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A17'] = "TIR después de impuestos"
    sheet['A17'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A17'].font=Font(italic=True, bold=True)
    sheet['B17'] = "%"
    sheet['B17'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B17'].font=Font(italic=True, bold=True)
    sheet['C17'] = TIR_dos*100
    sheet['C17'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A18'] ="Valor presente neto de los costos"
    sheet['A18'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A18'].font=Font(italic=True, bold=True)
    sheet['B18'] = "$"
    sheet['B18'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B18'].font=Font(italic=True, bold=True)
    sheet['C18'].number_format='#,##0.00'
    sheet['C18'] = VAN_dosAux
    sheet['C18'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A19'] = "Valor presente neto del capital final"
    sheet['A19'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A19'].font=Font(italic=True, bold=True)
    sheet['B19'] = "$"
    sheet['B19'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B19'].font=Font(italic=True, bold=True)
    sheet['C19'].number_format='#,##0.00'
    sheet['C19'] = VAN
    sheet['C19'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A20'] = "Se cumple el DCSR mínimo requerido"
    sheet['A20'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A20'].font=Font(italic=True, bold=True)
    sheet['C20'].alignment=Alignment(horizontal='center', vertical='center')
    if DSCR[0]>DCSRrequerido:
        sheet['C20']="Sí"
    else:
        sheet['C20']='No'
    sheet['A21']="Se cumple el DCSR promedio requerido"
    sheet['A21'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A21'].font=Font(italic=True, bold=True)
    sheet['C21'].alignment=Alignment(horizontal='center', vertical='center')
    if (sum(DSCR[0:15])/len(DSCR))>valorDCSRpromedio.get():
        sheet['C21']='Sí'
    else:
        sheet['C21']='No'
        
    sheet['A22']="Período de recuperación de la inversión"
    sheet['A22'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A22'].font=Font(italic=True, bold=True)
    sheet['B22']="Años"
    sheet['B22'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['B22'].font=Font(italic=True, bold=True)
    
    sheet['A23']="Relación beneficio costo"
    sheet['A23'].alignment=Alignment(horizontal='center', vertical='center')
    sheet['A23'].font=Font(italic=True, bold=True)
    sheet['C23']=BC
    sheet['C23'].alignment=Alignment(horizontal='center', vertical='center')
           
    
    segundaHoja=book.create_sheet(title="Flujo de caja anual")
    segundaHoja.column_dimensions['A'].width=17
    segundaHoja['A1']="Año del proyecto"
    segundaHoja['A1'].font=Font(italic=True,bold=True)
    segundaHoja['A1'].alignment=Alignment(horizontal='center', vertical='center')
    tiempo=[]
    GraficaLista_dos=[]
    GraficaLista_dos.append(0)
    
    for i in range(2,28):
        segundaHoja['A'+str(i)]=i-2
        segundaHoja['A'+str(i)].alignment=Alignment(horizontal='center',vertical='center')
        tiempo.append(i-2)
        if i<27:
           GraficaLista_dos.append(totalIngresos[i-2]-impuestoBaseGravable[i-2])
    
    segundaHoja.column_dimensions['B'].width=33
    segundaHoja['B1']="Tarifa Energía Vendida PPA COP/kWh"
    segundaHoja['B1'].font=Font(italic=True,bold=True)
    segundaHoja['B1'].alignment=Alignment(horizontal='center', vertical='center')
    
    segundaHoja.column_dimensions['C'].width=20
    segundaHoja['C1']="Ingresos por ventas $"
    segundaHoja['C1'].font=Font(italic=True,bold=True)
    segundaHoja['C1'].alignment=Alignment(horizontal='center', vertical='center')
    
    segundaHoja.column_dimensions['D'].width=20
    segundaHoja['D1']="Costos operativos $"
    segundaHoja['D1'].font=Font(italic=True,bold=True)
    segundaHoja['D1'].alignment=Alignment(horizontal='center', vertical='center')
    
    segundaHoja.column_dimensions['E'].width=33
    segundaHoja['E1']="Flujo de caja después de impuestos $"
    segundaHoja['E1'].font=Font(italic=True,bold=True)
    segundaHoja['E1'].alignment=Alignment(horizontal='center', vertical='center')
    
    segundaHoja.column_dimensions['F'].width=25
    segundaHoja['F1']="Flujo de caja acumulado $"
    segundaHoja['F1'].font=Font(italic=True,bold=True)
    segundaHoja['F1'].alignment=Alignment(horizontal='center', vertical='center')
    segundaHoja['F2'].alignment=Alignment(horizontal='center', vertical='center')
    segundaHoja['F2']=-Inversion
    segundaHoja['F2'].number_format='#,##0.00'
    AuxFilaF=-Inversion
    
    segundaHoja.column_dimensions['G'].width=25
    segundaHoja['G1']="Flujo de caja del interés $"
    segundaHoja['G1'].font=Font(italic=True,bold=True)
    segundaHoja['G1'].alignment=Alignment(horizontal='center', vertical='center')
    segundaHoja['G2'].alignment=Alignment(horizontal='center', vertical='center')
    AuxFilaG=0
    GraficaLista=[]
    GraficaLista.append(-Inversion)
    
    
    segundaHoja.column_dimensions['H'].width=25
    segundaHoja['H1']="Cobertura de servicio de la deuda"
    segundaHoja['H1'].font=Font(italic=True,bold=True)
    segundaHoja['H1'].alignment=Alignment(horizontal='center', vertical='center')
    
    for j in range(0,7):
        for i in range(2,27):
            if j==0:
               segundaHoja['B'+str(i+1)]=tarifacostoPPAlista[i-2]
               segundaHoja['B'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
            elif j==1:
                segundaHoja['C'+str(i+1)]=totalIngresos[i-2]
                segundaHoja['C'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                segundaHoja['C'+str(i+1)].number_format='#,##0.00'
            elif j==2:
                segundaHoja['D'+str(i+1)]=totalEgresos[i-2]
                segundaHoja['D'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                segundaHoja['D'+str(i+1)].number_format='#,##0.00'
            elif j==3:
                segundaHoja['E'+str(i+1)]=ingresosDespuesImpuestos[i-2]
                segundaHoja['E'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                segundaHoja['E'+str(i+1)].number_format='#,##0.00'
            elif j==4:
                AuxFilaF+=ingresosDespuesImpuestos[i-2]
                if AuxFilaF>0:
                    segundaHoja['F'+str(i+1)]=AuxFilaF
                    segundaHoja['F'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                    segundaHoja['F'+str(i+1)].number_format='#,##0.00'
                    GraficaLista.append(AuxFilaF)
                else:
                    sheet['C22']=i
                    sheet['C22'].alignment=Alignment(horizontal='center', vertical='center')
                    segundaHoja['F'+str(i+1)]=AuxFilaF
                    segundaHoja['F'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                    segundaHoja['F'+str(i+1)].number_format='#,##0.00'
                    segundaHoja['F'+str(i+1)].font=Font(color='FF0000')
                    GraficaLista.append(AuxFilaF)
            elif j==5:
                AuxFilaG+=interesDeudaList[i-2]
                segundaHoja['G'+str(i+1)]=AuxFilaG
                segundaHoja['G'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
                segundaHoja['G'+str(i+1)].number_format='#,##0.00'
            elif j==6:
                segundaHoja['H'+str(i+1)]=DSCR[i-2]
                segundaHoja['H'+str(i+1)].alignment=Alignment(horizontal='center',vertical='center')
            
    
    tercerHoja=book.create_sheet(title="Graficos")
    
    fig, axs=plt.subplots(2, figsize=(12,6))
    axs[0].plot(tiempo,GraficaLista)
    #axs[0].set_xlabel("Años del proyecto")
    axs[0].set_ylabel("Flujo de caja acumulado")
    axs[0].set_title("Flujo de caja acumulado")
    axs[0].yaxis.set_major_formatter(ticker.FuncFormatter(format_y_ticks))
    axs[0].axhline(0, color='black', linestyle='--')
    axs[1].plot(tiempo,GraficaLista_dos)
    axs[1].set_xlabel("Años del proyecto")
    axs[1].set_ylabel("$")
    axs[1].set_title("Ingreso más beneficio en impuesto")
    axs[1].yaxis.set_major_formatter(ticker.FuncFormatter(format_y_ticks))
    axs[1].axhline(0, color='black', linestyle='--')
    fig.savefig('Grafico_1.png')
    #fig.savefig('Grafico_2.png')
    img_uno=Image('Grafico_1.png')
    #img_dos=Image('Grafico_2.png')
        
    tercerHoja.add_image(img_uno,'B1')
    #tercerHoja.add_image(img_dos,'F1')
    #print(GraficaLista_dos)
    book.save('Reporte Excel.xlsx')
    
    

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
depreciacionlnAcumulada=[]
depreciacionVal=[]
depreciacionAcAcumulada=[]
valorLibro=[]
montoDepreciar=[]
depreciacionAux2=0
depreciacionAux=0
RentaLiquida=[]
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
costoFinanAux=deudaAcapital
valorSeguro=Capex*valorSeguroOyM.get()/100
AuxiliarLCOE=0

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
        AuxiliarLCOE+=listaEnergia[i]   
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
Inversion=CostoTotalInstalado-deudaAcapital
TIRAux=[]
TIRAux.append(-Inversion)
depreciacionAceleradaAux=CostoTotalInstalado
TIRAux_dos=[]

"""De la ventana costos de capital"""

reemplazoEquipo=valorReemplazoEquipo.get() #Año
costoReemplazo=valorCostoReemplazoEquipo.get() #COP/Watt
reemplazoEquipoDos=valorReemplazoEquipo_dos.get()
costoReemplazoDos=valorCostoReemplazoEquipo_dos.get() 

Acelerada=costoReemplazo*C_InstaladaDC*1000
resReemplazoEquipos=[]
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
deduccionBaseGravable=[]
acumuladoRenta=[]
acumuladoRentaAux=0
impuestoBaseGravable=[]
impuestoRentaAcumulado=[]
impuestoRentaAux=0
ingresosDespuesImpuestos=[]
TIRAux_dos.append(-Inversion)
ajustePorReemplazo=[]
VAN_dos=[]
VAN_dos.append(-CostoTotalInstalado)

for i in range(0,25):
    if i<reemplazoEquipo-1:
        resReemplazoEquipos.append((Acelerada)/((reemplazoEquipo-1)))
        balanceFinal.append(reservaDeuda[i]+resReemplazoEquipos[i])
        reservaDeuda.append(balanceFinal[i])
        interesDeuda.append(((balanceFinal[i]+reservaDeuda[i])/2)*(interesReserva/100))
        reservaCapitalTrabajo.append(0)
        reservaServicioDeuda.append(0)
        ajustePorReemplazo.append(0)
        #print(i)
    elif i==reemplazoEquipo-1:
            resReemplazoEquipos.append(-Acelerada)
            balanceFinal.append(reservaDeuda[i]+resReemplazoEquipos[i])
            reservaDeuda.append(balanceFinal[i])
            interesDeuda.append(((balanceFinal[i]+reservaDeuda[i])/2)*(interesReserva/100))
            reservaCapitalTrabajo.append(0)
            reservaServicioDeuda.append(0)
            ajustePorReemplazo.append(Acelerada)
            #print(i)
    elif i>reemplazoEquipo-1 and i<reemplazoEquipoDos-1:
        resReemplazoEquipos.append((vidaUtil)/(reemplazoEquipoDos-reemplazoEquipo-1))
        ajustePorReemplazo.append(0)
        if i==vidaUtil-1:
            reservaCapitalTrabajo.append(inicialOM)
            #print('no estoy entrando acá')
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
        #reservaCapitalTrabajo.append(0)
        reservaServicioDeuda.append(0)
        ajustePorReemplazo.append(0)
        if i==vidaUtil-1:
            reservaCapitalTrabajo.append(inicialOM)
        else:
            reservaCapitalTrabajo.append(0)
    totalIngresos.append(ingresoVentaAutAG[i]+ingresoExcAG[i]+ingresoCeret[i]+interesDeuda[i])
    EBITDA.append(totalIngresos[i]-totalEgresos[i])
    EBITDAux=EBITDAux+EBITDA[i]
    EBITDAAcumulado.append(EBITDAux)
    ingresosSinInteres.append(EBITDA[i]-interesDeudaList[i])
    ingresosAntesImpuestos.append(ingresosSinInteres[i]-capitalDeudaList[i]-resReemplazoEquipos[i]+reservaCapitalTrabajo[i]+reservaServicioDeuda[i]-ajustePorReemplazo[i])
    #print(len(reservaCapitalTrabajo[i]))
    TIRAux.append(ingresosAntesImpuestos[i])
    if i<plazoDeuda:
        DSCR.append((EBITDA[i]-resReemplazoEquipos[i])/R)
    else:
        DSCR.append("N/A")
    if depreciacion.get()==0:
        """Depreciacion Lineal"""
        depreciacionAux=CostoTotalInstalado*valorTasaDepreciacionLn.get()/100
        ValorDeRescate=0.1*CostoTotalInstalado
        if i<=valorTiempoDepreciacionLn.get()-1:
            depreciacionVal.append(depreciacionAux)
            depreciacionAux2+=depreciacionAux
            depreciacionlnAcumulada.append(depreciacionAux2)
            valorLibro.append(CostoTotalInstalado+ValorDeRescate-depreciacionlnAcumulada[i])
        else:
            depreciacionVal.append(0)
            depreciacionlnAcumulada.append(0)
    elif depreciacion.get()==1:
        """Depreciacion acelerada"""
        if i<=9:
            montoDepreciar.append(depreciacionAceleradaAux)
            depreciacionVal.append(depreciacionAceleradaAux*valorTasaDepreciacionAc.get()/100)
            depreciacionAcAcumulada.append(depreciacionAc[i])
            valorLibro.append(montoDepreciar[i]-depreciacionVal[i])
            depreciacionAceleradaAux=valorLibro[i]
            
        else:
            montoDepreciar.append(0)
            depreciacionVal.append(0)
            depreciacionAcAcumulada.append(0)
            valorLibro.append(0)
    if impuestos.get()==0:
        """El cliente declara renta"""
        if i==0:
            deduccionBaseGravable.append(0)
            acumuladoRenta.append(0)
            RentaLiquida.append(ingresosSinInteres[i]-depreciacionVal[i])
        else:
            if (acumuladoRenta[i-1]+RentaLiquida[i-1]*valorBaseGravable.get()/100)<(CostoTotalInstalado*valorMaxDesCapex.get()/100):
                deduccionBaseGravable.append(RentaLiquida[i-1]*valorBaseGravable.get()/100)
                #print("Estoy en el primer if")
            else:
                if CostoTotalInstalado*valorMaxDesCapex.get()/100-acumuladoRenta[i-1]<=0:
                    deduccionBaseGravable.append(0)
                else:
                    deduccionBaseGravable.append(CostoTotalInstalado*valorMaxDesCapex.get()/100-acumuladoRenta[i-1])
                    #print("Estoy en el tercer else")
            acumuladoRentaAux=acumuladoRenta[i-1]
            acumuladoRenta.append(deduccionBaseGravable[i]+acumuladoRentaAux)
            RentaLiquida.append(ingresosSinInteres[i]-depreciacionVal[i]-deduccionBaseGravable[i])
        impuestoBaseGravable.append((RentaLiquida[i]-deduccionBaseGravable[i])*valorImpuestoRenta.get()/100)
        impuestoRentaAux+=impuestoBaseGravable[i]
        impuestoRentaAcumulado.append(impuestoRentaAux)
    elif impuestos.get()==1:
        """El cliente no declara renta"""
        RentaLiquida.append(0)
    ingresosDespuesImpuestos.append(ingresosAntesImpuestos[i]-impuestoBaseGravable[i])
    TIRAux_dos.append(ingresosDespuesImpuestos[i])
    VAN_dos.append(-totalEgresos[i])
        
VANIngresos=npf.npv(valorEquityTIR.get()/100,ingresosAntesImpuestos)
AuxEgresosTotales=[]
VANEgresos=npf.npv(valorEquityTIR.get()/100,totalEgresos)
BC=VANIngresos/(VANEgresos+Inversion)
TIR=npf.irr(TIRAux)
TIR_dos=npf.irr(TIRAux_dos)
VAN=npf.npv(valorEquityTIR.get()/100,TIRAux_dos)
VAN_dosAux=npf.npv(valorEquityTIR.get()/100,VAN_dos)
valorUnitario=totalEgresos[0]/listaEnergia[0]
LCOE=-VAN_dosAux/sum(listaEnergia)


if contador>=1:
    reporteExcel()