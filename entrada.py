def ingresar_matriz():
 """Función para ingresar una matriz por teclado"""
 while True:
  try:
   filas = int(input("Ingrese el número de filas: "))
   if filas < 1:
    raise ValueError
   columnas = int(input("Ingrese el número de columnas: "))
   if columnas < 1:
    raise ValueError
   break
  except ValueError:
   print("Error: la cantidad de filas y columnas deben ser numeros enteros positivos.")
 matriz = []
 for i in range(filas):
   while True:
    try:
     fila = list(map(float, input(f"Ingrese la fila {i+1} separada por espacios: ").split()))
     if len(fila) != columnas:
      print(f"Error: debe ingresar exactamente {columnas} valores.")
     else:
      matriz.append(fila)
      break
    except ValueError:
     print("Error: debe ingresar solo números.")
 return matriz

def imprimir_matriz(matriz):
 """Función para imprimir una matriz"""
 try:
  for i in range(len(matriz)):
   print(matriz[i])
 except TypeError or ValueError:
   return None
