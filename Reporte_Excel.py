import matplotlib.pyplot as plt


discretizacionConsumo={
    "0-1": 0.001373216,
    "1-2": 0.001432921,
    "2-3": 0.001373216,
    "3-4": 0.001432921,
    "4-5": 0.001492626,
    "5-6": 0.001373216,
    "6-7": 0.001343364,
    "7-8": 0.001361275,
    "8-9": 0.001373216,
    "9-10": 0.001313511,
    "10-11": 0.001313511,
    "11-12": 0.001432921,
    "12-13": 0.001492626,
    "13-14": 0.001373216,
    "14-15": 0.001462774,
    "15-16": 0.001492626,
    "16-17": 0.001432921,
    "17-18": 0.001373216,
    "18-19": 0.001313511,
    "19-20": 0.001253806,
    "20-21": 0.001373216,
    "21-22": 0.001343364,
    "22-23": 0.001313511,
    "23-24": 0.001492626,
    }

discretizacion={
    "0-1": 0,
    "1-2": 0,
    "2-3": 0,
    "3-4": 0,
    "4-5": 0,
    "5-6": 0,
    "6-7": 0.028043272,
    "7-8": 0.056714993,
    "8-9": 0.077689734,
    "9-10": 0.092846792,
    "10-11": 0.108467785,
    "11-12": 0.11995363,
    "12-13": 0.120695205,
    "13-14": 0.11542733,
    "14-15": 0.104249698,
    "15-16": 0.08899897,
    "16-17": 0.065415597,
    "17-18": 0.02096693,
    "18-19": 0,
    "19-20": 0,
    "20-21": 0,
    "21-22": 0,
    "22-23": 0,
    "23-24": 0,    
}

def CalculoEnergia(demanda,Irradiancia, capacidad):
    
    irradiancia={
        "Enero": Irradiancia[0],
        "Febrero": Irradiancia[1],
        "Marzo": Irradiancia[2],
        "Abril": Irradiancia[3],
        "Mayo": Irradiancia[4],
        "Junio": Irradiancia[5],
        "Julio": Irradiancia[6],
        "Agosto": Irradiancia[7],
        "Septiembre": Irradiancia[8],
        "Octubre": Irradiancia[9],
        "Noviembre": Irradiancia[10],
        "Diciembre": Irradiancia[11],
        }
    
    consumo={
        "Enero": demanda[0],
        "Febrero": demanda[1],
        "Marzo": demanda[2],
        "Abril": demanda[3],
        "Mayo": demanda[4],
        "Junio": demanda[5],
        "Julio": demanda[6],
        "Agosto": demanda[7],
        "Septiembre": demanda[8],
        "Octubre": demanda[9],
        "Noviembre": demanda[10],
        "Diciembre": demanda[11],
       }
        
    
    generacionDia={}
    CapacidadDC=capacidad*1.2*1000000
    Potencia_panel=605
    Cantidad_paneles=CapacidadDC/Potencia_panel
    generacion={}
    listaAux=list(discretizacion.values())
    listaAuxDos=list(discretizacionConsumo.values())
    listaGenEnero=[]
    listaDemEnero=[]
    generacionDiaList=[]
    consumoDiaList=[]
    EnergiaExportada={}
    EnergiaConsumida={}
    EnergiaImportada={}
    EnergiaExportadaList=[]
    EnergiaConsumidaList=[]
    EnergiaImportadaList=[]
    EnergiaExportadaTotal=[]
    EnergiaImportadaTotal=[]
    EnergiaConsumidaTotal=[]
    consumoUsuarioTotal=[]
    consumoUsuario={}
    generacionDiaTotal=[]
    
    for clave in irradiancia:
        generacion[clave]=(irradiancia[clave]*Cantidad_paneles*Potencia_panel/1000)*30
        for i in range(0,len(listaAux)):
            generacionDiaList.append(listaAux[i]*irradiancia[clave]*Cantidad_paneles*Potencia_panel/1000)
            consumoDiaList.append(listaAuxDos[i]*consumo[clave])
            if generacionDiaList[i]>consumoDiaList[i]:
                EnergiaExportadaList.append(generacionDiaList[i]-consumoDiaList[i])
                EnergiaConsumidaList.append(consumoDiaList[i])  
                EnergiaImportadaList.append(0)
            elif generacionDiaList[i]<consumoDiaList[i]:
                EnergiaExportadaList.append(0)
                EnergiaConsumidaList.append(generacionDiaList[i])
                EnergiaImportadaList.append(consumoDiaList[i]-generacionDiaList[i])
            if clave=='Enero': #and j==1:
                listaGenEnero.append(listaAux[i]*irradiancia[clave]*Cantidad_paneles*Potencia_panel/1000)
                listaDemEnero.append(listaAuxDos[i]*consumo[clave])
                
            
        generacionDia[clave]=generacionDiaList
        EnergiaExportada[clave]=EnergiaExportadaList
        EnergiaConsumida[clave]=EnergiaConsumidaList
        EnergiaImportada[clave]=EnergiaImportadaList
        consumoUsuario[clave]=consumoDiaList
        consumoUsuarioTotal.append(sum(consumoDiaList)*30)
        EnergiaExportadaTotal.append(sum(EnergiaExportadaList)*30)
        EnergiaImportadaTotal.append(sum(EnergiaImportadaList)*30)
        EnergiaConsumidaTotal.append(sum(EnergiaConsumidaList)*30)
        generacionDiaTotal.append(sum(generacionDiaList)*30)
        generacionDiaList=[]
        EnergiaExportadaList=[]
        EnergiaConsumidaList=[]
        EnergiaImportadaList=[]
        consumoDiaList=[]
        
    
    
    EnergiaExportadaTotal=sum(EnergiaExportadaTotal)
    EnergiaImportadaTotal=sum(EnergiaImportadaTotal)
    EnergiaConsumidaTotal=sum(EnergiaConsumidaTotal)
    generacionDiaTotal=sum(generacionDiaTotal)
    
    
    hora=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    plt.plot(hora,listaGenEnero)
    plt.plot(hora,listaDemEnero)
    plt.xlabel('Hora')
    plt.ylabel('Irradiancia')
    plt.title('Generación Junio')
    
    
    plt.show()

    
    return EnergiaExportadaTotal, EnergiaImportadaTotal, EnergiaConsumidaTotal, generacionDiaTotal

def potenciaOptima(demanda, Irradiancia):
    
    irradiancia={
        "Enero": Irradiancia[0],
        "Febrero": Irradiancia[1],
        "Marzo": Irradiancia[2],
        "Abril": Irradiancia[3],
        "Mayo": Irradiancia[4],
        "Junio": Irradiancia[5],
        "Julio": Irradiancia[6],
        "Agosto": Irradiancia[7],
        "Septiembre": Irradiancia[8],
        "Octubre": Irradiancia[9],
        "Noviembre": Irradiancia[10],
        "Diciembre": Irradiancia[11],
        }
    
    consumo={
        "Enero": demanda[0],
        "Febrero": demanda[1],
        "Marzo": demanda[2],
        "Abril": demanda[3],
        "Mayo": demanda[4],
        "Junio": demanda[5],
        "Julio": demanda[6],
        "Agosto": demanda[7],
        "Septiembre": demanda[8],
        "Octubre": demanda[9],
        "Noviembre": demanda[10],
        "Diciembre": demanda[11],
       }

    CantidadPaneles=100
    PotenciaPanel=605
    PotenciaDC=CantidadPaneles*PotenciaPanel/1000
    generacionDia={}
    generacion={}
    listaAux=list(discretizacion.values())
    listaAuxDos=list(discretizacionConsumo.values())
    generacionDiaList=[]
    consumoDiaList=[]
    EnergiaExportada={}
    EnergiaConsumida={}
    EnergiaImportada={}
    EnergiaExportadaList=[]
    EnergiaConsumidaList=[]
    EnergiaImportadaList=[]
    EnergiaExportadaTotal=[]
    EnergiaImportadaTotal=[]
    EnergiaConsumidaTotal=[]
    consumoUsuarioTotal=[]
    consumoUsuario={}
    generacionDiaTotal=[]
    EnergiaExportadaTotal_dos=0
    EnergiaImportadaTotal_dos=0
    EnergiaConsumidaTotal_dos=0
    generacionDiaTotal_dos=0
    variable=False
    iterador=0
    
    while variable==False:
        for clave in irradiancia:
            for i in range(0,len(listaAux)):
                generacionDiaList.append(listaAux[i]*irradiancia[clave]*CantidadPaneles*PotenciaPanel/1000)
                consumoDiaList.append(listaAuxDos[i]*consumo[clave])
                if generacionDiaList[i]>consumoDiaList[i]:
                    EnergiaExportadaList.append(generacionDiaList[i]-consumoDiaList[i])
                    EnergiaConsumidaList.append(consumoDiaList[i])  
                    EnergiaImportadaList.append(0)
                elif generacionDiaList[i]<consumoDiaList[i]:
                    EnergiaExportadaList.append(0)
                    EnergiaConsumidaList.append(generacionDiaList[i])
                    EnergiaImportadaList.append(consumoDiaList[i]-generacionDiaList[i])
        
            generacionDia[clave]=generacionDiaList
            EnergiaExportada[clave]=EnergiaExportadaList
            EnergiaConsumida[clave]=EnergiaConsumidaList
            EnergiaImportada[clave]=EnergiaImportadaList
            consumoUsuario[clave]=consumoDiaList
            consumoUsuarioTotal.append(sum(consumoDiaList)*30)
            EnergiaExportadaTotal.append(sum(EnergiaExportadaList)*30)
            EnergiaImportadaTotal.append(sum(EnergiaImportadaList)*30)
            EnergiaConsumidaTotal.append(sum(EnergiaConsumidaList)*30)
            generacionDiaTotal.append(sum(generacionDiaList)*30)
            generacionDiaList=[]
            EnergiaExportadaList=[]
            EnergiaConsumidaList=[]
            EnergiaImportadaList=[]
            consumoDiaList=[]
                    
        EnergiaExportadaTotal_dos=sum(EnergiaExportadaTotal)
        EnergiaImportadaTotal_dos=sum(EnergiaImportadaTotal)
        EnergiaConsumidaTotal_dos=sum(EnergiaConsumidaTotal)
        generacionDiaTotal_dos=sum(generacionDiaTotal)
        
        
        if EnergiaExportadaTotal_dos-EnergiaImportadaTotal_dos>0:
            variable=True
        else:
            CantidadPaneles+=1
            iterador+=1
        EnergiaExportadaTotal=[]
        EnergiaImportadaTotal=[]
        EnergiaConsumidaTotal=[]
        generacionDiaTotal=[]
       
    print(CantidadPaneles)
    print(iterador)
    print(CantidadPaneles*PotenciaPanel/1000)
    string=str(CantidadPaneles*PotenciaPanel/1000)+str(" ")+str("kWp")+str("\nEl proceso se realizo en "+str(iterador)+str(" iteraciones"))
    return string
    
    
demanda=[70150,10600,22605,35950,0,0,13950,31300,24100,36910,14400,22100]
Irradiancia=[6.14,5.33,3.705,3.144,3.463,3.3,3.349,3.421,3.917,4.002,4.368,5.578]

print(potenciaOptima(demanda, Irradiancia))
    
    