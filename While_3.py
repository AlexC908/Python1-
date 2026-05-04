# Validacion de Datos y Clausula 

print("\n Ejemplo basico")
intentos = 0 
Max_de_Intentos = 4

while intentos < Max_de_Intentos:
  clave = (input(f"Intentos: {intentos} Ingrese la clave correcta: "))
  if clave == "Python123":
    print("Acceso consededido")
    break

  print("Clave incorrecta")
  intentos += 1   
else :
  print(" As alcanzado max de intentos")