import serial
import time
import sys
import os
from xbee import ZigBee
import pandas as pd
from datetime import datetime

path = '/home/database/mediciones.csv'
path_actuadores = '/home/database/actuadores.csv'
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
        }
        actuadores = pd.DataFrame.from_dict(dicc)
        actuadores.to_csv(path_actuadores,index= False)
    
    #Comunicacion Serial

    try:
        puerto= '/dev/ttyUSB0' #buscar bien el puerto del xbee
        BAUD = 9600
        conexion = serial.Serial(puerto, BAUD)
        print("xbee conectado")
        xbee = ZigBee(conexion)
    except:
        print("nothing conected")
        os._exit(0)
    
    
    try:
        sensor = xbee.wait_read_frame()
        data = sensor['rf_data'].decode('utf-8').split()
        print(data)

        if (len(data) ==7):
            print("valores correctos y motor off")
            guardar(data,tabla,path)
        elif (len(data) == 5):
            print("valores correctos y motor on")
            guardar(data,actuadores,path_actuadores)
        else:
            print("valores incorrectos")
            conexion.close()
            main()

           
    except:
        print("no recibo nada")
        conexion.close()
        main()
   
    
    conexion.close()

if __name__ == "__main__":
    main()
