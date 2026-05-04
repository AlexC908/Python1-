#             Clasificador de edades y Descuentos

# ask  al user su age y si tiene carnet de estudiante (si/no)
#·si es menor de 18 años, imprimir "Precio infantil"
# si tiene entre 18 y 65 años:
# si tiene carnet de estudiante, imprimir "Descuento de estudianter aplicado"
# Si no tiene carnet, imprimir "Precio adulto estandar"
# si tiene mas de 65, imprime "Precio tercera edad " 

print('Cual es tu edad y tienes credencial de estudinte?')

edad = int(input("tu edad: "))

if edad <= 18 :
  print("Precio infantil")
elif edad > 18 and edad < 65: 
  carnet = input("Tienes carnet de estudiante?: ")
  if carnet == "si":
    print("Descuento de estudiante aplicado")
  elif carnet == "no":
    print("Precio adulto Estandar")
elif edad >= 65:
  print("Precio Tercera edad")    
else :
  print("Usted no es un humano")  