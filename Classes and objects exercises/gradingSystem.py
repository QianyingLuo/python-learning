class Alumno():
    '''Clase Alumno
    Incluye el nombre y la nota de un alumno
    
    args
    - nombre: Es un string que compone el nombre del alumno
    - nota: Es un string que compone la nota del alumno
    '''

    # Constructor
    def __init__(self, nombre, nota):
        '''Constructor de la clase Alumno'''
        self.__nombre = nombre
        self.__nota = nota
        print("El alumno se ha creado con éxito.")
        
    # Getters y Setters
    @property
    def nombre(self):
        '''Metodo getter del atributo nombre'''
        print("ESTOY EN EL GETTER")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        '''Metodo setter del atributo nombre'''
        print("ESTOY EN EL SETTER")
        self.__nombre = nuevo
    
    @property
    def nota(self):
        '''Metodo getter del atributo nota'''
        print("ESTOY EN EL GETTER")
        return self.__nota
    
    @nota.setter
    def nota (self, nuevo):
        '''Metodo setter del atributo nota'''
        print("ESTOY EN EL SETTER")
        self.__nota = nuevo
    
    def calificacion(self):
        if 0< self.__nota < 6:
            print("Está suspendido")
        elif 6 <= self.__nota <= 10:
            print("Está aprobado")
        else:
            print("Nota incorrecta")
        
    def __str__ (self):
        '''Metodo __str__() de la clase Alumno. Indica el nombre y la nota del alumno'''
        return " > Nombre: {}\n > Nota: {}".format(self.__nombre, self.__nota)

a1 = Alumno("Pepe", 6)
print(a1)
a1.calificacion()
print(a1.nombre)
a1.nombre = "Andrés"
print(a1.nombre)
print(a1.nota)
a1.nota = "5.5"
print(a1.nota)

a2 = Alumno("Ana", 4)
print(a2)
a2.calificacion()
print(a2.nombre)
a2.nombre = "María"
print(a2.nombre)
print(a2.nota)
a2.nota = "8"
print(a2.nota)