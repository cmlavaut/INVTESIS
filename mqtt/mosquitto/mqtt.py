import time
import sys
import os
import pandas as pd
from datetime import datetime
import paho.mqtt.client as mqtt
import json
from threading import Thread

path = '../database/mediciones.csv'
broker = '172.19.0.2'
topic = 'sensores/0'
leercredenciales = open('credenciales.json',mode = 'r')
credenciales = json.load(leercredenciales)
user = credenciales['user']
paswd = credenciales['passwd']
leercredenciales.close()
now = datetime.now()
fecha = now.strftime("%d %m %y")
hora = now.strftime("%H:%M:%S")

def on_connect(client, userdata, flags, rc):
    print("conectando al broker", rc)
    client.subscribe(topic)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Se ha perdido la conexión con el broker")
    else:
        print("Desconectando del Broker")
    client.loop_stop()
    os._exit(0)

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
        print(tabla.shape[0])
        tabla.loc[tabla.shape[0]] = datos
        tabla.to_csv(path, index = False)
        print(tabla)


def on_message(client, userdata, message):
    global tabla
    print("topic: {} y su mensaje es {}".format(message.topic, message.payload.decode()))
    value = message.payload.decode()
    value = value.split()
    if (len(value) == 7):
        print("valores correctos")
        guardar(value, tabla)
        client.disconnect()
    else:
        print("valores incorrectos")

def main():
    #Leeer datos anteriores
    global tabla
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
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.username_pw_set(user,paswd)
    client.connect(broker)
    client.loop_start()
    print("Leyendo: {} {} {}".format(topic,fecha,hora))
    


def detener():
    time.sleep(15)
    print("cerrando codigo")
    os._exit(0)


if __name__ == "__main__":
    thread = Thread(target=detener)
    thread.start()
    main()
