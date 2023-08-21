
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

#Comienza porgrama tarjeta joven creanado objeto que hereda de Cuenta

class CuentaJoven(Cuenta):
    #inicializo contructor
	def __init__(self, edad, cantidad, bonificacion):
            self.cuenta = cantidad
            self.bonificacion = bonificacion
            
            
      #Bonificacion getter
      
            def get_bonificacion(self):
              return self.bonificacion
        
      #Bonificacion setter
              
            def set_bonificacion(self, bonificacion):
              self.bonificacion = bonificacion
                 
            def es_titular_valido(self):
              if edad < 25 and edad > 18:
                  return True
              else:
                  return False 
                  
                  
            def retirar(self, cantidad):
                  if self.es_titular_valido():
                        super().retirar(cantidad)
                  else:
                        print('No eres titular valido para retirar: ', cantidad)
                  
            def mostrar(self):
                  print('Cuenta Joven', cantidad)
                  print('Bonificacion:', bonificacion)
            
#Creo una instancia de Cuenta Joven
CuentaJoven = CuentaJoven(edad=24, cantidad=2000, bonificacion=30)

cantidad_a_retirar = 300
CuentaJoven.retirar(cantidad_a_retirar)
print(CuentaJoven.get_cantidad, CuentaJoven.get_bonificacion)


