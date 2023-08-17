'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad

'''


class Persona():
    def __init__(self, nombre, edad, dni):
        
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
        
    def __str__(self):
        return f'{self.nombre}, {self.edad}, {self.dni}'

#getters
       
def get_nombre(self):
    return self.nombre

def get_edad(self):
    return self.edad

def get_dni(self):
    return self.dni

#setters

def set_nombre(self, nombre):
      self.nombre = nombre
      
def set_nombre(self, edad):
      self.nombre = edad
      
def set_dni(self, dni):
      self.nombre = dni
      
#Calcular si es mayor de edad

def Es_mayor_de_edad(self):
    return self.edad >= 18

#Bloque principal
#Ingreso de datos

nombre:str = input('Ingrese su nombre: ')

dni:int = input('Ingrese su dni: ')
if len(dni) != 8:
    print("Longitud de dni no válida")
else:
    print("Acceso válido")

edad = int(input('Ingrese su edad: ')) 

#Creo una instancia de persona
persona = Persona(nombre, edad, dni) 

#Verificar si es mayor
if persona.Es_mayor_de_edad():
    print("Eres mayor de edad")
else:
    print("Acceso no permitido, eres menor de edad")
    
#Imprimo los datos usando str
    
print(persona)