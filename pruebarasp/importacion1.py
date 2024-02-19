import time
import sys
import os
import pandas as pd
import mysql.connector

path = "/home/cmlavaut/Documents/mediciones.csv"
db = mysql.connector.connect(
    host = "148.204.186.148",
    user = "cmlavaut",
    password ="cmlavaut96*",
    database = "invernadero"
)

conexion = db.cursor() 
sql = "INSERT INTO end_device (medicion_fecha, medicion_hora, esp_serial, sensor_HumS, sensor_Hum, sensor_Temp, status_agua, id_servidor) VALUES (%s, %s, %s,%s, %s, %s,%s,%s)" 

def main():
    tabla = pd.read_csv(path)
    datos = pd.DataFrame(tabla)
    print(datos)
    for index, row in datos.iterrows():
        conexion.execute(sql, tuple(row))
        db.commit()
    
    print("datos insertados en la base de datos")
    
    conexion.close()
    db.close()

if __name__ == "__main__":
    main()
