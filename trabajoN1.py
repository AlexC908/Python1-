'''Ejercicio 2: Control de Velocidad Pide la velocidad de un coche:
Si es menor a 20: "Muy lento".
Si está entre 20 y 60: "Velocidad moderada".
Si está entre 61 y 120: "Velocidad alta".
Si es mayor a 120: "¡Multa por exceso de velocidad!".'''

velocidad = int(input("¿Cual fue la velocidad de tu vehiculo?: "))

if velocidad < 20:
  print("Muy lento")
elif velocidad >= 21 and velocidad <=60:
  print("Velocidad Moderada")
elif velocidad >= 61 and velocidad <= 119:
  print("Velocidad alta") 
elif velocidad == 120:
  print("Multa por exeso de Velocidad")
else :
  print("No se registro la velocidad de su vehiculo")