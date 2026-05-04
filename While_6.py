# Segundo ejercicio. Login de usuario. Pide al usuario y contraseña validando con una tupla. Credencial = "admin, comilla, coma, comilla 1234, coma, comilla. Usa while para repetir hasta que acierte.

credendicial = ("admin","1234")

while True:
  usuario = str(input("Usuario :"))
  clave = (input("contrseña :"))
  if (usuario,clave) == credendicial:
    print("Accseso consedido")
    break
  else :
    print ("siga intentando ")