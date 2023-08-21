#Escribir una función que calcule el máximo común divisor entre dos números

def mcd(x, y):
    if x < y:
        return mcd(y, x)

    while y != 0:
        x, y = y, x % y

    return x

print(mcd(45, 90))

#Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm(num1, num2):
    num3 = max(num1, num2)
    
    while True:
        if (num3 % num1  == 0) and (num3 % num2 == 0):
            return num3
        num3 += 1 #evalua el siguiente numero entero

print(mcm(32,68))
print(mcm(56,90))

'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

def cont_palabras(texto):
    '''
    Funcion: Contar el Número de veces que aparece cada palabra en el texto.
    Parámetros:
        text: Es la cadena de caracteres.
    Retorna: 
        Un diccionario con pares palabra:frecuencia.
    '''
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_repetidas(palabras):
    max_palabras = ''
    max_freq = 0
    for palabras, freq in palabras.items():
        if freq > max_freq:
            max_palabras = palabras
            max_freq = freq
    return max_palabras, max_freq

texto = 'Tanjiro: Vive con orgullo. Si te vence tu debilidad, calienta tu corazón, aprieta los dientes y sigue adelante. Dile a mi padre que cuide su salud'

print(cont_palabras(texto))
print(mas_repetidas(cont_palabras(texto)))


'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''

def get_int():
    while True:
        try:
            ingreso_num = input("Ingresa un numero entero: ")
            valor_entero = int(ingreso_num)
            return valor_entero  
        except ValueError:
            print("Ingresa un valor válido") 
        
        
resultado = get_int()
print("El valor entero ingresado es: ", resultado)

