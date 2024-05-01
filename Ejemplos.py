# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:15:04 2024

@author: ASUS
"""
import tkinter as tk
from PIL import Image, ImageTk  #Librería para usar imagenes en la ventanas
from tkinter import messagebox #Librería para mensajes de advertencia
from Anal_Finan_CAPEX import generarResultados
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel
import locale
from Reporte_Excel import CalculoEnergia
from Reporte_Excel import potenciaOptima
from Anal_Finan_CAPEX import conductorOptimo


"""Funciones"""





def contadorExcel():
    global contador
    global resultadosDict
    global valorEnergia
    contador+=1
    ReporteLabel.config(text=f"Número de veces que se ha generado el reporte: {contador}")
    
    if calculoExactoVar.get()==1:
        demanda=[valorDemandaEnero.get(),valorDemandaFebrero.get(),valorDemandaMarzo.get(),valorDemandaAbril.get(),
                 valorDemandaMayo.get(),valorDemandaJunio.get(),valorDemandaJulio.get(),valorDemandaAgosto.get(),
                 valorDemandaSeptiembre.get(),valorDemandaOctubre.get(),valorDemandaNoviembre.get(),valorDemandaDiciembre.get()]
        irradiancia=[valorIrradianciaEnero.get(),valorIrradianciaFebrero.get(),valorIrradianciaMarzo.get(),valorIrradianciaAbril.get(),
                 valorIrradianciaMayo.get(),valorIrradianciaJunio.get(),valorIrradianciaJulio.get(),valorIrradianciaAgosto.get(),
                 valorIrradianciaSeptiembre.get(),valorIrradianciaOctubre.get(),valorIrradianciaNoviembre.get(),valorIrradianciaDiciembre.get()]        
        valorEnergia=CalculoEnergia(demanda,irradiancia,valorCapacidad.get())
        
    resultadosDict=generarResultados(valorCapacidad.get(),valorIrradiancia.get(), valorAutoconsumo.get(), valorDemanda.get(),valorENFICC.get(),
                      valorTarifaEnergiaRed.get(), valorCostoEnergiaPPA.get(), valorCostoEnergiaPPAgen.get(), valorCERE.get(),
                      valorArriendoHa.get(),valorAdministracionOyM.get(), valorTarifaPrestamista.get(), valorPorcenCostosDuros.get(),
                      var.get(),track.get(), varLC.get(),varCLC.get(), valorPeriodoFinanciacion.get(), valorTasaInteres.get(),
                      valorPlazoDeuda.get(), valorInteresDeuda.get(),valorDCSRminimo.get(), valorSeguroOyM.get(), valorPorcentajeIncrementoTarifa.get(),
                      valorTasaTarifaCostos.get(), valorRegalias.get(), valorPeriodoInflacionOyM.get(), valorGastosOyM.get(),
                      valorAporteCliente.get(),valorGastosVarOyM.get(), valorInflacionOyM.get(), valorInflacionOyM_dos.get(),
                      valorNumeroServicioDeuda.get(),valorNumeroDeMesesGastoOyM.get(),valorInteresCuentaReserva.get(),
                      valorReemplazoEquipo.get(), valorCostoReemplazoEquipo.get(),valorReemplazoEquipo_dos.get(),
                      valorCostoReemplazoEquipo_dos.get(),depreciacion.get(),valorTasaDepreciacionLn.get(),valorTiempoDepreciacionLn.get(),
                      valorTasaDepreciacionAc.get(),impuestos.get(),valorBaseGravable.get(),valorMaxDesCapex.get(),
                      valorImpuestoRenta.get(), valorEquityTIR.get(), contador, valorDCSRpromedio.get(), valorCambioEntrada.get(), valorReporteEx.get(),
                      valorDuracionTarifaCostos.get(), valorCostoPaneles.get(), valorCostoInversores.get(), valorCostoCableadoDC.get(),
                      valorCostoCableadoAC.get(), valorCostoSistemaMonitoreo.get(), valorCostoTuberia.get(), valorCostoCerramiento.get(),
                      valorCostoSPT.get(), valorCostoOtros.get(), valorCostoMaquinaria.get(), valorCostoInstalacion.get(),
                      valorCostoImprevistos.get(), valorCostoIngenieria.get(), valorCostoEstSuelos.get(), valorCostoResistividad.get(),
                      valorCostoEstTopografico.get(), valorCostoPruebas.get(), valorCostoCampamento.get(), valorCostoSPDA.get(), valorCostoTransformador.get(),
                      valorCostoProtecciones.get(), valorCostoMedidores.get(), calculoExactoVar.get(),list(valorEnergia), valorLCDig.get(), distanciaDig.get())
    

    
    print(valorEnergia)
      
    
    
    """
    if len(resultadosDict)>0 and valorReporteEx.get()==0:
                      
        df = pd.DataFrame(resultadosDict)
        df_transposed = df.transpose()
        df_transposed.reset_index(inplace=True)
        table = Table(frame, dataframe=df_transposed, width=1000)
        table.autoResizeColumns()
        table.show()
     """   
    #if valorReporteEx.get()==1:
    df = pd.read_excel('Reporte Excel.xlsx', sheet_name="Resumen Proyecto")
    table = Table(frame, dataframe=df, width=1000, height=500)
    table.autoResizeColumns()
    table.show()
    
contador=0
valorEnergia=[]
resultadosDict={}

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
    
"""Función para mostrar ventana DI desde Capex"""
def mostrarVentanaDI_Capex():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaCapex) 
    
def mostrarVentanaCapex():
    mostrarVentana(ventanaCapex)
    ocultarVentana(ventanaDI)
    
def mostrarVentanaGen():
    mostrarVentana(ventanaGen)
    ocultarVentana(ventanaDI)

def mostrarVentanaDI_Gen():
    mostrarVentana(ventanaDI)
    ocultarVentana(ventanaGen)

def mostrarVentanaEC():
    mostrarVentana(ventanaEC)
    
def ocultarVentanaEC():
    ocultarVentana(ventanaEC)
    
    
"""Función para convertir número a contable"""
def convertir_formato_contable(event):
    # Obtener el valor actual en el campo de entrada
    valor = valorTarifaEnergiaRed.get()

    try:
        # Convertir el valor a formato de moneda
        valor_formateado = locale.currency(float(valor), grouping=True)

        # Mostrar el valor en formato contable en el mismo campo de entrada
        valorTarifaEnergiaRed.delete(0, tk.END)  # Limpiar el campo de entrada
        valorTarifaEnergiaRed.insert(0, valor_formateado)  # Insertar el valor formateado en el campo de entrada
    except ValueError:
        # Manejar errores si el usuario ingresa un valor no válido
        valorTarifaEnergiaRed.delete(0, tk.END)
        valorTarifaEnergiaRed.insert(0, "Error: Ingresa un número válido")

    

def mostrarPotenciaOPT():
    demanda=[valorDemandaEnero.get(),valorDemandaFebrero.get(),valorDemandaMarzo.get(),valorDemandaAbril.get(),
             valorDemandaMayo.get(),valorDemandaJunio.get(),valorDemandaJulio.get(),valorDemandaAgosto.get(),
             valorDemandaSeptiembre.get(),valorDemandaOctubre.get(),valorDemandaNoviembre.get(),valorDemandaDiciembre.get()]
    irradiancia=[valorIrradianciaEnero.get(),valorIrradianciaFebrero.get(),valorIrradianciaMarzo.get(),valorIrradianciaAbril.get(),
             valorIrradianciaMayo.get(),valorIrradianciaJunio.get(),valorIrradianciaJulio.get(),valorIrradianciaAgosto.get(),
             valorIrradianciaSeptiembre.get(),valorIrradianciaOctubre.get(),valorIrradianciaNoviembre.get(),valorIrradianciaDiciembre.get()]
    calculoPotenciaOPT=potenciaOptima(demanda,irradiancia)
    resultado_potenciaOPT.config(text=f"la potencia óptima del proyecto es: {calculoPotenciaOPT}")

def mostrarConductorOPT():
    planta=[valorCapacidad.get(),valorIrradiancia.get(),0.5,76.2,valorENFICC.get()]
    energia=[valorAutoconsumo.get(),valorCostoEnergiaPPAgen.get(),valorTasaTarifaCostos.get(),valorCostoEnergiaPPA.get(), valorCERE.get()]
    gastos=[valorGastosOyM.get(), valorPeriodoInflacionOyM.get(), valorAporteCliente.get(),valorGastosVarOyM.get(),valorAdministracionOyM.get(),
            valorArriendoHa.get(),valorSeguroOyM.get(),valorInflacionOyM.get(), valorInflacionOyM_dos.get()]
    costos=[valorCostoPaneles.get(),valorCostoInversores.get(),valorCostoCableadoDC.get(),valorCostoCableadoAC.get(),valorCostoSistemaMonitoreo.get(),
            valorCostoTuberia.get(),valorCostoCerramiento.get(),valorCostoSPT.get(),valorCostoOtros.get(),valorCostoMaquinaria.get(),
            valorCostoInstalacion.get(),valorCostoImprevistos.get(),valorCostoIngenieria.get(),valorCostoEstSuelos.get(), valorCostoEstTopografico.get(),
            valorCostoResistividad.get(),valorCostoPruebas.get(),valorCostoCampamento.get(),valorCostoSPDA.get(), varCLC.get(),valorCostoTransformador.get(),
            valorCostoProtecciones.get(),valorCostoMedidores.get()]
    condicionales=[var.get(),track.get(), valorPorcenCostosDuros.get(), valorReemplazoEquipo.get(),valorCostoReemplazoEquipo.get(), valorNumeroDeMesesGastoOyM.get(),
                   valorInteresDeuda.get(),valorPlazoDeuda.get(),valorNumeroServicioDeuda.get(),valorInteresCuentaReserva.get(), valorReemplazoEquipo_dos.get(),
                   valorTarifaPrestamista.get(), valorTasaInteres.get(), valorPeriodoFinanciacion.get(), valorEquityTIR.get()]
    conductorOPT=conductorOptimo(energia,planta,gastos,costos,condicionales)
    resultado_conductorOPT.config(text=f"la distancia critica del proyecto es: {conductorOPT}")

def mostrarEntrada():
    if valorLCDig.get()==1:
        entradaDistanciaDig.place(x=900, y=170, width=50)
    else:
        entradaDistanciaDig.place_forget()
"""Función para salir"""
def salir():
    ventana.quit()
    ventana.destroy()
    

locale.setlocale(locale.LC_ALL, '')

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

"""Características ventana GenyDem"""
ventanaGen=tk.Toplevel()
ventanaGen.title("Análisis financiero proyectos Energía Renovable")
ventanaGen.geometry('1000x700')
ventanaGen.configure(background='#004292')


"""Características ventana Indicadores ecónomicos"""
ventanaEC=tk.Toplevel()
ventanaEC.title("Ventana de indicadores ecónomicos")
ventanaEC.geometry('1100x600')
ventanaEC.configure(background='#004292')


"""Botón para salir"""
#botonSalir=tk.Button(ventanaEC,text='Salir del programa',font=('Consolas',12),command=salir)
#botonSalir.grid(row=3,column=1,padx=10, pady=10)
#botonSalir.place(x=395,y=200)

frame=tk.Frame(ventanaEC, bd=2, relief='groove')
frame.place(x=5,y=5)

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
valorCapacidad=tk.DoubleVar(value=4.99)
entradaPotencia=tk.Entry(ventanaDI, textvariable=valorCapacidad)
entradaPotencia.place(x=460,y=35, height=18)

#Entrada irradiancia del lugar 
irradiancia=tk.Label(ventanaDI, text='Digite la irradiancia del lugar (kW/m2)', font=('Consolas',10), justify='left')
irradiancia.place(x=5, y=57, height=18)
valorIrradiancia=tk.DoubleVar(value=4.5)
entradaIrradiancia=tk.Entry(ventanaDI, textvariable=valorIrradiancia)
entradaIrradiancia.place(x=460, y=57, height=18)

botonVenGen=tk.Button(ventanaDI,text='Método exacto de cálculo para generación y demanda',font=('Consolas',10),command=mostrarVentanaGen, bg='LightBlue1')
botonVenGen.place(x=620,y=57)

botonIrVentanaDI_Gen=tk.Button(ventanaGen,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI_Gen, width=8)
botonIrVentanaDI_Gen.place(x=5,y=650)

calculoExacto=tk.Label(ventanaGen,text='¿Esta seguro de usar el método de cálculo exacto?', font=('Consolas',10),justify='left', bg='LightBlue1')
calculoExacto.place(x=5,y=10,height=18)
calculoExactoVar=tk.IntVar() #Guarda la respuesta
opcion_1=tk.Radiobutton(ventanaGen,text='Sí',font=('Consolas',10),value=1,variable=calculoExactoVar)
opcion_1.place(x=380,y=10,height=18)
opcion_2=tk.Radiobutton(ventanaGen,text='No',font=('Consolas',10),value=0,variable=calculoExactoVar)
opcion_2.place(x=430,y=10,height=18)


subtituloVenGen=tk.Label(ventanaGen, text='Irradiancia', font=('Consolas',13,'bold'), justify='center', bg='DeepSkyBlue2', fg='light cyan')
subtituloVenGen.place(x=5,y=38)


#Irradiancia por mes
irradianciaEnero=tk.Label(ventanaGen, text='Digite la irradiancia mes de enero (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaEnero.place(x=5, y=65,height=18)
valorIrradianciaEnero=tk.DoubleVar(value=6.14)
entradaIrradianciaEnero=tk.Entry(ventanaGen, textvariable=valorIrradianciaEnero, bg='khaki1')
entradaIrradianciaEnero.place(x=337, y=65,height=18, width=60)

irradianciaFebrero=tk.Label(ventanaGen, text='Digite la irradiancia mes de febrero (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaFebrero.place(x=5, y=90,height=18)
valorIrradianciaFebrero=tk.DoubleVar(value=5.33)
entradaIrradianciaFebrero=tk.Entry(ventanaGen, textvariable=valorIrradianciaFebrero, bg='khaki1')
entradaIrradianciaFebrero.place(x=337, y=90,height=18, width=60)

irradianciaMarzo=tk.Label(ventanaGen, text='Digite la irradiancia mes de marzo (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaMarzo.place(x=5, y=115,height=18)
valorIrradianciaMarzo=tk.DoubleVar(value=3.705)
entradaIrradianciaMarzo=tk.Entry(ventanaGen, textvariable=valorIrradianciaMarzo, bg='khaki1')
entradaIrradianciaMarzo.place(x=337, y=115,height=18, width=60)

irradianciaAbril=tk.Label(ventanaGen, text='Digite la irradiancia mes de abril (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaAbril.place(x=5, y=140,height=18)
valorIrradianciaAbril=tk.DoubleVar(value=3.144)
entradaIrradianciaAbril=tk.Entry(ventanaGen, textvariable=valorIrradianciaAbril, bg='khaki1')
entradaIrradianciaAbril.place(x=337, y=140,height=18, width=60)

irradianciaMayo=tk.Label(ventanaGen, text='Digite la irradiancia mes de mayo (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaMayo.place(x=5, y=165,height=18)
valorIrradianciaMayo=tk.DoubleVar(value=3.463)
entradaIrradianciaMayo=tk.Entry(ventanaGen, textvariable=valorIrradianciaMayo, bg='khaki1')
entradaIrradianciaMayo.place(x=337, y=165,height=18, width=60)

irradianciaJunio=tk.Label(ventanaGen, text='Digite la irradiancia mes de junio (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaJunio.place(x=5, y=190,height=18)
valorIrradianciaJunio=tk.DoubleVar(value=3.3)
entradaIrradianciaJunio=tk.Entry(ventanaGen, textvariable=valorIrradianciaJunio, bg='khaki1')
entradaIrradianciaJunio.place(x=337, y=190,height=18, width=60)

irradianciaJulio=tk.Label(ventanaGen, text='Digite la irradiancia mes de julio (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaJulio.place(x=5, y=215,height=18)
valorIrradianciaJulio=tk.DoubleVar(value=3.349)
entradaIrradianciaJulio=tk.Entry(ventanaGen, textvariable=valorIrradianciaJulio, bg='khaki1')
entradaIrradianciaJulio.place(x=337, y=215,height=18, width=60)

irradianciaAgosto=tk.Label(ventanaGen, text='Digite la irradiancia mes de agosto (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaAgosto.place(x=5, y=240,height=18)
valorIrradianciaAgosto=tk.DoubleVar(value=3.421)
entradaIrradianciaAgosto=tk.Entry(ventanaGen, textvariable=valorIrradianciaAgosto, bg='khaki1')
entradaIrradianciaAgosto.place(x=337, y=240,height=18, width=60)

irradianciaSeptiembre=tk.Label(ventanaGen, text='Digite la irradiancia mes de septiembre (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaSeptiembre.place(x=5, y=265,height=18)
valorIrradianciaSeptiembre=tk.DoubleVar(value=3.917)
entradaIrradianciaSeptiembre=tk.Entry(ventanaGen, textvariable=valorIrradianciaSeptiembre, bg='khaki1')
entradaIrradianciaSeptiembre.place(x=337, y=265,height=18, width=60)

irradianciaOctubre=tk.Label(ventanaGen, text='Digite la irradiancia mes de octubre (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaOctubre.place(x=5, y=290,height=18)
valorIrradianciaOctubre=tk.DoubleVar(value=4.002)
entradaIrradianciaOctubre=tk.Entry(ventanaGen, textvariable=valorIrradianciaOctubre, bg='khaki1')
entradaIrradianciaOctubre.place(x=337, y=290,height=18, width=60)

irradianciaNoviembre=tk.Label(ventanaGen, text='Digite la irradiancia mes de noviembre (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaNoviembre.place(x=5, y=315,height=18)
valorIrradianciaNoviembre=tk.DoubleVar(value=4.368)
entradaIrradianciaNoviembre=tk.Entry(ventanaGen, textvariable=valorIrradianciaNoviembre, bg='khaki1')
entradaIrradianciaNoviembre.place(x=337, y=315,height=18, width=60)

irradianciaDiciembre=tk.Label(ventanaGen, text='Digite la irradiancia mes de diciembre (kW/m2)', font=('Consolas',10), justify='left', bg='light slate blue')
irradianciaDiciembre.place(x=5, y=340,height=18)
valorIrradianciaDiciembre=tk.DoubleVar(value=5.578)
entradaIrradianciaDiciembre=tk.Entry(ventanaGen, textvariable=valorIrradianciaDiciembre, bg='khaki1')
entradaIrradianciaDiciembre.place(x=337, y=340,height=18, width=60)

botonPotenciaOPT=tk.Button(ventanaGen,text='Calcular potencia óptima para el consumo digitado', font=('Consolas',10), justify='center', command=mostrarPotenciaOPT, width=60, bg='cornflower blue')
botonPotenciaOPT.place(x=5,y=370)

resultado_potenciaOPT=tk.Label(ventanaGen,text='',font=('Consolas',10), bg='CadetBlue1')
resultado_potenciaOPT.place(x=450, y=370)

subtituloVenGen_dos=tk.Label(ventanaGen, text='Demanda Cliente', font=('Consolas',13,'bold'), justify='center', bg='DeepSkyBlue2', fg='light cyan')
subtituloVenGen_dos.place(x=450,y=38)

demandaEnero=tk.Label(ventanaGen, text='Digite la demanda del mes de enero (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaEnero.place(x=450, y=65,height=18)
valorDemandaEnero=tk.DoubleVar(value=70150)
entradaDemandaEnero=tk.Entry(ventanaGen, textvariable=valorDemandaEnero, bg='khaki1')
entradaDemandaEnero.place(x=805, y=65,height=18, width=60)

demandaFebrero=tk.Label(ventanaGen, text='Digite la demanda del mes de febrero (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaFebrero.place(x=450, y=90,height=18)
valorDemandaFebrero=tk.DoubleVar(value=10600)
entradaDemandaFebrero=tk.Entry(ventanaGen, textvariable=valorDemandaFebrero, bg='khaki1')
entradaDemandaFebrero.place(x=805, y=90,height=18, width=60)

demandaMarzo=tk.Label(ventanaGen, text='Digite la demanda del mes de marzo (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaMarzo.place(x=450, y=115,height=18)
valorDemandaMarzo=tk.DoubleVar(value=22605)
entradaDemandaMarzo=tk.Entry(ventanaGen, textvariable=valorDemandaMarzo, bg='khaki1')
entradaDemandaMarzo.place(x=805, y=115,height=18, width=60)

demandaAbril=tk.Label(ventanaGen, text='Digite la demanda del mes de abril (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaAbril.place(x=450, y=140,height=18)
valorDemandaAbril=tk.DoubleVar(value=35950)
entradaDemandaAbril=tk.Entry(ventanaGen, textvariable=valorDemandaAbril, bg='khaki1')
entradaDemandaAbril.place(x=805, y=140,height=18, width=60)

demandaMayo=tk.Label(ventanaGen, text='Digite la demanda del mes de mayo (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaMayo.place(x=450, y=165,height=18)
valorDemandaMayo=tk.DoubleVar(value=0)
entradaDemandaMayo=tk.Entry(ventanaGen, textvariable=valorDemandaMayo, bg='khaki1')
entradaDemandaMayo.place(x=805, y=165,height=18, width=60)

demandaJunio=tk.Label(ventanaGen, text='Digite la demanda del mes de junio (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaJunio.place(x=450, y=190,height=18)
valorDemandaJunio=tk.DoubleVar(value=0)
entradaDemandaJunio=tk.Entry(ventanaGen, textvariable=valorDemandaJunio, bg='khaki1')
entradaDemandaJunio.place(x=805, y=190,height=18, width=60)

demandaJulio=tk.Label(ventanaGen, text='Digite la demanda del mes de julio (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaJulio.place(x=450, y=215,height=18)
valorDemandaJulio=tk.DoubleVar(value=13950)
entradaDemandaJulio=tk.Entry(ventanaGen, textvariable=valorDemandaJulio, bg='khaki1')
entradaDemandaJulio.place(x=805, y=215,height=18, width=60)

demandaAgosto=tk.Label(ventanaGen, text='Digite la demanda del mes de agosto (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaAgosto.place(x=450, y=240,height=18)
valorDemandaAgosto=tk.DoubleVar(value=31300)
entradaDemandaAgosto=tk.Entry(ventanaGen, textvariable=valorDemandaAgosto, bg='khaki1')
entradaDemandaAgosto.place(x=805, y=240,height=18, width=60)

demandaSeptiembre=tk.Label(ventanaGen, text='Digite la demanda del mes de septiembre (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaSeptiembre.place(x=450, y=265,height=18)
valorDemandaSeptiembre=tk.DoubleVar(value=24100)
entradaDemandaSeptiembre=tk.Entry(ventanaGen, textvariable=valorDemandaSeptiembre, bg='khaki1')
entradaDemandaSeptiembre.place(x=805, y=265,height=18, width=60)

demandaOctubre=tk.Label(ventanaGen, text='Digite la demanda del mes de octubre (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaOctubre.place(x=450, y=290,height=18)
valorDemandaOctubre=tk.DoubleVar(value=36910)
entradaDemandaOctubre=tk.Entry(ventanaGen, textvariable=valorDemandaOctubre, bg='khaki1')
entradaDemandaOctubre.place(x=805, y=290,height=18, width=60)

demandaNoviembre=tk.Label(ventanaGen, text='Digite la demanda del mes de noviembre (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaNoviembre.place(x=450, y=315,height=18)
valorDemandaNoviembre=tk.DoubleVar(value=14400)
entradaDemandaNoviembre=tk.Entry(ventanaGen, textvariable=valorDemandaNoviembre, bg='khaki1')
entradaDemandaNoviembre.place(x=805, y=315,height=18, width=60)

demandaDiciembre=tk.Label(ventanaGen, text='Digite la demanda del mes de diciembre (kWh-mes)', font=('Consolas',10), justify='left', bg='light slate blue')
demandaDiciembre.place(x=450, y=340,height=18)
valorDemandaDiciembre=tk.DoubleVar(value=22100)
entradaDemandaDiciembre=tk.Entry(ventanaGen, textvariable=valorDemandaDiciembre, bg='khaki1')
entradaDemandaDiciembre.place(x=805, y=340,height=18, width=60)


#AutoconsumoUsuario
autoconsumo=tk.Label(ventanaDI, text='Digite el autoconsumo del usuario (kWh-año)', font=('Consolas',10), justify='left')
autoconsumo.place(x=5, y=79,height=18)
valorAutoconsumo=tk.DoubleVar(value=209000)
entradaAutoconsumo=tk.Entry(ventanaDI, textvariable=valorAutoconsumo)
entradaAutoconsumo.place(x=460, y=79,height=18)
#DemandaUsuario
demanda=tk.Label(ventanaDI, text='Digite la demanda del cliente (kWh-año)', font=('Consolas',10), justify='left')
demanda.place(x=5, y=101, height=18)
valorDemanda=tk.DoubleVar(value=209000)
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

distanciaLCDig=tk.Label(ventanaDI,text='Prefiere digitar la distancia en metros', font=('Consolas',10),justify='left', bg='light blue')
distanciaLCDig.place(x=600,y=145,height=18)

valorLCDig=tk.IntVar() #Guarda la respuesta
opcion_1Dig=tk.Radiobutton(ventanaDI,text='Sí',font=('Consolas',10),value=1,variable=valorLCDig, command=mostrarEntrada)
opcion_1Dig.place(x=885,y=145,height=18)
opcion_2Dig=tk.Radiobutton(ventanaDI,text='No',font=('Consolas',10),value=0,variable=valorLCDig, command=mostrarEntrada)
opcion_2Dig.place(x=935,y=145,height=18)

distanciaDig=tk.DoubleVar(value=0)
entradaDistanciaDig=tk.Entry(ventanaDI, textvariable=distanciaDig)


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
subtituloImpuestos=tk.Label(ventanaDI, text='Desea modificar variables asociadas a los impuestos y la depreciación', font=('Consolas',11), justify='center', bg='light blue')
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

#Label de ir a ventana capex
subtituloVenCapex=tk.Label(ventanaDI, text='Desea modificar variables asociadas al capex del proyecto', font=('Consolas',11), justify='center', bg='light blue')
subtituloVenCapex.place(x=5,y=353)
#Botón de ir a ventana de capex
botonIrVentanaCapex=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaCapex,width=8)
botonIrVentanaCapex.place(x=720,y=353)


reporteEx=tk.Label(ventanaDI,text='¿Desea usar el reporte de excel existente?', font=('Consolas',10),justify='left')
reporteEx.place(x=5,y=382,height=18)
valorReporteEx=tk.IntVar() #Guarda la respuesta
opcion_1Ex=tk.Radiobutton(ventanaDI,text='Sí',font=('Consolas',10),value=1,variable=valorReporteEx)
opcion_1Ex.place(x=330,y=382,height=18)
opcion_2Ex=tk.Radiobutton(ventanaDI,text='No',font=('Consolas',10),value=0,variable=valorReporteEx)
opcion_2Ex.place(x=380,y=382,height=18)


#Label de generar reporte en excel
subtituloReporte=tk.Label(ventanaDI, text='¿Desea generar reporte en excel?', font=('Consolas',12), justify='center', bg='pale green')
subtituloReporte.place(x=100,y=410)
#Botón de generar reporte en excel
botonReporte=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=contadorExcel, width=8)
botonReporte.place(x=410,y=410)
ReporteLabel=tk.Label(ventanaDI,text='Número de veces que se ha generado el reporte: 0', font=('Consolas',10),justify='left')
ReporteLabel.place(x=480,y=410,height=20)

subtituloEconomic=tk.Label(ventanaDI, text='¿Desea abrir ventana con resumen financiero?', font=('Consolas',12), justify='center', bg='pale green')
subtituloEconomic.place(x=5,y=450)
#Botón de generar reporte en excel
botonEconomic=tk.Button(ventanaDI,text='Sí', font=('Consolas',10), justify='center', command=mostrarVentanaEC, width=8)
botonEconomic.place(x=410,y=450)

botonVenEconomic=tk.Button(ventanaEC,text='Ocultar ventana', font=('Consolas',11), justify='center', command=ocultarVentanaEC, width=20)
botonVenEconomic.place(x=5,y=550)

cambioEntrada=tk.Label(ventanaDI, text='Digite el cambio que realizó para la comparación', font=('Consolas',10), justify='center', bg='light blue')
cambioEntrada.place(x=5,y=485, height=27)
valorCambioEntrada=tk.StringVar()
entradaValorCambioEntrada=tk.Entry(ventanaDI, textvariable=valorCambioEntrada, bg='pale green')
entradaValorCambioEntrada.place(x=350,y=485, height=27,width=300)

botonConductorOPT=tk.Button(ventanaDI,text='Calcular distancia \n crítica del proyecto', font=('Consolas',10), justify='center', command=mostrarConductorOPT, width=30, bg='cornflower blue')
botonConductorOPT.place(x=5,y=520)

resultado_conductorOPT=tk.Label(ventanaDI,text='',font=('Consolas',10), bg='CadetBlue1')
resultado_conductorOPT.place(x=230, y=525)

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
#valorTarifaEnergiaRed.bind("<Return>", convertir_formato_contable)

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
opcion_1=tk.Radiobutton(ventanaImpuestos,text='Sí',font=('Consolas',10),value=0,variable=impuestos)
opcion_1.place(x=460,y=250,height=18)
opcion_2=tk.Radiobutton(ventanaImpuestos,text='No',font=('Consolas',10),value=1,variable=impuestos)
opcion_2.place(x=510,y=250,height=18)

#Tasa de impuesto sobre la renta
tasaImpuestoRenta=tk.Label(ventanaImpuestos,text='Tasa de impuesto sobre la renta (%)', font=('Consolas',10),justify='left')
tasaImpuestoRenta.place(x=5,y=278,height=18)
valorImpuestoSobreRenta=tk.DoubleVar(value=35)
entradaValorImpuestoRenta=tk.Entry(ventanaImpuestos,textvariable=valorImpuestoSobreRenta, bg='orange2')
entradaValorImpuestoRenta.place(x=460,y=278, height=18)

#Tasa de impuesto local
tasaImpuestoLocal=tk.Label(ventanaImpuestos,text='Tasa de impuesto local (%)', font=('Consolas',10),justify='left')
tasaImpuestoLocal.place(x=5,y=302,height=18)
valorImpuestoLocal=tk.DoubleVar(value=0)
entradaValorImpuestoLocal=tk.Entry(ventanaImpuestos,textvariable=valorImpuestoLocal, bg='orange2')
entradaValorImpuestoLocal.place(x=460,y=302, height=18)

#Impuesto de renta
impuestoRenta=tk.Label(ventanaImpuestos,text='Impuesto de renta (%)', font=('Consolas',10),justify='left')
impuestoRenta.place(x=5,y=326,height=18)
valorImpuestoRenta=tk.DoubleVar(value=32)
entradaValorImpuestoRenta=tk.Entry(ventanaImpuestos,textvariable=valorImpuestoRenta, bg='orange2')
entradaValorImpuestoRenta.place(x=460,y=326, height=18)

#Descuento sobre la base gravable del valor invertido (ley 1715)
baseGravable=tk.Label(ventanaImpuestos,text='Descuento sobre la base gravable del valor invertido(%)', font=('Consolas',10),justify='left')
baseGravable.place(x=5,y=350,height=18)
valorBaseGravable=tk.DoubleVar(value=50)
entradaValorBaseGravable=tk.Entry(ventanaImpuestos,textvariable=valorBaseGravable, bg='orange2')
entradaValorBaseGravable.place(x=460,y=350, height=18)

#Maximo % sobre Capex a descontar de la renta liquida
maxDesCapex=tk.Label(ventanaImpuestos,text='Máximo % sobre capex a descontar de la renta liquida(%)', font=('Consolas',10),justify='left')
maxDesCapex.place(x=5,y=374,height=18)
valorMaxDesCapex=tk.DoubleVar(value=50)
entradaValorMaxDesCapex=tk.Entry(ventanaImpuestos,textvariable=valorMaxDesCapex, bg='orange2')
entradaValorMaxDesCapex.place(x=460,y=374, height=18)

#Tipo de depreciación
depreciacion_label=tk.Label(ventanaImpuestos,text='Tipo de depreciación deseada', font=('Consolas',10),justify='left')
depreciacion_label.place(x=5,y=398,height=18)
depreciacion=tk.IntVar() #Guarda la respuesta
opcion_1=tk.Radiobutton(ventanaImpuestos,text='Lineal',font=('Consolas',10),value=0,variable=depreciacion)
opcion_1.place(x=460,y=398,height=18, width=70)
opcion_2=tk.Radiobutton(ventanaImpuestos,text='Acelerada',font=('Consolas',10),value=1,variable=depreciacion)
opcion_2.place(x=540,y=398,height=18, width=95) 

#Tasa de depreciación acelerada
tasaDepreciacionAc=tk.Label(ventanaImpuestos,text='Tasa de depreciación acelerada (%)', font=('Consolas',10),justify='left')
tasaDepreciacionAc.place(x=5,y=422,height=18)
valorTasaDepreciacionAc=tk.DoubleVar(value=40)
entradaValorTasaDepreciacionAc=tk.Entry(ventanaImpuestos,textvariable=valorTasaDepreciacionAc, bg='orange2')
entradaValorTasaDepreciacionAc.place(x=460,y=422, height=18)

#Años para depreciación lineal
tiempoDepreciacionLn=tk.Label(ventanaImpuestos,text='Años para depreciación lineal (años)', font=('Consolas',10),justify='left')
tiempoDepreciacionLn.place(x=5,y=446,height=18)
valorTiempoDepreciacionLn=tk.DoubleVar(value=20)
entradaValorTiempoDepreciacionLn=tk.Entry(ventanaImpuestos,textvariable=valorTiempoDepreciacionLn, bg='orange2')
entradaValorTiempoDepreciacionLn.place(x=460,y=446, height=18)

#Tasa de depreciacion lineal
tasaDepreciacionLn=tk.Label(ventanaImpuestos,text='Tasa de depreciación lineal (%)', font=('Consolas',10),justify='left')
tasaDepreciacionLn.place(x=5,y=470,height=18)
valorTasaDepreciacionLn=tk.DoubleVar(value=5)
entradaValorTasaDepreciacionLn=tk.Entry(ventanaImpuestos,textvariable=valorTasaDepreciacionLn, bg='orange2')
entradaValorTasaDepreciacionLn.place(x=460,y=470, height=18)



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


"""Características ventana energética"""
ventanaCapex=tk.Toplevel()
ventanaCapex.title("Análisis financiero proyectos Energía Renovable")
ventanaCapex.geometry('1000x700')
ventanaCapex.configure(background='#004292')

botonIrVentanaDICap=tk.Button(ventanaCapex,text='Regresar', font=('Consolas',10), justify='center', command=mostrarVentanaDI_Capex, width=8)
botonIrVentanaDICap.place(x=5,y=650)

subtituloVenCapex=tk.Label(ventanaCapex, text='Equipos de generación', font=('Consolas',13,'bold'), justify='center', bg='DeepSkyBlue2', fg='light cyan')
subtituloVenCapex.place(x=5,y=5)

costoPaneles=tk.Label(ventanaCapex,text='Costo de paneles solares (COP/MW)', font=('Consolas',10),justify='left')
costoPaneles.place(x=5,y=35,height=18)
valorCostoPaneles=tk.DoubleVar(value=1401620000)
entradaValorCostoPaneles=tk.Entry(ventanaCapex,textvariable=valorCostoPaneles,bg='orange2')
entradaValorCostoPaneles.place(x=350,y=35, height=18)

costoInversores=tk.Label(ventanaCapex,text='Costo de inversores (COP/MW)', font=('Consolas',10),justify='left')
costoInversores.place(x=5,y=60,height=18)
valorCostoInversores=tk.DoubleVar(value=69333333.3333333)
entradaValorCostoInversores=tk.Entry(ventanaCapex,textvariable=valorCostoInversores,bg='orange2')
entradaValorCostoInversores.place(x=350,y=60, height=18)

subtituloVenCapex_dos=tk.Label(ventanaCapex, text='BOS', font=('Consolas',13,'bold'), justify='center', bg='DeepSkyBlue2', fg='light cyan')
subtituloVenCapex_dos.place(x=5,y=85)

costoCableadoDC=tk.Label(ventanaCapex,text='Costo cableado DC (COP/MW)', font=('Consolas',10),justify='left')
costoCableadoDC.place(x=5,y=113,height=18)
valorCostoCableadoDC=tk.DoubleVar(value=133333333.333333)
entradaValorCostoCableadoDC=tk.Entry(ventanaCapex,textvariable=valorCostoCableadoDC,bg='orange2')
entradaValorCostoCableadoDC.place(x=350,y=113, height=18)

costoCableadoAC=tk.Label(ventanaCapex,text='Costo cableado AC (COP/MW)', font=('Consolas',10),justify='left')
costoCableadoAC.place(x=5,y=138,height=18)
valorCostoCableadoAC=tk.DoubleVar(value=150000000)
entradaValorCostoCableadoAC=tk.Entry(ventanaCapex,textvariable=valorCostoCableadoAC,bg='orange2')
entradaValorCostoCableadoAC.place(x=350,y=138, height=18)

costoSistemaMonitoreo=tk.Label(ventanaCapex,text='Costo sistema monitoreo (COP/MW)', font=('Consolas',10),justify='left')
costoSistemaMonitoreo.place(x=5,y=138,height=18)
valorCostoSistemaMonitoreo=tk.DoubleVar(value=4666666.66666667)
entradaValorCostoSistemaMonitoreo=tk.Entry(ventanaCapex,textvariable=valorCostoSistemaMonitoreo,bg='orange2')
entradaValorCostoSistemaMonitoreo.place(x=350,y=138, height=18)

costoTuberia=tk.Label(ventanaCapex,text='Costo tuberia y/o accesorios (COP/MW)', font=('Consolas',10),justify='left')
costoTuberia.place(x=5,y=163,height=18)
valorCostoTuberia=tk.DoubleVar(value=116666666.666667)
entradaValorCostoTuberia=tk.Entry(ventanaCapex,textvariable=valorCostoTuberia,bg='orange2')
entradaValorCostoTuberia.place(x=350,y=163, height=18)

costoCerramiento=tk.Label(ventanaCapex,text='Costo cerramiento (malla eslabonada) (COP/MW)', font=('Consolas',10),justify='left')
costoCerramiento.place(x=5,y=188,height=18)
valorCostoCerramiento=tk.DoubleVar(value=66666666.6666667)
entradaValorCostoCerramiento=tk.Entry(ventanaCapex,textvariable=valorCostoCerramiento,bg='orange2')
entradaValorCostoCerramiento.place(x=350,y=188, height=18)

costoSPT=tk.Label(ventanaCapex,text='Costo Sistema de puesta  a tierra (COP/MW)', font=('Consolas',10),justify='left')
costoSPT.place(x=5,y=213,height=18)
valorCostoSPT=tk.DoubleVar(value=100000000)
entradaValorCostoSPT=tk.Entry(ventanaCapex,textvariable=valorCostoSPT,bg='orange2')
entradaValorCostoSPT.place(x=350,y=213, height=18)

costoOtros=tk.Label(ventanaCapex,text='Costo otros materiales (COP/MW)', font=('Consolas',10),justify='left')
costoOtros.place(x=5,y=238,height=18)
valorCostoOtros=tk.DoubleVar(value=166666666.666667)
entradaValorCostoOtros=tk.Entry(ventanaCapex,textvariable=valorCostoOtros,bg='orange2')
entradaValorCostoOtros.place(x=350,y=238, height=18)

costoMaquinaria=tk.Label(ventanaCapex,text='Costo alquiler maquinaría (COP/MW)', font=('Consolas',10),justify='left')
costoMaquinaria.place(x=5,y=238,height=18)
valorCostoMaquinaria=tk.DoubleVar(value=93333333.3333333)
entradaValorCostoMaquinaria=tk.Entry(ventanaCapex,textvariable=valorCostoMaquinaria,bg='orange2')
entradaValorCostoMaquinaria.place(x=350,y=238, height=18)

costoInstalacion=tk.Label(ventanaCapex,text='Costo instalación (COP/MW)', font=('Consolas',10),justify='left')
costoInstalacion.place(x=5,y=263,height=18)
valorCostoInstalacion=tk.DoubleVar(value=300000000)
entradaValorCostoInstalacion=tk.Entry(ventanaCapex,textvariable=valorCostoInstalacion,bg='orange2')
entradaValorCostoInstalacion.place(x=350,y=263, height=18)

costoImprevistos=tk.Label(ventanaCapex,text='Monto imprevistos (COP/MW)', font=('Consolas',10),justify='left')
costoImprevistos.place(x=5,y=288,height=18)
valorCostoImprevistos=tk.DoubleVar(value=133333333.333333)
entradaValorCostoImprevistos=tk.Entry(ventanaCapex,textvariable=valorCostoImprevistos,bg='orange2')
entradaValorCostoImprevistos.place(x=350,y=288, height=18)

costoIngenieria=tk.Label(ventanaCapex,text='Costo ingeniería de detalle (COP/MW)', font=('Consolas',10),justify='left')
costoIngenieria.place(x=5,y=313,height=18)
valorCostoIngenieria=tk.DoubleVar(value=60000000)
entradaValorCostoIngenieria=tk.Entry(ventanaCapex,textvariable=valorCostoIngenieria,bg='orange2')
entradaValorCostoIngenieria.place(x=350,y=313, height=18)

costoEstSuelos=tk.Label(ventanaCapex,text='Costo estudio de suelos (COP/MW)', font=('Consolas',10),justify='left')
costoEstSuelos.place(x=5,y=338,height=18)
valorCostoEstSuelos=tk.DoubleVar(value=6666666.66666667)
entradaValorCostoEstSuelos=tk.Entry(ventanaCapex,textvariable=valorCostoEstSuelos,bg='orange2')
entradaValorCostoEstSuelos.place(x=350,y=338, height=18)

costoResistividad=tk.Label(ventanaCapex,text='Costo estudio de resistividad (COP/MW)', font=('Consolas',10),justify='left')
costoResistividad.place(x=5,y=363,height=18)
valorCostoResistividad=tk.DoubleVar(value=16666666.6666667)
entradaValorCostoResistividad=tk.Entry(ventanaCapex,textvariable=valorCostoResistividad,bg='orange2')
entradaValorCostoResistividad.place(x=350,y=363, height=18)

costoEstTopografico=tk.Label(ventanaCapex,text='Costo estudios topograficos (COP/MW)', font=('Consolas',10),justify='left')
costoEstTopografico.place(x=5,y=388,height=18)
valorCostoEstTopografico=tk.DoubleVar(value=6666666.66666667)
entradaValorCostoTopografico=tk.Entry(ventanaCapex,textvariable=valorCostoEstTopografico,bg='orange2')
entradaValorCostoTopografico.place(x=350,y=388, height=18)

costoPruebas=tk.Label(ventanaCapex,text='Costo pruebas (medición variables) (COP/MW)', font=('Consolas',10),justify='left')
costoPruebas.place(x=5,y=413,height=18)
valorCostoPruebas=tk.DoubleVar(value=5000000)
entradaValorCostoPruebas=tk.Entry(ventanaCapex,textvariable=valorCostoPruebas,bg='orange2')
entradaValorCostoPruebas.place(x=350,y=413, height=18)

costoCampamento=tk.Label(ventanaCapex,text='Costo campamento (COP/MW)', font=('Consolas',10),justify='left')
costoCampamento.place(x=5,y=438,height=18)
valorCostoCampamento=tk.DoubleVar(value=33333333.3333333)
entradaValorCostoCampamento=tk.Entry(ventanaCapex,textvariable=valorCostoCampamento,bg='orange2')
entradaValorCostoCampamento.place(x=350,y=438, height=18)

costoSPDA=tk.Label(ventanaCapex,text='Costo Apantallamiento (SPDA) (COP/MW)', font=('Consolas',10),justify='left')
costoSPDA.place(x=5,y=463,height=18)
valorCostoSPDA=tk.DoubleVar(value=60000000)
entradaValorCostoSPDA=tk.Entry(ventanaCapex,textvariable=valorCostoSPDA,bg='orange2')
entradaValorCostoSPDA.place(x=350,y=463, height=18)

subtituloVenCapex_tres=tk.Label(ventanaCapex, text='Interconexión', font=('Consolas',13,'bold'), justify='center', bg='DeepSkyBlue2', fg='light cyan')
subtituloVenCapex_tres.place(x=5,y=488)

costoTransformador=tk.Label(ventanaCapex,text='Costo transformador (COP/MW)', font=('Consolas',10),justify='left')
costoTransformador.place(x=5,y=516,height=18)
valorCostoTransformador=tk.DoubleVar(value=83333333.3333333)
entradaValorCostoTransformador=tk.Entry(ventanaCapex,textvariable=valorCostoTransformador,bg='orange2')
entradaValorCostoTransformador.place(x=350,y=516, height=18)

costoProtecciones=tk.Label(ventanaCapex,text='Costo Protecciones (COP/MW)', font=('Consolas',10),justify='left')
costoProtecciones.place(x=5,y=541,height=18)
valorCostoProtecciones=tk.DoubleVar(value=31666666.6666667)
entradaValorCostoProtecciones=tk.Entry(ventanaCapex,textvariable=valorCostoProtecciones,bg='orange2')
entradaValorCostoProtecciones.place(x=350,y=541, height=18)

costoMedidores=tk.Label(ventanaCapex,text='Costo Medidor bidireccional (COP/MW)', font=('Consolas',10),justify='left')
costoMedidores.place(x=5,y=566,height=18)
valorCostoMedidores=tk.DoubleVar(value=5000000)
entradaValorCostoMedidores=tk.Entry(ventanaCapex,textvariable=valorCostoMedidores,bg='orange2')
entradaValorCostoMedidores.place(x=350,y=566, height=18)




ocultarVentana(ventanaEnergetica)
ocultarVentana(ventanaImpuestos)
ocultarVentana(ventanaFinan)
ocultarVentana(ventanaOyM)
ocultarVentana(ventanaDI)
ocultarVentana(ventanaEC)
ocultarVentana(ventanaCapex)
ocultarVentana(ventanaGen)



ventana.mainloop()





