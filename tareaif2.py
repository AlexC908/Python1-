'''Ejercicio 1: El Clasificador de Triángulos Pide al usuario las longitudes de los tres lados de un triángulo.
Si los tres lados son iguales: "Equilátero".
Si solo dos son iguales: "Isósceles".
Si todos son diferentes: "Escaleno".'''

print("Cual son las longuitudes de tu triangulo?")

lado1 = str(input("lado 1: "))
lado2 = str(input("lado 2: "))
lado3 = str(input("lado 3: "))

if lado1 == lado2 and lado2 == lado3:
  print("Tu triangulo es Equilatero")
elif lado1 == lado2 and lado2 != lado3:
  print("Tu triangulo es Isoseles")
elif lado1 != lado2 and lado2 != lado3:
  print("tu triangulo es Escaleno")
else:
  print("No existe ese triangulo")