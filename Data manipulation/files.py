'''
1) En este ejercicio deberás crear un programa que abra y lea un fichero de texto, y nos proporcione la siguiente información:

Nombre del fichero
Si el fichero esta cerrado o no (True o False)
El modo de apertura del fichero
El fichero de texto se denominará example.txt y tendrá el siguiente contenido en texto plano (créalo previamente):

Hola que tal estas
Esto es una prueba
Hoy no llueve
Se acerca la navidad
Hasta luego y muy buenas
Busca en la documentación que métodos nos proporcionan la información requerida. Por último, lista el contenido del fichero.
'''

import os

with open(file="Data manipulation/example.txt",mode="r", encoding="utf8") as fichero:
    for linea in fichero:
        print(linea, end="")

nombre_fichero = os.path.basename("example.txt")
print(f"Nombre del fichero: {nombre_fichero}")

def cerrado():
    print("El fichero está cerrado?", end=" ")
    if fichero.close:
        print(True)
    else:
        print(False)

cerrado()

print("El modo de apertura del fichero: función with open")

'''
2) Sobre el fichero anterior, obtén la siguiente información:

Lectura de una línea del fichero
Lectura del fichero línea a línea
'''

fichero = open(file="Data manipulation/example.txt",mode="r",encoding="utf8")
texto = fichero.readline() # lectura de una línea
print(texto)

fichero = open(file="Data manipulation/example.txt",mode="r",encoding="utf8")
texto = fichero.readlines()
for linea in texto:
    print(linea)
fichero.close()

'''
3) Sobre el fichero anterior, realiza la siguiente operación:

Abrir el fichero en modo escritura (concatenando el contenido, sin sobrescribirlo) y escribir una nueva línea de texto
Comprueba que este funcionando correctamente comprobando el fichero (tendrás que cerrarlo y abrirlo para poder visualizar los cambios).
'''

fichero = open(file="Data manipulation/example.txt",mode="a",encoding="utf8") # Añadimos una nueva línea
fichero.write('\nHola de nuevo')
fichero.close()

fichero = open(file="Data manipulation/example.txt",mode="r",encoding="utf8") # Volvemos a leer el fichero para comprobar que se haya añadido esta última línea
texto = fichero.readlines() # Leer creando una lista de líneas
fichero.close()
print(texto)

'''
4) Sobre el fichero anterior, realiza la siguiente operación:

Abrir el fichero en modo escritura (sobrescribiendo el contenido) y escribir una nueva línea de texto
Comprueba que este funcionando correctamente comprobando el fichero (tendrás que cerrarlo y abrirlo para poder visualizar los cambios).
'''

nuevo_texto = "Sobreescribimos el contenido"
fichero = open(file="Data manipulation/example.txt",mode="w",encoding="utf8") 
fichero.write(nuevo_texto)
fichero.close()

fichero = open(file="Data manipulation/example.txt",mode="r",encoding="utf8") # Volvemos a leer el fichero para comprobar que se haya añadido esta última línea
texto = fichero.readlines()
fichero.close()
print(texto)

'''
5) En este ejercicio deberás crear un programa que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego recorre las personas de la lista y para cada una muestra de forma amigable todos sus campos. Por ejemplo así:

(id=1) Carlos Pérez => 05/01/1989 
El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo previamente):

1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.

Aviso importante: Si quieres leer un fichero que no se ha escrito directamente con Python, entonces es posible que encuentres errores de codificación al mostrar algunos caracteres. Asegúrate de indicar la codificación del fichero manualmente durante la apertura como argumento en el open, por ejemplo con UTF-8:

open(..., encoding="utf8")
Pista: Es posible que tengas que recurrir a funciones como replace o split para poder modificar el texto de una línea de texto. Busca documentación sobre ello
'''

claves = ['id','nombre','apellido','nacimiento']
personas = [] # Añadiremos el diccionario a una lista llamada personas

try:
    with open(file="Data manipulation/persons.txt",mode="r",encoding="utf8") as f:
        for linea in f:     # para cada línea
            dic = {} 
            for c,v in zip(claves,linea.split(';')):    # separamos clave, valor
                dic[c] = v.rstrip()     # añadimos clave valor
            personas.append(dic)       # añadimos el diccionario a la lista
except Exception as e:
    print(e)

f.close()

for x in personas:     # recorremos las personas de la lista
    print(f"(id={x['id']}) {x['nombre']} {x['apellido']} => {x['nacimiento']})")