import importlib
import entrada as ent
import operaciones_matrices as mtc
import menu
importlib.reload(ent)
importlib.reload(mtc)
importlib.reload(menu)
opcion = 0
while True:
 if opcion == 6:
   break
 else:
  print('Elige las matrices:')
  print('La matriz 1 sera:')
  matriz1 = ent.ingresar_matriz()
  print('')
  print('La martriz 2 sera:')
  matriz2 = ent.ingresar_matriz()
  print('')
  while True:
   opcion = menu.mostrar_menu()
   if opcion == 1:
    print('Resultado:')
    {ent.imprimir_matriz(mtc.suma_matrices(matriz1,matriz2))}
    print('')
   elif opcion == 2:
    print('Resultado:')
    {ent.imprimir_matriz(mtc.multiplicacion_matrices(matriz1,matriz2))}
    print('')
   elif opcion == 3:
    print('Resultado:')
    {ent.imprimir_matriz(mtc.productohadamard_matrices(matriz1,matriz2))}
    print('')
   elif opcion == 4:
    print('Resultado:')
    {ent.imprimir_matriz(mtc.productokronecker_matrices(matriz1,matriz2))}
    print('')
   elif opcion == 5:
    print('')
    break
   elif opcion == 6:
    print('Adios!!')
    break
