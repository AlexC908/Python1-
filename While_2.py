# Menu interactivo con break y continue 

while True:
  opcion = float(input("Escribe:'hola','salir' o 'saltar'" )).lower()
  if opcion =="salir":
    print("Saliendo del sistema")
    break
  elif opcion =="saltar":
    print("saltando esta parte...")
    continue
print(f"Escribiste:{opcion}")  