# Selector de clima 
print("Hola,¿como se encuentra el clima el dia de hoy?")
respuesta = input("respuesta :").lower()


match respuesta:
   case "soleado":
    print(respuesta,"le recomendamos usar gorro y protector solar")
   case"lluvioso":
    print(respuesta,"le recomendamos usar abrigo y tomarse un cafe caliente")
   case"nublado":
    print(respuesta,"Le recomendamos tener en manos una sombrilla")
   case"nevado":
    print(respuesta,"le recomendamos usar un buen abrigo y tomar chocolate caliente en familia")
   case _:
      print("No se reconoce ese clima")