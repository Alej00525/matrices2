def mostrar_menu():
 print("\n--- MENU DE OPERACIONES CON MATRICES ---")
 print("1. Suma de matrices")
 print("2. Multiplicación de matrices")
 print("3. Producto de Hadamard")
 print("4. Producto de Kronecker")
 print("5. Cambiar las matrices")
 print("6. Salir")
 while True:
  try:
   opcion = int(input("Seleccione una opción: "))
   if opcion in [1, 2, 3, 4, 5,6]:
    return opcion
   else:
    print("Error: opción no válida.")
  except ValueError:
    print('Error: opción no válida')
