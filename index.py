from flask import Flask, render_template, make_response, request
import plotly.utils
#from velocimetro import crear_velocimetro
import matplotlib.pyplot as plt
from threading import Thread
from webapp import create_app
import numpy as np
import pandas as pd
from datetime import datetime
#import time
import json
import os


path = '../database/mediciones.csv'

varHumedad = [0.0,0.0, 0.0]
varTemperatura = [0.0,0.0,0.0]
varHumedadSuelo = [0.0,0.0,0.0]
agua = [0,0,0]
humedadMinima = [0,0,0]
tiempoRegado = [0,0,0]
numPlanta = 0
listoThread = [Thread(),Thread(), Thread()]

app = create_app()

def inicializarSensores(planta):
    global varHumedadSuelo, varHumedad, varTemperatura, agua, humedadMinima, tiempoRegado, numPlanta
    numPlanta = planta
    data = pd.read_csv(path)
    fila = data[data['Place']== numPlanta].iloc[-1]
    varHumedadSuelo[numPlanta] = np.round(float(fila[3]), 2)
    humedadMinima[numPlanta] = 4.0
    tiempoRegado[numPlanta] = 25
    varHumedad[numPlanta] = np.round(float(fila[4]),2)
    varTemperatura[numPlanta] = np.round(float(fila[5]),2)
    agua[numPlanta] = int(fila[6])
    print("Se cargo los datos")
    context = {
        "varHumedad" : varHumedad[numPlanta],
        "varTemperatura" : varTemperatura[numPlanta],
        "varHumedadSuelo" : varHumedadSuelo[numPlanta],
        "agua" : agua[numPlanta],
        'humedadMinima' : humedadMinima[numPlanta],
        'tiempoRegado' : tiempoRegado[numPlanta],
        'numPlanta': numPlanta
    }
    return context

  
    
""" @app.route('/user/add', methods=['GET', 'POST']) 
def clientadd():
    datos = {}
    form = UserForm()
    if form.validate_on_submit(): #aqui estoy validando que tenga el texto lleno con algo
        datos= {
            'id': form.id.data,
            'name': form.name.data, 
            'email': form.email.data,
            'userdb': form.userdb.data, 
            'passw': form.passw.data
        }
        form.id.data = ''
        form.name.data = '' #limpiar el box 
        form.email.data = ''
        form.userdb.data = ''
        form.passw.data = ''
    return render_template ("add_client.html", **datos, form = form) """


@app.route('/graficar/<parametro>',methods=['GET'])
def graficar(parametro):
    global numPlanta
    datosGraficar = parametro.split(',')
    generarGrafico = 'python3 graficar.py "{}" "{}" "{}"'.format(numPlanta, datosGraficar[1],datosGraficar[0])
    print(generarGrafico)
    os.system(generarGrafico)
    response = make_response(generarGrafico)
    return response

@app.route('/enviarData/<parametro>',methods=['GET'])
def enviarData(parametro):
    global numPlanta
    actualizar = parametro.split(",")
    data = pd.read_csv(path)
    fila = data[data['Place']== numPlanta].iloc[-1]
    indice = fila.name
    fila["humedad_selecc"] = actualizar[0]
    fila["tiempo_selecc"]= actualizar[1]
    data.loc[indice] = fila
    data.to_csv("../database/mediciones.csv", index= False)
    return response

@app.route('/historial')
def historial():
    dataFrame = pd.read_csv(path)
    fechaArray = dataFrame.loc[:,'Fecha'].drop_duplicates().to_numpy()
    lenFecha = len(fechaArray)
    content = {
        'fechaArray' : fechaArray,
        'lenFecha' : lenFecha
    }
    return render_template("historial.html", **content)


@app.route('/inicio')
def main():
    return render_template('inicio.html')

@app.route('/sensor/<planta>',methods=['GET'])
def sensor(planta):
    #print(planta)
    datos = inicializarSensores(int(planta))
    print(datos)
    return render_template('sensor{}.html'.format(planta), datos = datos)

def pagenotfound(error):
    return render_template("404.html"), 404

# if __name__ == '__main__':
#     app.register_error_handler(404, pagenotfound)
#     #app.run(host="172.19.0.3",port=5010,debug=True)
#     app.run(port=5010, debug=True)
