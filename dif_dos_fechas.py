from datetime import datetime
from dateutil import relativedelta

from datetime import datetime

fecha_1 = input("Ingrese la primera fecha en dd/mm/aaaa: ")
fecha_2 = input("Ingrese la segunda fecha en dd/mm/aaaa: ")

inicial = datetime.strptime(fecha_1, "%d/%m/%Y")
final =   datetime.strptime(fecha_2, "%d/%m/%Y")

# Obtener el intervalo entre dos fechas, libreria relative delta, permite intervalos restando la final de la inicial
diferencia = relativedelta.relativedelta(final, inicial)

print('El intervalo entre dos años es: ', diferencia.years)

print('La diferencia completa entre los dos datos es: ')
print(diferencia.years , ' años, ', diferencia.months, ' meses y ', diferencia.days, ' días')