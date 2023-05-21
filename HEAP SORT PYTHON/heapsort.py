import os
import time


# Defino una lista de tamaños de datos para generar
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Función de ordenamiento de burbuja
def heapify(lista, n, i):
    # función auxiliar que reorganiza el heap
    padre = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and lista[padre] < lista[izquierda]:
        padre = izquierda

    if derecha < n and lista[padre] < lista[derecha]:
        padre = derecha

    if padre != i:
        lista[i], lista[padre] = lista[padre], lista[i]
        heapify(lista, n, padre)

def heap_sort(lista):
    n = len(lista)

    # Construir el heap máximo
    for i in range(n, -1, -1):
        heapify(lista, n, i)

    # Extraer los elementos uno por uno
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista


# Generar archivos para cada tamaño de datos y crear archivo de tiempo de cada tamaño
with open("HEAP SORT PYTHON/tiempos_heapsort_python.txt", "w") as archivo_tiempo:
    for tamano in tamanos:
        # Leer el archivo y obtener los números aleatorios
        with open(f"HEAP SORT PYTHON/datos_{tamano}.txt", "r") as archivo:
            numeros_aleatorios = [int(linea.strip()) for linea in archivo.readlines()]
        
        # Ordenar los números aleatorios (TOMANDO EL TIEMPO DE EJECUCION)
        tiempo_inicio = time.time()
        numeros_ordenados = heap_sort(numeros_aleatorios)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        
        # Guardar los números ordenados en un nuevo archivo
        with open(f"HEAP SORT PYTHON/datos_{tamano}_ordenados HEAPSORT PYTHON.txt", "w") as archivo_ordenado:
            for numero in numeros_ordenados:
                archivo_ordenado.write(str(numero) + "\n")       
        archivo_tiempo.write(f"Archivo {tamano}: {tiempo_ejecucion} segundos\n")
        nombre_archivo = f"HEAP SORT PYTHON/datos_{tamano}.txt"
        os.remove(nombre_archivo)


    

