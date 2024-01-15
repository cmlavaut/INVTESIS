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

def get_fecha(id):
    with open ('./bd/select_time.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        try:
            cursor.execute(comando_sql.format(str(id)))
            consulta = cursor.fetchall()
            columnas = ['fecha', 'hora']
            resultado = pd.DataFrame(consulta, columns = columnas)
            cursor.close()
        except:
            fecha = {
                'fecha' : [],
                'hora': []
            }
            resultado = pd.DataFrame(fecha)
        return resultado 

def main():
    tabla = get_fecha(1)
    print(tabla)
    fechaArray = tabla.loc[:,'fecha'].drop_duplicates().to_numpy()
    lenFecha = len(fechaArray)

    content = {
        'fechaArray' : fechaArray,
        'lenFecha' : lenFecha
    }
    print(content)

if __name__ == '__main__':
    main()