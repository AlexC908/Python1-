# El validador de contraseña
#Crea un programa que pida un nombre y una contraseña
# Si el nomnbre de usuario es "admin" y la contraseña es "1234" imprimir accseso total
# Si el usuariom es "invitado" y la contraseñs es "hola", imprimir "Acceso limitado"
# En cualquier otro caso, imprimir "Datos incorrectos "

print("Cual es tu nombre de usuario y contraseña?")

usuario = (input("su usuario : "))
clave = (input("Ingrese su contraseña: "))

nombre1 = "admin"
contraseña1 = "1234"

nombre2 = "invitado"
contraseña2 = "hola"
 
if usuario == nombre1 and clave == contraseña1:
   print("Acceso total")
elif usuario == nombre2 and clave == contraseña2:
   print("Acceso limitado")
else :
   print("Datos incorrectos")