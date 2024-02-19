import time
import sys
import os
import pandas as pd
import mysql.connector

path = '/home/invernadero/Invernadero/database/mediciones.csv'
path_actuadores = '/home/invernadero/Invernadero/database/actuadores.csv'


db = mysql.connector.connect(
    host = "148.204.186.148",
    user = "cmlavaut",
    password ="cmlavaut96*",
    database = "invernadero"
)
sql = "INSERT INTO end_device (medicion_fecha, medicion_hora, esp_serial, sensor_HumS, sensor_Hum, sensor_Temp, status_agua, id_servidor) VALUES (%s, %s, %s,%s, %s, %s,%s,%s)" 
sql_actuadores = "INSERT INTO actuadores (medicion_fecha, medicion_hora, esp_serial, humedad_suelo, humedad_deseada, tiempo_regado, status_agua, id_servidor) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
conexion = db.cursor() 


def main():
    tabla = pd.read_csv(path)
    datos = pd.DataFrame(tabla)
    columnas_eliminar = ["humedad_deseada", "tiempo_regado"]
    datos = datos.drop(columnas_eliminar, axis= 1)
    print(datos)

    for index, row in datos.iterrows():
        fecha= row["Fecha"]
        hora = row["Hora"]
        place = row["Place"]
        seleccionar= "SElECT `medicion_fecha`, `medicion_hora`, `esp_serial` FROM `end_device` WHERE medicion_fecha ='{}' AND medicion_hora ='{}' AND esp_serial='{}';".format(fecha, hora, place)
        conexion.execute(seleccionar)
        consulta = conexion.fetchall()
        print (consulta)
        if not consulta:
            conexion.execute(sql, tuple(row))
            db.commit()
            print("datos insertados en la base de datos")
        else:
            print("dato ya insertado")
    
    time.sleep(10)
    
    tabla_actuadores = pd.read_csv(path_actuadores)
    data = pd.DataFrame(tabla_actuadores)
    print(data)

    for index, row in data.iterrows():
        fecha= row["Fecha"]
        hora = row["Hora"]
        place = row["Place"]
        seleccionar= "SElECT `medicion_fecha`, `medicion_hora`, `esp_serial` FROM `actuadores` WHERE medicion_fecha ='{}' AND medicion_hora ='{}' AND esp_serial='{}';".format(fecha, hora, place)
        conexion.execute(seleccionar)
        consulta = conexion.fetchall()
        print (consulta)
        if not consulta:
            conexion.execute(sql_actuadores, tuple(row))
            db.commit()
            print("datos insertados en la base de datos")
        else:
            print("dato ya insertado")

    conexion.close()
    db.close()
    print("Finished")
    

if __name__ == "__main__":
    main()

    

    
