'''
1.Crea una base de datos que se llame biblioteca
2. Crea las siguiente tablas (deberás poner los tipos de los atributos con lógica, investiga cuales hay en SQLite para poder hacerlo):
    autor(dni, nombre, apellidos, estarVivo)
    libro(isbn, titulo, editorial, año_escrito)
    usuario(dni, nombre, apellidos, numPrestamos)
2.Inserta al menos 3 registros en cada una de las tablas
    En autor, algunos vivos y otros muertos
    En libro, algunos con año de escritura anerior a 1900 y otros después
    En usuario, algunos con más de 10 prestamos y otros con menos
3.Comprueba que todo este correcto con DB Browser (SQLite)
4.Realiza las siguientes consultas:
    Lista a todos los autores
    Lista todos los libros
    Lista todos los usuarios
    Lista todos los autores que esten vivos (CLAUSULA WHERE)
    Lista todos los libros que hayan sido escritos posteriormente a 1900
    Lista todos los usuarios que se hayan llevado más de 10 libros y que se llamen Paco
'''

import os
import sqlite3

# Definimos la ruta y nombre de la base de datos, por defecto, en el directorio actual
default_path_db = "Data manipulation/biblioteca.db" 
   
''' Función encargada de la conexión a la base de datos '''
def db_connect(db_path = default_path_db):
    conexion = sqlite3.connect(db_path) # Conexión a la base de datos
    return conexion
 
''' Función encargada de crear las tablas de la BD '''
def db_create_tables():
    try:
        cur.execute("""CREATE TABLE autor (
                              dni TEXT NOT NULL,
                              nombre TEXT NOT NULL,
                              apellidos TEXT NOT NULL,
                              estarVivo INTEGER NOT NULL
                            )""")
        print(" > Tabla autor creada con éxito")                        
    except sqlite3.OperationalError:
        print(" > La tabla autor ya existe") 
        
    try:
        cur.execute("""CREATE TABLE libro (
                              isbn INTEGER NOT NULL,
                              titulo TEXT NOT NULL,
                              editorial TEXT NOT NULL,
                              año_escrito INTEGER NOT NULL
                            )""")
        print(" > Tabla libro creada con éxito")                        
    except sqlite3.OperationalError:
        print(" > La tabla libro ya existe") 
        
    try:
        cur.execute("""CREATE TABLE usuario (
                              dni TEXT NOT NULL,
                              nombre TEXT NOT NULL,
                              apellidos TEXT NOT NULL,
                              numPrestamos INTEGER NOT NULL
                            )""")
        print(" > Tabla usuario creada con éxito")                        
    except sqlite3.OperationalError:
        print(" > La tabla usuario ya existe") 
        
        
    con.commit() # Se actualizan los cambios pendientes en la BD

''' Función encargada de crear un registro en la tabla autor '''
def db_create_autor(dni, nombre, apellidos, estarVivo):
    sql = """
        INSERT INTO autor (dni, nombre, apellidos, estarVivo)
        VALUES (?, ?, ?, ?)"""
    cur.execute(sql, (dni, nombre, apellidos, estarVivo))
    return cur.lastrowid

''' Función encargada de crear un registro en la tabla libro '''
def db_create_libro(isbn, titulo, editorial, año_escrito):
    sql = """
        INSERT INTO libro (isbn, titulo, editorial, año_escrito)
        VALUES (?, ?, ?, ?)"""
    cur.execute(sql, (isbn, titulo, editorial, año_escrito))
    return cur.lastrowid

''' Función encargada de crear un registro en la tabla usuario '''
def db_create_usuario(dni, nombre, apellidos, numPrestamos):
    sql = """
        INSERT INTO usuario (dni, nombre, apellidos, numPrestamos)
        VALUES (?, ?, ?, ?)"""
    cur.execute(sql, (dni, nombre, apellidos, numPrestamos))
    return cur.lastrowid

    
''' Función que resetea la base de datos eliminando sus tablas '''
def db_reset_database():
    cur.execute("DROP TABLE IF EXISTS autor")
    cur.execute("DROP TABLE IF EXISTS libro")
    cur.execute("DROP TABLE IF EXISTS usuario")
    con.commit() # Se actualizan los cambios pendientes en la BD
    print(" > Reset DB ... OK")
    
def db_select_all(nombre_tabla):
    print("\n=== LISTA", nombre_tabla.upper(), "===")
    cur.execute("SELECT * FROM {}".format(nombre_tabla))
    resultados = cur.fetchall()
    for registro in resultados:
        print(registro)    
    

''' Función pricipal del programa '''
if __name__ == "__main__":
    
    con = db_connect() # Invocamos a la función que establece la conexión con la BD
    cur = con.cursor()  # Se crea el cursor para la BD
    
    db_reset_database() # Borramos las tablas de la base de datos antes de empezar
    db_create_tables() # Crear las tablas
    
    db_create_autor("25804316", "William", "Faulkner", False) # dni, nombre, apellidos, estarVivo
    db_create_autor("34820945", "Stephen", "Edwin King", True)
    db_create_autor("68559123", "Victor", "Marie Hugo", False)
    db_create_autor("88243510", "Brandon", "Sanderson", True)
    db_create_autor("54138722", "Sarah", "Janet Maas", True)
    db_create_autor("31891311", "Kenneth", "Martin Follett", True)
    db_create_autor("11344830", "Alex", "Michaelides", True)
    db_create_autor("24854100J", "Javier", "Castillo", True)
    
    db_create_libro(9788475300566, "El sonido y la furia", "Jonathan Cape", 1929) # isbn, titulo, editorial, año_escrito
    db_create_libro(9788845928178, "Luz de agosto", "Smith & Haas", 1932)
    db_create_libro(9788401031113, "Holly", "PLAZA & JANES", 2023)
    db_create_libro(9788497591508, "El cazador de sueños", "Scribner", 2001)
    db_create_libro(9780752821467, "La milla verde", "New American Library", 1996)
    db_create_libro(9789752119161, "Mr. Mercedes", "Scribner", 2014)
    db_create_libro(9788491041542, "Los miserables", "ALIANZA EDITORIAL", 1862)
    db_create_libro(9788811609599, "Nuestra Señora de París", "ALIANZA EDITORIAL", 1831)
    db_create_libro(9788418037818, "Trenza del mar Esmeralda", "NOVA", 2023)
    db_create_libro(9788408155089, "Una corte de rosas y espinas", "Crossbooks", 2015)
    db_create_libro(9788418359330, "Torre del alba", "HIDRA", 2017)
    db_create_libro(9788401336560, "Un mundo sin fin", "PLAZA & JANES", 2007)
    db_create_libro(9788466351935, "La paciente silenciosa", "DEBOLSILLO", 2019)
    db_create_libro(9788420455488, "Las Doncellas", "ALFAGUARA", 2021)
    db_create_libro(9788491293552, "El cuco de cristal", "Suma", 2023)
    
    db_create_usuario("54318311L", "Francisco", "García Hernández", 2) # dni, nombre, apellidos, numPrestamos
    db_create_usuario("31098132S", "Ana", "Moreno Castillo", 1)
    db_create_usuario("63452270M", "Paco", "Serrano Ortega", 11)
    db_create_usuario("81321354H", "Carla", "Torres Vidal", 3)
    db_create_usuario("24057863N", "Miguel", "Rivera Garrido", 12)
    
    # Hacemos unos selects generales para comprobar que los inserts se hayan realizado correctamente
    db_select_all("autor")
    db_select_all("libro")
    db_select_all("usuario")

    cur.execute("SELECT nombre, apellidos FROM autor WHERE estarVivo = True")
    autores_vivos = cur.fetchall()
    print("\nLos autores que están vivos:")
    for autor_vivo in autores_vivos:
        print("-", autor_vivo[0], autor_vivo[1])
        
    cur.execute("SELECT titulo FROM libro WHERE año_escrito > 1900")
    libros_pos_1900 = cur.fetchall()
    print("\nLos libros escritos posteriormente a 1900:")
    for libro_pos_1900 in libros_pos_1900:
        print("-", libro_pos_1900[0])
    
    cur.execute("SELECT nombre, apellidos FROM usuario WHERE numPrestamos > 10 AND nombre = 'Paco'")
    numPrestamos_superior_10_Paco = cur.fetchall()
    print("\nLos usuarios que se han llevado más de 10 libros y que se llaman Paco:")
    for usuario_requerido in numPrestamos_superior_10_Paco:
        print("-", usuario_requerido[0], usuario_requerido[1])
        
    try:
        con.commit() # Se actualizan los cambios pendientes en la BD
        con.close() # Se cierra la conexión
        
    except:
        con.rollback() # rollback devuelve la bd al último commit
        raise RuntimeError("Ha ocurrido un error ... Volviendo al commit anterior ... ")