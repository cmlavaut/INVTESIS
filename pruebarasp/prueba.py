import serial
import time
import sys
import os
import pandas as pd
from datetime import datetime

#path = '/home/pi/Invernadero/prueba/mediciones.csv'
#path_actuadores = '/home/pi/Invernadero/prueba/actuadores.csv'
path = '/home/cmlavaut/Documents/pruebarasp/mediciones.csv'
path_actuadores = '/home/cmlavaut/Documents/pruebarasp/actuadores.csv'

now = datetime.now()
fecha = now.strftime("%d %m %y")
hora = now.strftime("%H:%M:%S")

def guardar(valorA,tabla,path):
        now = datetime.now()
        now_fecha = now.strftime("%d %m %y")
        now_hora = now.strftime("%H:%M:%S")
        try:
            tabla.insert(0, "Fecha", now_fecha)
            tabla.insert(1, "Hora", now_hora)
        except:
            #print("ya existe columnas de hora y fecha")
            pass            
        datos = [now_fecha, now_hora]
        datos = datos + valorA
        tabla.loc[tabla.shape[0]] = datos
        tabla.to_csv(path, index = False)
        #print(tabla)

def main():
    #Leer datos anteriores
    try:
        tabla = pd.read_csv(path)
    except:
        dicc = {
            "Place" : [],
            "humedad_suelo" : [],
            "humedad_amb" : [],
            "temperatura" :[],
            "status_agua" : [],
            "id_servidor" : [],
            "humedad_deseada" : [],
            "tiempo_regado" : [],
        }
        tabla = pd.DataFrame.from_dict(dicc)
        tabla.to_csv(path,index= False)
    try:
        actuadores = pd.read_csv(path_actuadores)
    except:
        dicc = {
            "Place" : [],
            "humedad_suelo" : [],
            "humedad_deseada" : [],
            "tiempo_regado" : [],
            "status_agua" : [],
            "id_servidor" : [],

        }
        actuadores = pd.DataFrame.from_dict(dicc)
        actuadores.to_csv(path_actuadores,index= False)
    
    sensor = "00 75 35.1 18.6 1 01 98 3"
    actuador= "00 50 96 4 0 2" 
    #data = sensor.split()
    data = actuador.split()
    print(data)

    if (len(data) == 8):
        print("valores correctos y motor off")
        guardar(data,tabla,path)
    elif (len(data) == 6):
        print("valores correctos y motor on")
        guardar(data,actuadores,path_actuadores)
    else:
        print("valores incorrectos")
        
    

if __name__ == "__main__":
    main()