
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
      
            def get_bonificacion(self):
              return self.bonificacion
              
            def set_bonificacion(self, bonificacion):
              self.bonificacion = bonificacion
                 
            def es_titular_valido(self):
              edad_titular = self.calcular_edad() 
              return 18 <= edad_titular < 25   
                  
                  
            def retirar(self, cantidad):
                  if self.es_titular_valido() and cantidad <= self.cantidad:
                        self.cantidad -= cantidad
                        return True
                  else:
                        return False
                  
            def mostrar(self):
                  return f'Tienes beneficio de Cuenta Joven'(self.bonificacion)