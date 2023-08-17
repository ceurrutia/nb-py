
'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.

'''

class Cuenta():
        #inicializo clase
        def __init__(self, titular, cantidad=0):
            self.titular = titular
            self.cantidad = cantidad
         

        #Invoco metodos get y set
        
        def get_titular(self):
              return self.titular
        
        def set_titular(self, titular):
              self.titular = titular
                
        
        def get_cantidad(self):
              return self.cantidad
        
        def set_cantidad(self, cantidad):
              self.cantidad = cantidad
        
        
        #Mostrar los datos con formato f
        def mostrar(self):
            print(f' Titular: {self.titular}') 
            print(f'Cantidad: {self.cantidad}')
        
        #Ingreso de cantidadse suma al 0 o a la inicial

        def ingresar(self, cantidad):
              if cantidad > 0:
                    self.cantidad += cantidad

       #Retiro de cantidad, resto la cantidad dada de la actual de la cuenta
        def retirar(self, cantidad):
            self.cantidad -= cantidad
       
       #Craeo una instancia de cuenta
cuenta1 = Cuenta("Cecilia Urrutia", 3000)
            
cuenta1.mostrar()
cuenta1.ingresar(4000)
cuenta1.retirar(2000)
            
cuenta1.mostrar()