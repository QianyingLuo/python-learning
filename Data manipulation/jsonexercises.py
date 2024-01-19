import json
import requests

'''
A continuación se muestra un JSON String
{"jefe_proyecto": {"Nombre": "Juan","Edad": 28,"Experiencia": ["Gestion","Finanzas","Bases de datos"],"Residencia": "Madrid","HorasProyecto": 3500},"empleados": [{"Nombre": "Elena","Edad": 26,"Experiencia": ["JavaScript","Python"],"Residencia": "Madrid","HorasProyecto": 500},{"Nombre": "Luis","Edad": 31,"Experiencia": ["Django","Flask","Pyramid"],"Residencia": "Barcelona","HorasProyecto": 1100}]}

Si es necesario utiliza un visualizador de JSON para entenderlo.
El objetivo es crear un diccionario con todos los datos y estructuras internas necesarias para que sea igual que el JSON String
Vete creando estructuras más pequeñas hasta que llegues a formar el mismo JSON string que ves arriba
Una vez que lo tengas creado, vamos a operar con él
Almacena esta estructura (el diccionario) en una variable
Comprueba su tipo y muéstrala por pantalla
Crea dos variables: horas_empleados y horas_jefe
Extrae las horas del jefe e introducelas en su variable
Crea un bucle que recorra el número de empleados que se tienen en la estructura, y para cada empleado vete sumando sus horas en su correspondiente variable
Suma todas las horas y muéstralas por pantalla
'''

lista_experiencia_jefe =  ["Gestion","Finanzas","Bases de datos"]
dicc_value_jefe =  {"Nombre": "Juan",
                   "Edad": 28,
                   "Experiencia": lista_experiencia_jefe,
                   "Residencia": "Madrid",
                   "HorasProyecto": 3500}

dicc_empleado_1 = {"Nombre": "Elena",
                   "Edad": 26,
                   "Experiencia": ["JavaScript","Python"],
                   "Residencia": "Madrid",
                   "HorasProyecto": 500}

print(dicc_empleado_1)

dicc_empleado_2 = {"Nombre": "Luis",
                   "Edad": 31,
                   "Experiencia": ["Django","Flask","Pyramid"],
                   "Residencia": "Barcelona",
                   "HorasProyecto": 1100}

print(dicc_empleado_2, "\n")


personal = {"jefe_proyecto": dicc_value_jefe, "empleados":[dicc_empleado_1, dicc_empleado_2]}
print(personal)
print(type(personal))

horas_jefe = personal["jefe_proyecto"]["HorasProyecto"]

horas_empleados = [i['HorasProyecto'] for i in personal['empleados']]
print("\nHoras empleados:", horas_empleados)

horas_total = horas_jefe + horas_empleados[0] + horas_empleados[1]
print("Horas en total:", horas_total)

'''
2. En el ejercicio anterior has trabajado con un diccionario que tu mismo/a creaste, conviértelo a un formato JSON String, muestra su tipo y los datos por pantalla
'''
json_personal = json.dumps(personal, indent=4) 
print("Tipo de los datos:", type(json_personal))
print("\nDatos en JSON:\n")
print(json_personal)

'''
3. A veces os encontraréis con JSON que tendréis que modificar. Para ello tenéis que decodificarlos, realizar las modificaciones pertinentes y volver a codificarlo para dejarlo como 
JSON de nuevo. En el siguiente ejemplo os habéis dado cuenta de que hay algunos errores:
A Superman le falta como poder "Volar"
En Batman, la edad es 35, no 350
En Batman, le sobra el poder de "Rayos en los ojos"
En Wonder Woman le falta el poder "Lazo de la verdad"
Después de corregir todo esto, transforma estos datos en un JSON String
'''

superheroes = {
	"nombreEquipo": "Super Hero Squad",
	"ciudad": "Metro City",
	"formado": 2016,
	"baseSecreta": "Super Tower",
	"activo": "Si",
	"miembros": [
		{
			"nombre": "SuperMan",
			"edad": 29,
			"identidadSecreta": "Clart Kent",
			"poderes": [
				"Super fuerza",
				"Super velocidad",
				"Rayos en los ojos"
			]
		},
		{
			"nombre": "Batman",
			"edad": 350,
			"identidadSecreta": "Bruce Wayne",
			"poderes": [
				"Detective",
				"Dinero",
				"Rayos en los ojos"
			]
		},
		{
			"nombre": "Wonder Woman",
			"edad": 900,
			"identidadSecreta": "Diana de Temiscira",
			"poderes": [
				"Super fuerza",
				"Super velocidad"
			]
		}
	]
}

superheroes["miembros"][0]["poderes"].append("Volar")
superheroes["miembros"][1]["edad"] = 35
superheroes["miembros"][1]["poderes"].pop(2)
superheroes["miembros"][2]["poderes"].append("Lazo de la verdad")

print(superheroes)
json_superheroes = json.dumps(superheroes) # Transformamos estos datos en un JSON String
print("\nTipo de los datos:", type(json_superheroes))

'''
4. En base al ejercicio anterior, modifica la estructura de super para lograr que miembros tenga dos ramas: "miembrosActivos" y "miembrosInactivos", 
donde cada una de estas ramas, almacenen los héroes que están en activo y los que no. En este caso, introduce a SuperMan y Wonder Woman en la lista de 
activos y a Batman en la de Inactivos. Esta modificación puedes hacerla como quieras, o bien programando las estructuras de datos e ir componiéndolo o 
bien cogiendo el JSON y modificándolo sobre él mismo. Al finalizar puedes comprobar tu JSON en un visualizador online (http://jsonviewer.stack.hu/)
'''

superheroes = {
  "nombreEquipo": "Super Hero Squad",
  "ciudad": "Metro City",
  "formado": 2016,
  "baseSecreta": "Super Tower",
  "activo": "Si",
  "miembros": [
    {
      "miembros activos": [
        {
          "nombre": "SuperMan",
          "edad": 29,
          "identidadSecreta": "Clart Kent",
          "poderes": [
            "Super fuerza",
            "Super velocidad",
            "Rayos en los ojos",
            "Volar"
          ]
        },
        {
          "nombre": "Batman",
          "edad": 35,
          "identidadSecreta": "Bruce Wayne",
          "poderes": [
            "Detective",
            "Dinero"
          ]
        }
      ]
    },
    {
      "miembros inactivos": {
        "nombre": "Wonder Woman",
        "edad": 900,
        "identidadSecreta": "Diana de Temiscira",
        "poderes": [
          "Super fuerza",
          "Super velocidad",
          "Lazo de la verdad"
        ]
      }
    }
  ]
}
             
json_superheroes = json.dumps(superheroes)
print(json_superheroes)

'''
5. En el siguiente código, accedemos a un JSON de forma remota, a partir de la respuesta, realizar lo siguiente:
Mostrar el tipo de dato que se ha recibido
Mostrar los datos recibidos
Mostrar el número de personas que se encuentran actualmente en el espacio
Realizar un bucle que recorra a todas esas personas y muestre nombre y nave en la que se encuentra.
'''

# API que nos comunica cuantas personas se encuentran actualmente en el espacio
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

print(type(data))
print("Datos recibidos:\n", data)

num_personas = len(data["people"])
print("\nEl número de personas en el espacio:", num_personas, "\n")

contador = 0
for i in data["people"]: 
    for key, value in data["people"][contador].items():
        print(key + ": " + value)
    contador += 1
