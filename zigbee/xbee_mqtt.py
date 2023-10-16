import serial
import time
import sys
import os
import pandas as pd
from datetime import datetime
import json
from threading import Thread

path = '/home/database/mediciones.csv'
now = datetime.now()
fecha = now.strftime("%d %m %y")
hora = now.strftime("%H:%M:%S")
conexion= serial.Serial()

def guardar(valorA,tabla):
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
        print(tabla)


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
        }
        tabla = pd.DataFrame.from_dict(dicc)
        tabla.to_csv(path,index= False)
    #Comunciacion Serial
    try:
        puerto = '/dev/ttyUSB0'
        conexion.port = puerto
        conexion.baudrate = 115200
        conexion.open()
    except:
        print("nothing conected")
        os._exit(0)
    
    conexion.flushInput()
    sensor = conexion.readline()
    sensor = sensor.decode()
    value= sensor.split()
    print(value)
    if (len(value)==5):
        print("valores correctos")
        guardar(value,tabla)
    else:
        print("valores incorrectos")
        conexion.close()
        main()
    
    conexion.close()

def detener():
    time.sleep(15)
    conexion.close()
    print("cerrando codigo")

if __name__ == "__main__":
    #thread = Thread(target=detener)
    #thread.start()
    main()
