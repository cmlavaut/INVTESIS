import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import sys

#path = "../database/mediciones.csv"
hora_arreglo = np.arange(0,24)
humedadamb = np.empty(0)
humedadsuelo = np.empty(0)
ph = np.empty(0)
temperatura = np.empty(0)

db = mysql.connector.connect(
    host="172.19.0.6",
    user="cmlavaut",
    password="cmlavaut96*",
    database="invernadero"
)

def get_fecha(id):
    with open ('./bd/graficar.sql', 'r') as sql:
        comando_sql = sql.read()
        cursor = db.cursor()
        try:
            cursor.execute(comando_sql.format(str(id)))
            consulta = cursor.fetchall()
            columnas = ['fecha', 'hora', 'hmedad_suelo', 'humeda_amb', 'temperatura', 'ph']
            resultado = pd.DataFrame(consulta, columns = columnas)
            cursor.close()
        except:
            fecha = {
                'fecha' : [],
                'hora': [],
                'humedad_suelo': [],
                'humedad_amb': [],
                'temperatura': [],
                'ph': []
            }
            resultado = pd.DataFrame(fecha)
        return resultado 
    
def promedio(columna,i , datos):
    hora = datos[datos["hora"].astype(int)==i]
    hora = hora.loc[:, columna].astype(float)
    h_arr = hora.to_numpy()
    return np.round(np.mean(h_arr),3)
    

def graficar(x,y,variable,titulo):
    plt.plot(x, y, "r", marker = "o")
    plt.title(titulo)
    plt.xlabel("Horas")
    plt.ylabel(variable)
    titulo = titulo.replace(" ","")
    titulo = titulo.replace(":","")
    plt.savefig('./static/graficos/{}.png'.format(titulo))
    #plt.show()
    
def main():
    global humedadamb, humedadsuelo, temperatura, ph
    place = sys.argv[1]
    fecha = sys.argv[2]
    variable = sys.argv[3]
    datos = get_fecha(place)
    print(datos)

    print(datos.tail(8)) #muestra los ultimos 8 filas

    for i in hora_arreglo:
        h_mediana = promedio("humedad_amb", i, datos)
        humedadamb = np.append(humedadamb, h_mediana)
        h_mediana = promedio("humedad_suelo", i, datos)
        humedadsuelo = np.append(humedadsuelo, h_mediana)
        h_mediana = promedio("temperatura", i, datos)
        temperatura = np.append(temperatura, h_mediana)
        h_mediana = promedio("ph", i, datos)
        ph = np.append(ph, h_mediana)

        
    if variable == 'temperatura':
        y = temperatura
    elif variable == 'humedad ambiente':
        y = humedadamb
    elif variable == 'humedad suelo':
        y = humedadsuelo
    else:
        y = ph

         
    print(hora_arreglo)
    print(humedadamb)
    print(humedadsuelo)
    titulo = "Sensor:{} Fecha:{}".format(variable,fecha)
    graficar(hora_arreglo,y,variable,titulo)
       

    

if __name__ == "__main__":
    main()




