
'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
'''

from cuenta import Cuenta
from persona import Persona


#Comienza porgrama tarjeta joven creanado objeto hereda de Cuenta

class CuentaJoven(Cuenta):
    #inicializo contructor
	def __init__(self, cuenta, bonificacion):
            self.cuenta = cuenta
            self.bonificacion = bonificacion
            
            
      #Bonificacion setter
      
            def set_bonificacion(self, bonificacion):
              self.titular = bonificacion
                 
    
#Programa cuenta
edad_titular = True

edad_titular = int(input("Ingresa tu edad: "))
if edad_titular >= 18 and edad_titular <= 35:
      print("Eres beneficiario de cuenta Joven")
else:
      print("No eres beneficiario del programa Cuenta Joven")