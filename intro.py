# Este bloque comprueba que archivos se encuentran en la ruta
import os

r''' IMPORTANTE: Usar el prefijo 'r' en un directorio para que python lo identifique como "raw string"
    no usar la r hace que se confunda la  \U como un comando unicode parecido a \n y da error'''

# my_dir_path = r'C:\Users\Jazz\Desktop\Maiguel R. Guti\MI trabajo\Pandas\survey'
# dir_content = os.listdir(my_dir_path)
# print(dir_content)

# -----------------------------------

import pandas # as pd

"""Pandas es comunmente usado junto con el editor de texto Jupiter > pip install jupyterlab
este editor muestra las tablas visualmente y se ejecuta en internet
ABRIR ARCHIVO: cd Escritorio/Ruta_de/Carpeta para entrar en la carpeta desde la terminal > jupyter notebook
Esto abre un servidor de jupyter, en internet, pero HAY QUE DEJAR LA TERMINAL ABIERTA para poder mantener
el servidor > Crear nuevo notebook"""

# En pandas el principal objeto con el que se trabaja es dataframes, que son iguales a los de R, una lista de valores

# Muestra maximo 85 clumnas al imprimir, pero en terminal se ve como basura, en Jupyter es donde se ve bien
pandas.set_option('display.max_columns',20)

# En esta linea, se crea un dataframe, en formato de diccionario
df_original = pandas.DataFrame({'columna1':[1,2,3,4], 'columna2':['a','b','c','d']})
print(df_original) # En jupyter se puede mostrar con un mejor formato

# Si se usa una linea para leer un archivo csv, también crea un dataframe
df = pandas.read_csv(r'C:\Users\Jazz\Desktop\Maiguel R. Guti\Programacion\Python\Pandas\survey\survey_results_public.csv')

# ATRIBUTOS

# Es posible imprimir el dataframe completo, pero si es grande se tarda mucho, por eso es preferible imprimir la cabeza o cola para revisar
if False:
    print(df) # imprime el dataframe entero (con un limite)
    print(df.head(3)) # muestra las 3 primeras filas
    print(df.tail()) # default muestra 5 filas (ultimas)

    # Informacion del dataframe
    print(df.shape) # Tupla (numero filas, numero columnas)
    print(df.info()) # Tambien devuelve el tipo de datos en cada columna (object = string)


# FILTRAR

# Como en excel, se puede filtrar información, pero en un dataframe nuevo

# DataFrame  donde la columna Trans tenga la respuesta Yes
trans_devs = df[(df["Trans"] == "Yes")] # especificando la columna por su nombre
# trans_devs = df[(df[51] == "Yes")] ???
print(trans_devs)

if False:
    # Tambien se puede ordenar los datos de acuerdo a una columna
    print(trans_devs.sort_values(by = 'YearsCode', ascending = False))

if False:
    print(trans_devs.head(3))
    print(len(trans_devs)) # para saber cuantas entradas hay, en base a len()
    print(trans_devs.iloc[1:4]) # acceder a las filas 2da a 4ta
    print(trans_devs.iloc[3:4]) # acceder a las 4ta  fila
    print(trans_devs.iloc[4]) # no se que hace

# AGREGAR

# Para agregar una columna, hay distintos metodos
''' Estas lineas solo se pueden ejecutar una vez, hacerlo multiples veces da errores '''
# El metodo crudo agrega a la derecha de la última columna del DataFrame, hayq que especificar una colmna extra que no exista

if False:
    trans_devs["Hola"] = ""
    trans_devs["Dia"] = "Lunes" # Esto agrega una columna donde todos los valores son "Lunes"
    #trans_devs["Dia"] = ['Lun', 'Mar', 'Mie',...]  # También se puede agregar una lista, pero la longitud de la lista y el dataframe debe coincidir

# Con el metodo insert() se puede especificar la locacion de la columna
trans_devs.insert(loc = 1, column = "Pollos", value = range(1064)) # Es necesario los 3 argumentos

# El metodo assign() es igual a insert, pero puedes insertar multiples columnas en una linea

# La otra forma es usando un diccionario como al inicio
"trans_devs['Col_Name'] = {diccionario}, pero este es un poco raro"

# Exportar un csv a directorio (como un archivo común)
trans_devs.to_csv("Trans_developers.csv") 
# otros argumentos son 
#   encoding = 'utf-8' (default), 'utf-16' resuelve muchos problemas
#   sep = '', (el separador de valores en el texto del csv)
