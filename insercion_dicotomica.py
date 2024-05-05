"""
Algoritmo de ordenación por inserción dicotómica

Especificaciones del algoritmo:
Precondición:
- La tabla t debe contener elementos comparables.
- La tabla t no debe estar vacía.
Postcondición:
- Después de la ejecución del algoritmo, la tabla t estará ordenada en orden creciente.

Análisis completo:
En la ordenación por inserción dicotómica, se utiliza una estrategia de búsqueda binaria 
para encontrar la posición de inserción de cada elemento en la tabla. 
Esto reduce el número de comparaciones necesarias en comparación con la inserción estándar, 
lo que resulta en una mejor eficiencia en términos de tiempo.

Algoritmo:
1. Para cada índice i desde 1 hasta el tamaño de la tabla - 1:
   a. Definir el elemento actual como t[i].
   b. Definir el índice de inserción como i.
   c. Para cada índice j desde i - 1 hasta 0, mientras j >= 0:
      i. Calcular el índice medio mid entre insert_index y j.
      ii. Si t[mid] > actual, actualizar el índice de inserción a mid.
      iii. Si t[mid] <= actual, actualizar el índice de inserción a mid + 1.
   d. Si el índice de inserción no es igual a i:
      i. Eliminar el elemento actual de la tabla.
      ii. Insertar el elemento actual en la posición de inserción.

"""


#ejemplo de algoritmo con ordenacioon poor insercioon dicotomica
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        insert_index = i
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > current:
                insert_index = mid
                high = mid - 1
            else:
                low = mid + 1

        if insert_index != i:
            arr.pop(i)
            arr.insert(insert_index, current)

#solicitar al usuario que ingrese los elementos de la lista para ordenar
input_string = input("Ingrese los elementos de la lista separados por espacios: ")
unsorted_array = list(map(int, input_string.split()))

print("Array original:", unsorted_array)

binary_insertion_sort(unsorted_array)
print("Array ordenado por inserción dicotómica:", unsorted_array)
