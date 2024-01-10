'''
1) Ejercicio de herencia múltiple y polimorfismo:

Crea la clase Vehiculos con un constructor que incluya marca y modelo
Esta clase Vehiculos también tendrá que incluir un método que se llame repostar() el cual imprima por pantalla "Este vehiculo tiene que repostar gasolina"
Crea la clase VElectricos con un constructor que incluya marca, modelo y autonomia
Esta clase VElectricos también tendrá que incluir un método que se llame repostar() el cual imprima por pantalla "Este vehiculo tiene que repostar electricidad"
Crea la clase BicicletaElectrica que herede de Vehiculos y de VElectricos, pero dando prioridad a VElectricos (ya que es un vehículo más electrico que normal)
Crea la clase Quad que herede de Vehiculos y de VElectricos, pero dando prioridad a Vehiculos (ya que sólo usa la electricidad de modo puntual)
Crear un objeto de BicicletaElectrica y otro de Quad
Emplear las técnicas de polimorfismo aprendidas para conseguir que al peguntarle a los objetos que acabamos de crear por su repostaje, ambos nos respondan adecuadamente
'''

class Vehiculos():
    
    #Constructor
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, nuevaMarca):
        self.__marca = nuevaMarca
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevoModelo):
        self.__modelo = nuevoModelo
    
    def repostar(self):
        print("Este vehiculo tiene que repostar gasolina")

class VElectricos():
    
    #Constructor
    def __init__(self, marca, modelo, autonomia):
        self.__marca = marca
        self.__modelo = modelo
        self.__autonomia = autonomia
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, nuevaMarca):
        self.__marca = nuevaMarca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevoModelo):
        self.__modelo = nuevoModelo
    
    @property
    def autonomia(self):
        return self.__autonomia
    
    @autonomia.setter
    def autonomia(self, nuevaAutonomia):
        self.__autonomia = nuevaAutonomia
    
    def repostar(self):
        print("Este vehiculo tiene que repostar electricidad")
    
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

class Quad(Vehiculos, VElectricos):
    pass

def repostar(vehiculo):
    vehiculo.repostar()

miBici = BicicletaElectrica("Orbea", "Vibe H10", "18km")
repostar(miBici)
miQuad = Quad("YAMAHA", "YFM90R")
repostar(miQuad)

'''
2) Ejercicio de herencia

Crea la superclase Personal_Universitario con un único atributo que sea un diccionario que incluya: "id", "nombre" y "email"
Crear la clases Oficina, Profesor y Alumno. Todas ellas heredaran de Personal_Universitario y heredaran sus datos
En el caso de Oficina, debe añadir a su diccionario de datos el dato "Puesto"
En el caso de Profesor, debe añadir a su diccionario de datos el dato "Especialización"
En el caso de Alumno, debe añadir a su diccionario de datos el dato "CreditosAprobados" (integer)
Crear métodos que sirvan para mostrar la información de cada clase
Crear objetos de todas las clases
Mostrar la información de esos objetos y comprobar que sale lo que tiene que salir
'''

class Personal_Universitario():
        
    def __init__(self, datos=None):
        self.datos = {}
        self.datos["id"] = datos["id"]
        self.datos["nombre"] = datos["nombre"]
        self.datos["email"] = datos["email"]
        
    def __str__(self):
        return '''
        Id: {}
        Nombre: {}
        Email: {}
        '''.format(self.datos["id"], self.datos["nombre"], self.datos["email"])

class Oficina(Personal_Universitario):
    
    def __init__(self, datos, puesto):
        super().__init__(datos)
        self.datos["puesto"] = puesto
        
    def __str__(self):
        return super().__str__() + '''Puesto: {}\n'''.format(self.datos["puesto"])

class Profesor(Personal_Universitario):
    
    def __init__(self, datos, especializacion):
        super().__init__(datos)
        self.datos["especializacion"] = especializacion
    
    def __str__(self):
        return super().__str__() + '''Especialización: {}\n'''.format(self.datos["especializacion"])

class Alumno(Personal_Universitario):
    
    def __init__(self, datos, creditos:int):
        super().__init__(datos)
        self.datos["creditosAprobados"] = creditos

    def __str__(self):
        return super().__str__() + '''Creditos Aprobados: {}\n'''.format(self.datos["creditosAprobados"])

# Creo diccionario para cada personal universitario
persona1 = {"id": "15345", "nombre":"Jose", "email":"jose@gmail.com"}
persona2 = {"id": "18307", "nombre":"Ana", "email":"ana@gmail.com"}
persona3 = {"id": "19153", "nombre":"Marina", "email":"marina@gmail.com"}

# Creo objetos de todas las clases
oficinista = Oficina(persona1, "Administrativo")
profesor = Profesor(persona2, "Geografía")
alumno = Alumno(persona3, 300)
print(oficinista)
print(profesor)
print(alumno)

'''
3) Escoge la temática que prefieras y define una estructura de clases y subclases donde practiques la herencia en al menos dos niveles (herencia multi nivel). 
Crea una estructura de mínimo 5 clases, con sus respectivos constructores y métodos. Crea algunos objetos y comprueba que la herencia este funcionando. 
Si puedes, incluye alguna técnica de polimorfismo.
'''
class Producto():
    
    def __init__(self, referencia, nombre, pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
    
    def __str__(self):
        return '''\
Referencia\t{}
Nombre\t\t{}
PVP\t\t{}\n'''.format(self.referencia, self.nombre, self.pvp)

class Mueble(Producto):
    
    def __init__(self, referencia, nombre, pvp, material):
        super().__init__(referencia, nombre, pvp)
        self.material = material
    
    def __str__(self):
        return super().__str__() + '''\
Material\t{}\n'''.format(self.material)
    
class Iluminacion(Producto):
    
    def __init__(self, referencia, nombre, pvp, colorLuz):
        super().__init__(referencia, nombre, pvp)
        self.colorLuz = colorLuz
    
    def __str__(self):
        return super().__str__() + '''\
Color de luz\t{}\n'''.format(self.colorLuz)

class Mesa(Mueble):
    
    def __init__(self, referencia, nombre, pvp, material, forma):
        super().__init__(referencia, nombre, pvp, material)
        self.forma = forma
    
    def __str__(self):
        return super().__str__() + '''\
Forma\t\t{}\n'''.format(self.forma)

class Lampara(Iluminacion):
    
    def __init__(self, referencia, nombre, pvp, colorLuz, posicion):
        super().__init__(referencia, nombre, pvp, colorLuz)
        self.posicion = posicion
    
    def __str__(self):
        return super().__str__() + '''\
Posicion\t{}\n'''.format(self.posicion)
    
listaCompra = []

# Creamos una función para añadir productos a la lista
def anadirLista(producto):
    listaCompra.append(producto)
    print("Producto:",type(producto).__name__,"{} añadido a la lista de compra\n".format(producto.nombre))
    

tarjetaSocio = Producto("001", "Tarjeta de Socio", 1)
print(tarjetaSocio)
anadirLista(tarjetaSocio)

mueble = Mueble("2431", "KALLAX", 78, "Madera")
print(mueble)
anadirLista(mueble)

mesa = Mesa("3248", "MICKE", 50, "Tablero de fibras", "Rectangular")
print(mesa)
anadirLista(mesa)

iluminacion = Iluminacion("2614", "LAUTERS", 52, "Amarillo calido")
print(iluminacion)
anadirLista(iluminacion)

lampara = Lampara("3650", "RANARP", 60, "Blanco", "de Pie")
print(lampara)
anadirLista(lampara)