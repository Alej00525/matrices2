def suma_matrices(matriz1,matriz2):
 """Función para sumar dos matrices"""
 filas = len(matriz1)
 columnas = len(matriz1[0])
 if filas != len(matriz2) or columnas != len(matriz2[0]):
   print("Error, las matrices no tienen las mismas dimensiones.")
   return None
 else:
   resultado = []
   for i in range(filas):
     fila = []
     for j in range(columnas):
       fila.append(matriz1[i][j] + matriz2[i][j])
     resultado.append(fila)
   return resultado

def multiplicacion_matrices(matriz1,matriz2):
 """Función para multiplicar dos matrices"""
 filas_A = len(matriz1)
 columnas_A = len(matriz1[0])
 filas_B = len(matriz2)
 columnas_B = len(matriz2[0])
 if columnas_A != filas_B:
  print("Error: El número de columnas de A debe ser igual al número de filas de B.")
  return None
 else:
  resultado = []
  for i in range(filas_A):
   fila = []
   for j in range(columnas_B):
    suma = 0
    for k in range(columnas_A):
     suma += matriz1[i][k] * matriz2[k][j]
    fila.append(suma)
   resultado.append(fila)
  return resultado

def productohadamard_matrices(matriz1,matriz2):
 """Función para calcular el producto hadamard de dos matrices"""
 filas = len(matriz1)
 columnas = len(matriz1[0])
 if filas != len(matriz2) or columnas != len(matriz2[0]):
   print("Error: las matrices deben tener las mismas dimensiones")
   return None
 else:
    resultado = []
    for i in range(filas):
      fila = []
      for j in range(columnas):
        fila.append(matriz1[i][j] * matriz2[i][j])
      resultado.append(fila)
 return resultado

def productokronecker_matrices(matriz1,matriz2):
 '''Función para calcular el producto de Kronecker de dos matrices'''
 af = len(matriz1)     # filas matriz a
 ac = len(matriz1[0])  # colum matriz a
 bf = len(matriz2)     # filas matriz b
 bc = len(matriz2[0])  # colum matriz b
 mm = []             # matriz madre la cual estara compuesto de los vectores fila hecho de la matriz resultante2
 for i in range(af):
  mr2 = []           # matriz resultante2 que equivale a un vector fila cuyos componentes son las matrices resultantes1
  for j in range(ac):
   mr1 = []          # matriz resultante1 que equivale a la matriz compuesta por los vectores fila de la forma a[i][j] x B
   for k in range(bf):
    mr = []          # matriz resultante que equivale al vector fila con componentes a[i][j] X b[k][l]
    for l in range(bc):
     cp = matriz1[i][j]*matriz2[k][l]  # componente posicion
     mr.append(cp)
     if l == bc-1:
      mr1.append(mr)
      if k == bf-1:
       mr2.append(mr1)
       if j == ac-1:
        mm.append(mr2)
 mf1 = []
 for i in range(af):
  for k in range(bf):
   mf=[]
   for j in range(ac):
    for l in range(bc):
     mf.append(mm[i][j][k][l])
     if j == ac-1 and l == bc-1:
      mf1.append(mf)
 return mf1
