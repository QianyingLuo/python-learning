import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
1) Trabajemos con NumPy

Importa numpy y usa un alias para poder utilizar sus recursos
Crea un array de elementos (del 10 al 100)
Invertir el array
Crear un array 3x3 con valores de 0 a 8
Crear un array identidad de 6x6
Crear un array con valores al azar con forma 3x3x3
Crear dos arrays con valores al azar A y B, verificar si son iguales (hay varias opciones, investigar)
'''

array1 = np.arange(10, 100)
print(array1)

print("\n", array1[::-1]) # invertir el array -- otra opción: np.flip(primer_array)

array2 = np.arange(0,9).reshape(3,3) # Crear un array 3x3 con valores de 0 a 8
print("\n", array2)

array3 = np.identity(6) # Crear un array identidad de 6x6
print("\n", array3)

array4 = np.random.random((3,3,3)) # Crear un array con valores al azar con forma 3x3x3
print("\n", array4)


A1 = np.random.randint(5) # Comprobar si los valores al azar de los dos arrays A y B son iguales
B1 = np.random.randint(5)
print("\narray A1:", A1)
print("array B1:", B1)
print(A1==B1)

A2 = np.random.rand(2, 3)
B2 = np.random.rand(2, 3)
print("\narray A2:", A2)
print("array B2:", B2)
print(A2==B2)

A3 = np.random.rand(4) 
B3 = np.random.rand(4)
print("\narray A3:", A3)
print("array B3:", B3)
print(A3==B3)

A4 = np.random.randint(100, 1000, (3, 2))
B4 = np.random.randint(100, 1000, (3, 2))
print("\narray A4:", A4)
print("array B4:", B4)
print(A4==B4)

'''
2) Sigamos con NumPy

Crear un array de 100 elementos aleatorios comprendidos entre 1 y 1000 (pueden ser números enteros).
Este array se llamara dólares
Crear otro array llamado euros
Realizar la conversión de los precios en dólares del primer array al segundo array en euros. Se puede serguir la siguiente conversión:
1 EUR = 1,14362 USD
1 USD = 0,874413 EUR
Mostrar el resultado del array de euros pero redondeado a 2 decimales
'''
dolares = np.random.randint(1, 1000, 100)
print(dolares)
euros = dolares * 0.874413
print(np.round(euros, 2))

'''
3) Trabajemos con pandas

Importa pandas y usa un alias para poder utilizar sus recursos
Cargar como dataframe de pandas el csv 05_05_imdb_titulos.csv y mostrar sus 5 primeros registros
Cargar como dataframe de pandas el csv 05_05_imdb_elenco.csv y mostrar sus 5 primeros registros
Mostrar el número de registros del dataframe de titulos
Mostrar el número de registros del dataframe de elenco
Mostrar las 5 peliculas más antiguas del listado de titulos
Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
Mostrar los 10 titulos más comunes (que más se repiten)
Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
Mostrar cuantas peliculas fueron hechas en el año 1950
Mostrar cuantas peliculas fueron hechas de 1950 a 1959
Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
Mostrar cuantos papeles para actores hubo en la década de los 50's
Mostrar cuantos papeles para actrices hubo en la década de los 50's
'''


titulos = pd.read_csv('Data manipulation/05_05_imdb_titulos.csv')
print(titulos.head()) # Primeras 5 filas del csv 05_05_imdb_titulos.csv

elenco = pd.read_csv('Data manipulation/05_05_imdb_elenco.csv')
print("\n", elenco.head()) # Primeras 5 filas del csv 05_05_imdb_elenco.csv

print(len(titulos)) #Mostrar el número de registros del dataframe de titulos
print(len(elenco)) #Mostrar el número de registros del dataframe de elenco

# Mostrar las 5 peliculas más antiguas del listado de titulos
titulos_ordenado = titulos.sort_values(by=['year'], ascending=True)
print("====Las 5 peliculas más antiguas====")
print(titulos_ordenado[:5])

# Las peliculas que en el titulo tienen la palabra "Dracula"
condicion = titulos['title'].str.contains('Dracula', na=False)
peli_dracula = titulos['title'][condicion]
print("Las peliculas que en el titulo tienen la palabra 'Dracula':\n", peli_dracula)
print("\nNúmero total: ", len(peli_dracula))

print("*" * 25)

# Mostrar los 10 titulos más comunes (que más se repiten)
print(titulos['title'].value_counts().nlargest(10))

print("*" * 25)

# Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
condicion = titulos["title"].str.contains("Exorcist", na=False)
exorcist = titulos.loc[condicion, ["title", "year"]]
exorcist_ordenado = exorcist.sort_values(by=["year"], ascending=True)
print(exorcist_ordenado)

print("*" * 25)

# Mostrar cuantas peliculas fueron hechas en el año 1950
grouped_titulos = titulos.groupby("year")
peli_1950 = grouped_titulos.get_group(1950)
print("{} películas fueron hechas en el año 1950".format(len(peli_1950)))
print(peli_1950)

print("*" * 25)

# Mostrar cuantas peliculas fueron hechas de 1950 a 1959
condicion = (titulos["year"] >= 1950) & (titulos["year"]<= 1959)
peli_19501959 = titulos.loc[condicion, ["title", "year"]]
print("{} películas fueron hechas de 1950 a 1959".format(len(peli_19501959)))
print(peli_19501959)

print("*" * 25)

# Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". 
#También mostrar el número total de coincidencias
condicion = elenco["title"].str.fullmatch("The Godfather", na=False)
the_godfather = elenco.loc[condicion, ["title", "character"]]
print(the_godfather)
grouped_character_the_godfather = the_godfather.groupby("character")
print(grouped_character_the_godfather.size())

print("*" * 25)

# Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
condicion = (elenco["title"].str.fullmatch("Dracula", na=False)) & (elenco["year"] == 1958)
dracula = elenco.loc[condicion, ["title", "year", "name", "character", "n"]]
dracula_ordenada = dracula.sort_values(by=["n"])
print(dracula_ordenada)

print("*" * 25)

# Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
condicion = elenco["character"] == "Bruce Wayne"
papeles_bruce_wayne = elenco.loc[condicion, ["title", "year", "name", "character"]]
print("{} papeles de 'Bruce Wayne' han sido hechos en la historia de las peliculas".format(len(papeles_bruce_wayne)))
print(papeles_bruce_wayne)

print("*" * 25)

# Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
condicion = elenco["name"] == "Robert De Niro"
papeles_Robert_de_niro = elenco.loc[condicion, ["title", "year", "character"]]
papeles_Robert_de_niro_ordenado = papeles_Robert_de_niro.sort_values(by=["year"])
print("Roberto De Niro ha hecho {} papeles en su carrera".format(len(papeles_Robert_de_niro["character"])))
print(papeles_Robert_de_niro_ordenado)

print("*" * 25)

# Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, 
# ordenado por año de forma descendente
condicion = (elenco["n"] == 1) & (elenco["name"] == "Charlton Heston") & (elenco["year"]>=1960) & (elenco["year"]<1970)
protagonista_charltonheston_60 = elenco.loc[condicion, ["title", "year", "name", "character", "n"]]
protagonista_charltonheston_60_ordenado = protagonista_charltonheston_60.sort_values(by=["year"], ascending=False)
print(protagonista_charltonheston_60_ordenado)

print("*" * 25)

# Mostrar cuantos papeles para actores hubo en la década de los 50's
condicion = (elenco["type"]=="actor") & (elenco["year"]>=1950) & (elenco["year"]<1960)
actores50 = elenco.loc[condicion, ["character", "type", "year"]]
print("Hubo {} papeles para actores en la década de los 50's".format(len(actores50["type"])))
actores50

print("*" * 25)

# Mostrar cuantos papeles para actrices hubo en la década de los 50's
condicion = (elenco["type"] == "actriz") & (elenco["year"]>=1950) & (elenco["year"]<1960)
actrices50 = elenco.loc[condicion, ["character", "type", "year"]]
print("Hubo {} papeles para actrices en la década de los 50's".format(len(actrices50["type"])))
print(actrices50)