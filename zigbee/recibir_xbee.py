import serial
import time
import sys
import os
import pandas as pd
from datetime import datetime
import mysql.connector
from threading import Thread

arduino = serial.Serial()
db = mysql.connector.connect(
    host="172.19.0.6",
    user="cmlavaut",
    password="cmlavaut96*",
    database="invernadero"
)
print("Inicio...")


def guardar(valorA):
        now = datetime.now()
        now_fecha = now.strftime("%y %m %d")
        now_hora = now.strftime("%H:%M:%S")
        esp_serial = "esp"+ str(value[0])
        humedadSuelo = value[1]
        humedad = value[2]
        temperatura = value[3]
        ph = value[4]
        agua = value[5]
        with open ('./database/insertar.sql', 'r') as sql:
            comando_sql = sql.read()
            cursor = db.cursor()
            dispositivo = (esp_serial, humedadSuelo, humedad, temperatura, ph, agua, now_fecha, now_hora, "1")
            cursor.execute(comando_sql,dispositivo)
            db.commit()
            cursor.close()
        print("valores guardados en base de datos")


def main():
    try:
        #puerto= /dev/ttyUSB0 buscar bien el puerto del xbee
        arduino.port= puerto
        arduino.baudrate = 115200
        arduino.open()
    except:
        print("nothing conected")
        os._exit(0)
    
    arduino.flushInput()
    sensor = arduino.readline()
    sensor = sensor.decode()
    value= sensor.split()
    print(value)
    #if (len(value)==6): ver la sentencia bien de los valores
        print("valores correctos")
        guardar(value)
        client.disconnect()
    else:
        print("valores incorrectos")
        arduino.close()
        main()
    
    arduino.close()

def detener():
    time.sleep(20)
    arduino.close()
    print("cerrando codigo")
    os._exit(0)


if __name__ == "__main__":
    thread = Thread(target=detener)
    thread.start()
    main()
