import mysql.connector
from flask import request
import time
import pandas as pd
import datetime

db = mysql.connector.connect(
    host="172.19.0.6",
    user="cmlavaut",
    password="cmlavaut96*",
    database="invernadero"
)
def user_put(userdata):
    with open ('./webapp/bd/insertar.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        creado_user = datetime.datetime.now()
        creado_user = creado_user.strftime("%Y-%m-%d %H:%M:%S")
        valor = (userdata.name, userdata.email, userdata.username, userdata.password, creado_user, creado_user, userdata.id_plantacion)
        cursor.execute(comando_sql, valor)
        db.commit()
        cursor.close()

def get_user(id):
    with open ('./webapp/bd/consulta.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        try:
            cursor.execute(comando_sql.format(str(id)))
            consulta = cursor.fetchall()[0]
            user_ref = {
                'username' : [consulta[2]],
                'password' : [consulta[3]],
                'name' : [consulta[0]],
                'email' : [consulta[1]],
                'id_plantacion': [consulta[4]],
            }
            resultado = pd.DataFrame(user_ref)
            cursor.close()
        except:
            user_ref = {
                'username' : [],
                'password' : [],
                'name' : [],
                'email' : [],
                'id_plantacion': []
            }
            resultado = pd.DataFrame(user_ref)
        return resultado 


def get_planta(id):
    with open ('./webapp/bd/consultaplanta.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        try:
            cursor.execute(comando_sql.format(str(id)))
            consulta = cursor.fetchall()[0]
            user_ref = {
                'esp32' : [consulta[0]],
                'humedadSuelo' : [consulta[1]],
                'humedad' : [consulta[2]],
                'temperatura' : [consulta[3]],
                'ph': [consulta[4]],
                'agua': [consulta[5]],
            }
            resultado = pd.DataFrame(user_ref)
            cursor.close()
        except:
            user_ref = {
                'esp32' : [],
                'humedadSuelo' : [],
                'humedad' : [],
                'temperatura' : [],
                'ph': [],
                'agua': []
            }
            resultado = pd.DataFrame(user_ref)
        return resultado 



def get_fecha(id):
    with open ('./webapp/bd/select_medicion.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        try:
            cursor.execute(comando_sql.format(str(id)))
            consulta = cursor.fetchall()[0]
            fecha = {
                'fecha': [consulta[0]],
                'hora': [consulta[1]]
            }
            resultado = pd.DataFrame(fecha)
            cursor.close()
        except:
            fecha = {
                'fecha' : [],
                'hora': []
            }
            resultado = pd.DataFrame(fecha)
        return resultado 
    




