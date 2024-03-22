# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:15:04 2024

@author: ASUS
"""
import tkinter as tk
from PIL import Image, ImageTk  #Librería para usar imagenes en la ventanas
from tkinter import messagebox #Librería para mensajes de advertencia

"""Funciones"""

"""Función para mostrar ventana"""
def mostrarVentana(ventana):
    ventana.deiconify()
"""Función para ocultar ventana"""
def ocultarVentana(ventana):
    ventana.withdraw()

"""Función para mostrar ventana 1"""
def mostrarVentanaUno():
    mostrarVentana(ventana)
    ocultarVentana(ventanaDI)
    
"""Función para mostrar ventana 2"""
def mostrarVentanaDos():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventana)

"""Función para mostrar ventana OyM"""
def mostrarVentanaTres():
    mostrarVentana(ventanaOyM)
    ocultarVentana(ventanaDI)
    
"""Función para mostrar ventana DI desde OyM"""
def mostrarVentanaDI():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaOyM)    
    
def mostrarVentanaDI_Finan():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaFinan)
    
"""Función para mostrar ventana Financiación"""    
def mostrarVentanaFinan():
    mostrarVentana(ventanaFinan)
    ocultarVentana(ventanaDI)
    
"""Función para mostrar ventana de Impuestos"""    
def mostrarVentanaImpuestos():
    mostrarVentana(ventanaImpuestos)
    ocultarVentana(ventanaDI)

"""Función para mostrar ventana DI desde impuestos"""
def mostrarVentanaDI_Impuestos():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaImpuestos)
    
"""Función para mostrar ventana de Datos energéticos"""
def mostrarVentanaEnergetica():
    mostrarVentana(ventanaEnergetica)
    ocultarVentana(ventanaDI)

"""Función para mostrar ventana DI desde Energetica"""
def mostrarVentanaDI_Energetica():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaEnergetica)

"""Función para salir"""
def salir():
    ventana.destroy()


"""Características ventana principal"""
ventana = tk.Tk()
ventana.title("Análisis financiero Proyectos De Energías Renovables")
ventana.geometry('1000x700')
ventana.configure(background='#004292')
fuente_personalizada=('Consolas',16,'bold')

"""Etiqueta superior ventana principal"""
etiquetaInicial=tk.Label(ventana, text='Bienvenido al programa de análisis financiero \npara energias renovables creado por We power S.A.S',
                         font=fuente_personalizada, justify='center', anchor='center')
#etiquetaInicial.grid(row=0,column=0,padx=10,pady=10)
#etiquetaInicial.pack(side='top',padx=20,pady=20)
etiquetaInicial.place(x=100,y=20, width=800, height=70)

"""Etiqueta media ventana principal"""
etiquetaMedia=tk.Label(ventana,text='¿Qué desea hacer?',font=('Consolas',12), justify='center',anchor='center')
#etiquetaMedia.pack()
#etiquetaMedia.grid(row=1,column=0, padx=5, pady=5)
etiquetaMedia.place(x=400,y=100)

"""Boton de continuar ventana principal"""

botonContinuar=tk.Button(ventana,text='Continuar',font=('Consolas',12),command=mostrarVentanaDos)
#botonContinuar.grid(row=2,column=1,padx=10, pady=10)
botonContinuar.place(x=430,y=150)

"""Botón para salir"""
botonSalir=tk.Button(ventana,text='Salir del programa',font=('Consolas',12),command=salir)
#botonSalir.grid(row=3,column=1,padx=10, pady=10)
botonSalir.place(x=395,y=200)

"""Etiqueta pie de pagina ventana principal"""
etiquetaPie=tk.Label(ventana, text='contacto\n colombia@wepower.com.co \n +57 (301)7877074',font=('Consolas',12), justify='center')
etiquetaPie.place(x=375,y=630)

"""Características ventana Datos iniciales"""
ventanaDI=tk.Toplevel()
ventanaDI.title("Análisis financiero proyectos Energía Renovable")
ventanaDI.geometry('1000x700')
ventanaDI.configure(background='#004292')

"""Etiqueta superior ventana Datos iniciales"""
titulo=tk.Label(ventanaDI, text='Ingrese los datos iniciales de su proyecto', font=('Consolas',13), justify='center')
titulo.place(x=320,y=1)

"""Boton para volver a la página principal ventana DI"""
botonRegresar=tk.Button(ventanaDI,text='Regresar \n ventana principal', font=('Consolas',10), justify='center', command=mostrarVentanaUno,
                        width=20)
botonRegresar.place(x=5,y=650)

"""Boton para salir del programa en ventana DI"""
botonSalir=tk.Button(ventanaDI,text='Salir del programa',font=('Consolas',10),command=salir)
#botonSalir.grid(row=3,column=1,padx=10, pady=10)
botonSalir.place(x=845,y=660)

"""Datos iniciales capex en ventana DI"""
#Entrada capacidad del sistema
Capacidad=tk.Label(ventanaDI, text='¿Cuál es la capacidad instalada del sistema de generación? (MW)', font=('Consolas',10), justify='left')
Capacidad.place(x=5,y=35,height=18)
valorCapacidad=tk.IntVar(value=1)
entradaPotencia=tk.Entry(ventanaDI, textvariable=valorCapacidad)
entradaPotencia.place(x=460,y=35, height=18)

#Entrada irradiancia del lugar 
irradiancia=tk.Label(ventanaDI, text='Digite la irradiancia en el lugar (kW/m2)', font=('Consolas',10), justify='left')
irradiancia.place(x=5, y=57, height=18)
valorIrradiancia=tk.DoubleVar(value=5.5)
entradaIrradiancia=tk.Entry(ventanaDI, textvariable=valorIrradiancia)
entradaIrradiancia.place(x=460, y=57, height=18)

#AutoconsumoUsuario
autoconsumo=tk.Label(ventanaDI, text='Digite el autoconsumo del usuario (kWh-año)', font=('Consolas',10), justify='left')
autoconsumo.place(x=5, y=79,height=18)
valorAutoconsumo=tk.DoubleVar(value=80000)
entradaAutoconsumo=tk.Entry(ventanaDI, textvariable=valorAutoconsumo)
entradaAutoconsumo.place(x=460, y=79,height=18)

#DemandaUsuario
demanda=tk.Label(ventanaDI, text='Digite la demanda del cliente (kWh-año)', font=('Consolas',10), justify='left')
demanda.place(x=5, y=101, height=18)
valorDemanda=tk.DoubleVar(value=80000)
entradaDemanda=tk.Entry(ventanaDI, textvariable=valorDemanda)
entradaDemanda.place(x=460, y=101, height=18)

#Selección del tipo de terreno
terreno=tk.Label(ventanaDI,text='Seleccione el tipo de terreno del cliente', font=('Consolas',10),justify='left')
terreno.place(x=5,y=123,height=18)
var=tk.StringVar(ventanaDI) #Variable que guarda la opción var.get()
opciones=['Parcialmente plano',
          'Con pendiente superior al 10%',
          'Con vegetación',
          'No es uniforme presenta protuberancias']

opcion=tk.OptionMenu(ventanaDI,var,*opciones)
opcion.place(x=460,y=123, height=20)

#Selección distancia del predio al punto de conexión
distanciaLC=tk.Label(ventanaDI,text='Seleccione la distancia del predio al punto de conexión', font=('Consolas',10),justify='left')
distanciaLC.place(x=5,y=145,height=18)
varLC=tk.StringVar(ventanaDI) #Variable que guarda la opción var.get()
opcionesLC=['0-50m','51m-100m','101m-150m','151m-200m','201m-250m','251m-300m','301m-350m','351m-400m','401m-450m','451m-500m',
            '501m-600m','601m-700m','701m-800m','801m-900m','901m-1000m','1000m-2000m','2000m-3000m','3000m-4000m','4000m-5000m']
opcionLC=tk.OptionMenu(ventanaDI,varLC,*opcionesLC)
opcionLC.place(x=460,y=145,height=20)

#Seleccion el calibre de la línea a ser usado
calibreLC=tk.Label(ventanaDI,text='Seleccione el calibre de la línea de conexión', font=('Consolas',10),justify='left')
calibreLC.place(x=5,y=167,height=18)
varCLC=tk.StringVar(ventanaDI) #Variable que guarda la opción var.get()
opcionesCLC=['ACSR 4 AWG','ACSR 2 AWG','ACSR 1/0 AWG','ACSR 2/0 AWG','ACSR 3/0 AWG','ACSR 4/0 AWG','ACSR 266 kcmil','ACSR 336 kcmil','ACSR 397 kcmil','ACSR 477 kcmil',
            'ACSR 650 kcmil','ACSR 795 kcmil']
opcionCLC=tk.OptionMenu(ventanaDI,varCLC,*opcionesCLC)
opcionCLC.place(x=460,y=167,height=20)

#Seleccion de trackers
trackers=tk.Label(ventanaDI,text='¿Va a usar trackers?', font=('Consolas',10),justify='left')
trackers.place(x=5,y=189,height=18)
track=tk.IntVar() #Guarda la respuesta
opcion_1=tk.Radiobutton(ventanaDI,text='Sí',font=('Consolas',10),value=1,variable=track)
opcion_1.place(x=460,y=189,height=18)
opcion_2=tk.Radiobutton(ventanaDI,text='No',font=('Consolas',10),value=0,variable=track)
opcion_2.place(x=510,y=189,height=18)

#ENFICC
ENFICC=tk.Label(ventanaDI, text='Digite el porcentaje de ENFICC (%)', font=('Consolas',10), justify='left')
ENFICC.place(x=5, y=213, height=18)
valorENFICC=tk.DoubleVar(value=15)
entradaValorENFICC=tk.Entry(ventanaDI, textvariable=valorENFICC)
entradaValorENFICC.place(x=460, y=213, height=18)


#Label de ir a ventana OyM
subtitulo=tk.Label(ventanaDI, text='Desea modificar variables asociadas a la entrada de costos de operación y mantenimiento', font=('Consolas',11), justify='center', bg='light blue')
subtitulo.place(x=5,y=241)

#Botón para ir a ventana de costos de operación y mantenimiento
botonIrVentanaOyM=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaTres, width=8)
botonIrVentanaOyM.place(x=720,y=241)

#Label de ir a ventana de financiación de la deuda
subtituloFinan=tk.Label(ventanaDI, text='Desea modificar variables asociadas a la financiación del proyecto (deuda, construcción)', font=('Consolas',11), justify='center', bg='light blue')
subtituloFinan.place(x=5,y=269)
#Botón de ir a ventana de financiación de la deuda
botonIrVentanaFinan=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaFinan, width=8)
botonIrVentanaFinan.place(x=720,y=269)

#Label de ir a ventana de impuestos
subtituloImpuestos=tk.Label(ventanaDI, text='Desea modificar variables asociadas a los impuestos (declaración de renta)', font=('Consolas',11), justify='center', bg='light blue')
subtituloImpuestos.place(x=5,y=297)
#Botón de ir a ventana de impuestos
botonIrVentanaFinan=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaImpuestos, width=8)
botonIrVentanaFinan.place(x=720,y=297) 

#Label de ir a ventana energética
subtituloEnergeticos=tk.Label(ventanaDI, text='Desea modificar variables asociadas a los costos de energía', font=('Consolas',11), justify='center', bg='light blue')
subtituloEnergeticos.place(x=5,y=325)
#Botón de ir a ventana de costos de energía
botonIrVentanaEnerg=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaEnergetica, width=8)
botonIrVentanaEnerg.place(x=720,y=325)

"""Características ventana energética"""
ventanaEnergetica=tk.Toplevel()
ventanaEnergetica.title("Análisis financiero proyectos Energía Renovable")
ventanaEnergetica.geometry('1000x700')
ventanaEnergetica.configure(background='#004292')

#Titulo ventana datos energeticos
titulo=tk.Label(ventanaEnergetica, text='Datos de consumo actual', font=('Consolas',13), justify='center')
titulo.place(x=380,y=150)

#Tarifa de energía de la red
tarifaEnergiaRed=tk.Label(ventanaEnergetica,text='Tarifa energía de la red (COP/kWh)', font=('Consolas',10),justify='left')
tarifaEnergiaRed.place(x=5,y=183,height=18)
valorTarifaEnergiaRed=tk.DoubleVar(value=700)
entradaValorTarifaEnergiaRed=tk.Entry(ventanaEnergetica,textvariable=valorTarifaEnergiaRed, bg='orange2')
entradaValorTarifaEnergiaRed.place(x=460,y=183, height=18)

#CostoEnergíaPPA
costoEnergiaPPA=tk.Label(ventanaEnergetica,text='Costo energía PPA (COP/kWh)', font=('Consolas',10),justify='left')
costoEnergiaPPA.place(x=5,y=205,height=18)
valorCostoEnergiaPPA=tk.DoubleVar(value=300)
entradaValorCostoEnergiaPPA=tk.Entry(ventanaEnergetica,textvariable=valorCostoEnergiaPPA, bg='orange2')
entradaValorCostoEnergiaPPA.place(x=460,y=205, height=18)

#Costo energia PPA autogenerador
costoEnergiaPPAgen=tk.Label(ventanaEnergetica,text='Costo energía PPA con Autogenerador (COP/kWh)', font=('Consolas',10),justify='left')
costoEnergiaPPAgen.place(x=5,y=227,height=18)
valorCostoEnergiaPPAgen=tk.DoubleVar(value=350)
entradaValorCostoEnergiaPPAgen=tk.Entry(ventanaEnergetica,textvariable=valorCostoEnergiaPPAgen, bg='orange2')
entradaValorCostoEnergiaPPAgen.place(x=460,y=227, height=18)

#Costo actual Generación
costoGeneracion=tk.Label(ventanaEnergetica,text='Costo actual generación (COP/kWh)', font=('Consolas',10),justify='left')
costoGeneracion.place(x=5,y=249,height=18)
valorCostoGeneracion=tk.DoubleVar(value=307)
entradaValorCostoGeneracion=tk.Entry(ventanaEnergetica,textvariable=valorCostoGeneracion, bg='orange2')
entradaValorCostoGeneracion.place(x=460,y=249, height=18)

#Costo actual comercialización
costoComercializacion=tk.Label(ventanaEnergetica,text='Costo actual comercialización (COP/kWh)', font=('Consolas',10),justify='left')
costoComercializacion.place(x=5,y=271,height=18)
valorCostoComercializacion=tk.DoubleVar(value=13)
entradaValorCostoComercializacion=tk.Entry(ventanaEnergetica,textvariable=valorCostoComercializacion, bg='orange2')
entradaValorCostoComercializacion.place(x=460,y=271, height=18)

#Costo actual pérdidas
costoPerdidas=tk.Label(ventanaEnergetica,text='Costo actual perdidas (COP/kWh)', font=('Consolas',10),justify='left')
costoPerdidas.place(x=5,y=293,height=18)
valorCostoPerdidas=tk.DoubleVar(value=34)
entradaValorCostoPerdidas=tk.Entry(ventanaEnergetica,textvariable=valorCostoPerdidas, bg='orange2')
entradaValorCostoPerdidas.place(x=460,y=293, height=18)

#Costo actual transmisión
costoTransmision=tk.Label(ventanaEnergetica,text='Costo actual transmisión (COP/kWh)', font=('Consolas',10),justify='left')
costoTransmision.place(x=5,y=315,height=18)
valorCostoTransmision=tk.DoubleVar(value=50)
entradaValorCostoTransmision=tk.Entry(ventanaEnergetica,textvariable=valorCostoTransmision, bg='orange2')
entradaValorCostoTransmision.place(x=460,y=315, height=18)

#Costo actual distribución
costoDistribucion=tk.Label(ventanaEnergetica,text='Costo actual distribución (COP/kWh)', font=('Consolas',10),justify='left')
costoDistribucion.place(x=5,y=337,height=18)
valorCostoDistribucion=tk.DoubleVar(value=111)
entradaValorCostoDistribucion=tk.Entry(ventanaEnergetica,textvariable=valorCostoDistribucion, bg='orange2')
entradaValorCostoDistribucion.place(x=460,y=337, height=18)

#Costo actual restricciones
costoRestricciones=tk.Label(ventanaEnergetica,text='Costo actual restricciones (COP/kWh)', font=('Consolas',10),justify='left')
costoRestricciones.place(x=5,y=359,height=18)
valorCostoRestricciones=tk.DoubleVar(value=26)
entradaValorCostoRestricciones=tk.Entry(ventanaEnergetica,textvariable=valorCostoRestricciones, bg='orange2')
entradaValorCostoRestricciones.place(x=460,y=359, height=18)

#Costo actual contribuciones 
costoContribuciones=tk.Label(ventanaEnergetica,text='Costo actual contribuciones (%)', font=('Consolas',10),justify='left')
costoContribuciones.place(x=5,y=381,height=18)
valorCostoContribuciones=tk.DoubleVar(value=20)
entradaValorCostoContribuciones=tk.Entry(ventanaEnergetica,textvariable=valorCostoContribuciones, bg='orange2')
entradaValorCostoContribuciones.place(x=460,y=381, height=18)

#Costo propuesto comercialización
costoPropuestoComercializacion=tk.Label(ventanaEnergetica,text='Costo propuesto comercializacion (COP/kWh)', font=('Consolas',10),justify='left')
costoPropuestoComercializacion.place(x=5,y=403,height=18)
valorCostoPropuestoComercializacion=tk.DoubleVar(value=13)
entradaValorCostoPropuestoComercializacion=tk.Entry(ventanaEnergetica,textvariable=valorCostoPropuestoComercializacion, bg='orange2')
entradaValorCostoPropuestoComercializacion.place(x=460,y=403, height=18)

#Costo CERE
CERE=tk.Label(ventanaEnergetica,text='Precio CERE (COP/kWh)', font=('Consolas',10),justify='left')
CERE.place(x=5,y=425,height=18)
valorCERE=tk.DoubleVar(value=70.01)
entradaValorCERE=tk.Entry(ventanaEnergetica,textvariable=valorCERE, bg='orange2')
entradaValorCERE.place(x=460,y=425, height=18)

#Estructura tarifaria basada en costos
subTitulo=tk.Label(ventanaEnergetica, text='Estructura tarifaría basada en costos', font=('Consolas',11), justify='center', bg='DeepSkyBlue2', fg='White')
subTitulo.place(x=5,y=447)

#Duración de pago de una tarifa basada en costos
duracionTarifaCostos=tk.Label(ventanaEnergetica,text='Duración de la tarifa basada en costos (años)', font=('Consolas',10),justify='left')
duracionTarifaCostos.place(x=5,y=477,height=18)
valorDuracionTarifaCostos=tk.DoubleVar(value=25)
entradaValorDuracionTarifaCostos=tk.Entry(ventanaEnergetica,textvariable=valorDuracionTarifaCostos, bg='orange2')
entradaValorDuracionTarifaCostos.place(x=460,y=477, height=18)

#Porcentaje de incremento de la tarifa del primer año
porcentajeIncrementoTarifa=tk.Label(ventanaEnergetica,text='Porcentaje de incremento de la tarifa del primer año (%)', font=('Consolas',10),justify='left')
porcentajeIncrementoTarifa.place(x=5,y=499,height=18)
valorPorcentajeIncrementoTarifa=tk.DoubleVar(value=100)
entradaValorPorcentajeIncrementoTarifa=tk.Entry(ventanaEnergetica,textvariable=valorPorcentajeIncrementoTarifa, bg='orange2')
entradaValorPorcentajeIncrementoTarifa.place(x=460,y=499, height=18)

#Tasa de escala de la tarifa basada en costos
tasaTarifaCostos=tk.Label(ventanaEnergetica,text='Tasa de la tarifa basada en costos (%)', font=('Consolas',10),justify='left')
tasaTarifaCostos.place(x=5,y=521,height=18)
valorTasaTarifaCostos=tk.DoubleVar(value=5)
entradaValorTasaTarifaCostos=tk.Entry(ventanaEnergetica,textvariable=valorTasaTarifaCostos, bg='orange2')
entradaValorTasaTarifaCostos.place(x=460,y=521, height=18)



"""Boton para regresar a la ventana DI"""
botonIrVentanaDI=tk.Button(ventanaEnergetica,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI_Energetica, width=8)
botonIrVentanaDI.place(x=5,y=650)

"""Características ventana de impuestos"""
ventanaImpuestos=tk.Toplevel()
ventanaImpuestos.title("Análisis financiero proyectos Energía Renovable")
ventanaImpuestos.geometry('1000x700')
ventanaImpuestos.configure(background='#004292')

#Titulo ventana financiación de impuestos
titulo=tk.Label(ventanaImpuestos, text='Impuestos', font=('Consolas',13), justify='center')
titulo.place(x=420,y=211)

#Seleccion de impuestos
impuestos=tk.Label(ventanaImpuestos,text='¿Es el propietario una entidad sujeta a impuestos?', font=('Consolas',10),justify='left')
impuestos.place(x=5,y=250,height=18)
impuestos=tk.IntVar() #Guarda la respuesta
opcion_1=tk.Radiobutton(ventanaImpuestos,text='Sí',font=('Consolas',10),value=1,variable=impuestos)
opcion_1.place(x=460,y=250,height=18)
opcion_2=tk.Radiobutton(ventanaImpuestos,text='No',font=('Consolas',10),value=0,variable=impuestos)
opcion_2.place(x=510,y=250,height=18)

#Tasa de impuesto sobre la renta
tasaImpuestoRenta=tk.Label(ventanaImpuestos,text='Tasa de impuesto sobre la renta (%)', font=('Consolas',10),justify='left')
tasaImpuestoRenta.place(x=5,y=278,height=18)
valorImpuestoRenta=tk.DoubleVar(value=35)
entradaValorImpuestoRenta=tk.Entry(ventanaImpuestos,textvariable=valorImpuestoRenta, bg='orange2')
entradaValorImpuestoRenta.place(x=460,y=278, height=18)

#Tasa de impuesto local
tasaImpuestoLocal=tk.Label(ventanaImpuestos,text='Tasa de impuesto local (%)', font=('Consolas',10),justify='left')
tasaImpuestoLocal.place(x=5,y=302,height=18)
valorImpuestoLocal=tk.DoubleVar(value=0)
entradaValorImpuestoLocal=tk.Entry(ventanaImpuestos,textvariable=valorImpuestoLocal, bg='orange2')
entradaValorImpuestoLocal.place(x=460,y=302, height=18)


"""Boton para regresar a la ventana DI"""
botonIrVentanaDI=tk.Button(ventanaImpuestos,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI_Impuestos, width=8)
botonIrVentanaDI.place(x=5,y=650)



"""Características ventana de financiación de la deuda"""
ventanaFinan=tk.Toplevel()
ventanaFinan.title("Análisis financiero proyectos Energía Renovable")
ventanaFinan.geometry('1000x700')
ventanaFinan.configure(background='#004292')

#Titulo ventana financiación de la deuda
titulo=tk.Label(ventanaFinan, text='Financiación', font=('Consolas',13), justify='center')
titulo.place(x=420,y=160)

#Financiación de la construcción
subTitulo=tk.Label(ventanaFinan, text='Financiación de la construcción', font=('Consolas',11), justify='center', bg='DeepSkyBlue2', fg='White')
subTitulo.place(x=5,y=184)

#Periodos de financiación de construcción
periodoFinanciacion=tk.Label(ventanaFinan,text='Período de construcción (meses)', font=('Consolas',10),justify='left')
periodoFinanciacion.place(x=5,y=214,height=18)
valorPeriodoFinanciacion=tk.DoubleVar(value=8)
entradaPeriodoFinanciacion=tk.Entry(ventanaFinan,textvariable=valorPeriodoFinanciacion, bg='orange2')
entradaPeriodoFinanciacion.place(x=460,y=214, height=18)

#Tasa de interes anual
tasaInteresDeuda=tk.Label(ventanaFinan,text='Tasa efectiva de interés anual (%)', font=('Consolas',10),justify='left')
tasaInteresDeuda.place(x=5,y=236,height=18)
valorTasaInteres=tk.DoubleVar(value=13)
entradaTasaInteres=tk.Entry(ventanaFinan,textvariable=valorTasaInteres, bg='orange2')
entradaTasaInteres.place(x=460,y=236, height=18)

#Financión para costo total del proyecto a largo plazo. 
subTituloFinan=tk.Label(ventanaFinan, text='Financiación de la construcción a largo plazo', font=('Consolas',11), justify='center',bg='DeepSkyBlue2', fg='White')
subTituloFinan.place(x=5,y=258)

#Porcentaje de costos duros
porcenCostosDuros=tk.Label(ventanaFinan,text='Porcentaje de costos duros (%)', font=('Consolas',10),justify='left')
porcenCostosDuros.place(x=5,y=288,height=18)
valorPorcenCostosDuros=tk.DoubleVar(value=10)
entradaPorcenCostosDuros=tk.Entry(ventanaFinan,textvariable=valorPorcenCostosDuros, bg='orange2')
entradaPorcenCostosDuros.place(x=460,y=288, height=18)

#Plazo de la Deuda
plazoDeuda=tk.Label(ventanaFinan,text='Plazo de la deuda (años)', font=('Consolas',10),justify='left')
plazoDeuda.place(x=5,y=310,height=18)
valorPlazoDeuda=tk.DoubleVar(value=15)
entradaValorPlazoDeuda=tk.Entry(ventanaFinan,textvariable=valorPlazoDeuda, bg='orange2')
entradaValorPlazoDeuda.place(x=460,y=310, height=18)

#Tasa de interés de la Deuda
interesDeuda=tk.Label(ventanaFinan,text='Tasa de interés deuda a largo plazo (%)', font=('Consolas',10),justify='left')
interesDeuda.place(x=5,y=332,height=18)
valorInteresDeuda=tk.DoubleVar(value=9)
entradaValorInteresDeuda=tk.Entry(ventanaFinan,textvariable=valorInteresDeuda, bg='orange2')
entradaValorInteresDeuda.place(x=460,y=332, height=18)

#Tarifa del prestamista porcentaje total
tarifaPrestamista=tk.Label(ventanaFinan,text='Tarifa del prestamista porcentaje total (%)', font=('Consolas',10),justify='left')
tarifaPrestamista.place(x=5,y=354,height=18)
valorTarifaPrestamista=tk.DoubleVar(value=0)
entradaValorTarifaPrestamista=tk.Entry(ventanaFinan,textvariable=valorTarifaPrestamista, bg='orange2')
entradaValorTarifaPrestamista.place(x=460,y=354, height=18)

#DCSR mínimo requerido
DCSRminimo=tk.Label(ventanaFinan,text='DCSR mínimo requerido (Un)', font=('Consolas',10),justify='left')
DCSRminimo.place(x=5,y=376,height=18)
valorDCSRminimo=tk.DoubleVar(value=1.2)
entradaValorDCSRminimo=tk.Entry(ventanaFinan,textvariable=valorDCSRminimo, bg='orange2')
entradaValorDCSRminimo.place(x=460,y=376, height=18)

#DCSR promedio requerido
DCSRpromedio=tk.Label(ventanaFinan,text='DCSR promedio requerido (Un)', font=('Consolas',10),justify='left')
DCSRpromedio.place(x=5,y=398,height=18)
valorDCSRpromedio=tk.DoubleVar(value=1.45)
entradaValorDCSRpromedio=tk.Entry(ventanaFinan,textvariable=valorDCSRpromedio, bg='orange2')
entradaValorDCSRpromedio.place(x=460,y=398, height=18)

#TIR después de impuestos
equityTIR=tk.Label(ventanaFinan,text='TIR después de impuestos (%)', font=('Consolas',10),justify='left')
equityTIR.place(x=5,y=420,height=18)
valorEquityTIR=tk.DoubleVar(value=13)
entradaValorEquityTIR=tk.Entry(ventanaFinan,textvariable=valorEquityTIR, bg='orange2')
entradaValorEquityTIR.place(x=460,y=420, height=18)

#Financiamiento cuentas de reserva. 
subTituloCuentaRes=tk.Label(ventanaFinan, text='Financiación cuentas de reserva', font=('Consolas',11), justify='center',bg='DeepSkyBlue2', fg='White')
subTituloCuentaRes.place(x=5,y=442)

#Número de meses de servicio de la deuda
numeroServicioDeuda=tk.Label(ventanaFinan,text='Número de meses de servicio de la deuda (meses)', font=('Consolas',10),justify='left')
numeroServicioDeuda.place(x=5,y=472,height=18)
valorNumeroServicioDeuda=tk.DoubleVar(value=4)
entradaValorNumeroServicioDeuda=tk.Entry(ventanaFinan,textvariable=valorNumeroServicioDeuda, bg='orange2')
entradaValorNumeroServicioDeuda.place(x=460,y=472, height=18)

#Financiamiento cuentas de reserva para operación y mantenimiento. 
subTituloOyMRes=tk.Label(ventanaFinan, text='Reserva en operación y mantenimiento', font=('Consolas',11), justify='center',bg='DeepSkyBlue2', fg='White')
subTituloOyMRes.place(x=5,y=502)

#Número de meses de gasto de Operación y mantenimiento
numeroDeMesesGastoOyM=tk.Label(ventanaFinan,text='Número de meses de gasto en O&M reserva (meses)', font=('Consolas',10),justify='left')
numeroDeMesesGastoOyM.place(x=5,y=532,height=18)
valorNumeroDeMesesGastoOyM=tk.DoubleVar(value=4)
entradaValorNumeroDeMesesGastoOyM=tk.Entry(ventanaFinan,textvariable=valorNumeroDeMesesGastoOyM, bg='orange2')
entradaValorNumeroDeMesesGastoOyM.place(x=460,y=532, height=18)

#Interés cuentas de reserva
interesCuentaReserva=tk.Label(ventanaFinan,text='Intereses cuenta de reserva (%)', font=('Consolas',10),justify='left')
interesCuentaReserva.place(x=5,y=554,height=18)
valorInteresCuentaReserva=tk.DoubleVar(value=13)
entradaValorInteresCuentaReserva=tk.Entry(ventanaFinan,textvariable=valorInteresCuentaReserva, bg='orange2')
entradaValorInteresCuentaReserva.place(x=460,y=554, height=18)

"""Boton para regresar a la ventana DI"""
botonIrVentanaDI=tk.Button(ventanaFinan,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI_Finan, width=8)
botonIrVentanaDI.place(x=5,y=650)


"""Características ventana costos operación y mantenimiento"""
ventanaOyM=tk.Toplevel()
ventanaOyM.title("Análisis financiero proyectos Energía Renovable")
ventanaOyM.geometry('1000x700')
ventanaOyM.configure(background='#004292')

"""Boton para regresar a la ventana DI"""

botonIrVentanaDI=tk.Button(ventanaOyM,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI, width=8)
botonIrVentanaDI.place(x=5,y=650)

"""Boton para salir de ventana OyM"""
botonSalir=tk.Button(ventanaOyM,text='Salir del programa',font=('Consolas',10),command=salir)
botonSalir.place(x=845,y=660)


"""Costos asociados a la operación y mantenimiento"""
#Costos asociados a la operación y mantenimiento
subtitulo=tk.Label(ventanaOyM, text='Gastos de operación y mantenimiento', font=('Consolas',13), justify='center')
subtitulo.place(x=350,y=100)
#Gastos fijos de operación y mantenimiento
GastosOyM=tk.Label(ventanaOyM,text='Costo Fijo de operación y mantenimiento $/kW', font=('Consolas',10),justify='left')
GastosOyM.place(x=5,y=130,height=18)
valorGastosOyM=tk.DoubleVar(value=19825)
entradaGastosOyM=tk.Entry(ventanaOyM,textvariable=valorGastosOyM, bg='orange2')
entradaGastosOyM.place(x=460,y=130, height=18)
#Gasto variable de operación y mantenimiento
GastosVarOyM=tk.Label(ventanaOyM,text='Costo Variable de operación y mantenimiento ¢/kWh', font=('Consolas',10),justify='left')
GastosVarOyM.place(x=5,y=152,height=18)
valorGastosVarOyM=tk.DoubleVar(value=118.95)
entradaGastosVarOyM=tk.Entry(ventanaOyM,textvariable=valorGastosVarOyM, bg='orange2')
entradaGastosVarOyM.place(x=460,y=152, height=18)
#Inflación de costos de operación y mantenimiento
inflacionOyM=tk.Label(ventanaOyM,text='Inflación de costos de operación y mantenimiento (%)', font=('Consolas',10),justify='left')
inflacionOyM.place(x=5,y=174,height=18)
valorInflacionOyM=tk.DoubleVar(value=8)
entradaInflacionOyM=tk.Entry(ventanaOyM,textvariable=valorInflacionOyM, bg='orange2')
entradaInflacionOyM.place(x=460,y=174, height=18)
#Período de finalización del primer porcentaje de inflación
periodoInflacionOyM=tk.Label(ventanaOyM,text='Primer periodo de finalización de la inflación (años)', font=('Consolas',10),justify='left')
periodoInflacionOyM.place(x=5,y=196,height=18)
valorPeriodoInflacionOyM=tk.DoubleVar(value=10)
entradaPeriodoInflacionOyM=tk.Entry(ventanaOyM,textvariable=valorPeriodoInflacionOyM, bg='orange2')
entradaPeriodoInflacionOyM.place(x=460,y=196, height=18)
#Inflación después de primer periodo
inflacionOyM_dos=tk.Label(ventanaOyM,text='2da Inflación de costos de operación y mantenimiento (%)', font=('Consolas',10),justify='left')
inflacionOyM_dos.place(x=5,y=218,height=18)
valorInflacionOyM_dos=tk.DoubleVar(value=4)
entradaInflacionOyM_dos=tk.Entry(ventanaOyM,textvariable=valorInflacionOyM_dos, bg='orange2')
entradaInflacionOyM_dos.place(x=460,y=218, height=18)
#Seguro año 1
seguroOyM=tk.Label(ventanaOyM,text='Seguro año 1 porcentaje costo total (%)', font=('Consolas',10),justify='left')
seguroOyM.place(x=5,y=240,height=18)
valorSeguroOyM=tk.DoubleVar(value=0.3)
entradaSeguroOyM=tk.Entry(ventanaOyM,textvariable=valorSeguroOyM, bg='orange2')
entradaSeguroOyM.place(x=460,y=240, height=18)
#Gastos de administración
administracionOyM=tk.Label(ventanaOyM,text='Costos de administración ($/año)', font=('Consolas',10),justify='left')
administracionOyM.place(x=5,y=262,height=18)
valorAdministracionOyM=tk.DoubleVar(value=80000000)
entradaAdministracionOyM=tk.Entry(ventanaOyM,textvariable=valorAdministracionOyM, bg='orange2')
entradaAdministracionOyM.place(x=460,y=262, height=18)
#Impuesto sobre la propiedad
impuestoPropiedad=tk.Label(ventanaOyM,text=' Impuesto sobre la propiedad ($/año)', font=('Consolas',10),justify='left')
impuestoPropiedad.place(x=5,y=284,height=18)
valorImpuestoPropiedad=tk.DoubleVar(value=2000000)
entradaImpuestoPropiedad=tk.Entry(ventanaOyM,textvariable=valorImpuestoPropiedad, bg='orange2')
entradaImpuestoPropiedad.place(x=460,y=284, height=18)
#Factor de ajuste de impuesto anual sobre la propiedad
ajusteImpuestoPropiedad=tk.Label(ventanaOyM,text=' Ajuste anual impuesto sobre la propiead (%)', font=('Consolas',10),justify='left')
ajusteImpuestoPropiedad.place(x=5,y=306,height=18)
valorAjusteImpuestoPropiedad=tk.DoubleVar(value=5)
entradaAjusteImpuestoPropiedad=tk.Entry(ventanaOyM,textvariable=valorAjusteImpuestoPropiedad, bg='orange2')
entradaAjusteImpuestoPropiedad.place(x=460,y=306, height=18)
#Valor arriendo
valorArriendo=tk.Label(ventanaOyM,text='Valor de arriendo ($/ha)', font=('Consolas',10),justify='left')
valorArriendo.place(x=5,y=328,height=18)
valorArriendoHa=tk.DoubleVar(value=5000000)
entradaValorArriendoHa=tk.Entry(ventanaOyM,textvariable=valorArriendoHa, bg='orange2')
entradaValorArriendoHa.place(x=460,y=328, height=18)
#Valor Costo Tierra
valorCostoTierra=tk.Label(ventanaOyM,text='Valor costo Tierra ($/ha)', font=('Consolas',10),justify='left')
valorCostoTierra.place(x=5,y=350,height=18)
valorCostoTierraHa=tk.DoubleVar(value=0)
entradaValorCostoTierraHa=tk.Entry(ventanaOyM,textvariable=valorCostoTierraHa)
entradaValorCostoTierraHa.place(x=460,y=350, height=18)
#Participación del cliente en Equity
participacionCliente=tk.Label(ventanaOyM,text='Participación del cliente en equity (%)', font=('Consolas',10),justify='left')
participacionCliente.place(x=5,y=372,height=18)
valorParticipacionCliente=tk.DoubleVar(value=0)
entradaValorParticipacionCliente=tk.Entry(ventanaOyM,textvariable=valorParticipacionCliente,bg='orange2')
entradaValorParticipacionCliente.place(x=460,y=372, height=18)
#Aporte del cliente en capital
aporteCliente=tk.Label(ventanaOyM,text='Aporte del cliente a capital ($)', font=('Consolas',10),justify='left')
aporteCliente.place(x=5,y=394,height=18)
valorAporteCliente=tk.DoubleVar(value=0)
entradaValorAporteCliente=tk.Entry(ventanaOyM,textvariable=valorAporteCliente,bg='orange2')
entradaValorAporteCliente.place(x=460,y=394, height=18)
#Regalias 
regalias=tk.Label(ventanaOyM,text='Porcentaje de los ingresos a regalías (%)', font=('Consolas',10),justify='left')
regalias.place(x=5,y=416,height=18)
valorRegalias=tk.DoubleVar(value=0)
entradaValorRegalias=tk.Entry(ventanaOyM,textvariable=valorRegalias,bg='orange2')
entradaValorRegalias.place(x=460,y=416, height=18)

#Gastos de reemplazo de equipos
subtituloReem=tk.Label(ventanaOyM, text='Gastos de capital durante operaciones', font=('Consolas',11), justify='left', bg='DeepSkyBlue2', fg='White')
subtituloReem.place(x=5,y=446)

#Año de reemplazo del primer equipo
reemplazoEquipo=tk.Label(ventanaOyM,text='Primer reemplazo inversores (años)', font=('Consolas',10),justify='left')
reemplazoEquipo.place(x=5,y=476,height=18)
valorReemplazoEquipo=tk.DoubleVar(value=10)
entradaValorReemplazoEquipo=tk.Entry(ventanaOyM,textvariable=valorReemplazoEquipo,bg='orange2')
entradaValorReemplazoEquipo.place(x=460,y=476, height=18)

#Costo por año de reemplazar el equipo
costoReemplazoEquipo=tk.Label(ventanaOyM,text='Costo de reemplazo primera vez (COP/Watt)', font=('Consolas',10),justify='left')
costoReemplazoEquipo.place(x=5,y=498,height=18)
valorCostoReemplazoEquipo=tk.DoubleVar(value=250)
entradaValorCostoReemplazoEquipo=tk.Entry(ventanaOyM,textvariable=valorCostoReemplazoEquipo,bg='orange2')
entradaValorCostoReemplazoEquipo.place(x=460,y=498, height=18)

#Segundo año de reemplazo de equipo
reemplazoEquipo_dos=tk.Label(ventanaOyM,text='Segundo reemplazo inversores (años)', font=('Consolas',10),justify='left')
reemplazoEquipo_dos.place(x=5,y=520,height=18)
valorReemplazoEquipo_dos=tk.DoubleVar(value=20)
entradaValorReemplazoEquipo_dos=tk.Entry(ventanaOyM,textvariable=valorReemplazoEquipo_dos,bg='orange2')
entradaValorReemplazoEquipo_dos.place(x=460,y=520, height=18)

#Costo segundo año de reemplazar el equipo
costoReemplazoEquipo_dos=tk.Label(ventanaOyM,text='Costo de reemplazo segunda vez (COP/Watt)', font=('Consolas',10),justify='left')
costoReemplazoEquipo_dos.place(x=5,y=542,height=18)
valorCostoReemplazoEquipo_dos=tk.DoubleVar(value=200)
entradaValorCostoReemplazoEquipo_dos=tk.Entry(ventanaOyM,textvariable=valorCostoReemplazoEquipo_dos,bg='orange2')
entradaValorCostoReemplazoEquipo_dos.place(x=460,y=542, height=18)


ocultarVentana(ventanaEnergetica)
ocultarVentana(ventanaImpuestos)
ocultarVentana(ventanaFinan)
ocultarVentana(ventanaOyM)
ocultarVentana(ventanaDI)
ventana.mainloop()






