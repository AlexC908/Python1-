print("Escoge un numero entre el 1 y 10")

numero = int(input("Numero: "))

while numero not in range(1,11): 
    print(input("Siga intentando"))
    continue 
if numero in range(1,11):
      print("es correcto")

 