import os
import time

# Defino una lista de tamaños de datos para generar
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Función de ordenamiento Merge sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    # Combinar las dos mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i< len(izquierda) and j < len(derecha):
        if izquierda[i]< derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

# Generar archivos para cada tamaño de datos y crear archivo de tiempo de cada tamaño
with open("MERGE SORT PYTHON/tiempos_mergesort_python.txt", "w") as archivo_tiempo:
    for tamano in tamanos:
        # Leer el archivo y obtener los números aleatorios
        with open(f"MERGE SORT PYTHON/datos_{tamano}.txt", "r") as archivo:
            numeros_aleatorios = [int(linea.strip()) for linea in archivo.readlines()]

        # Ordenar los números aleatorios (TOMANDO EL TIEMPO DE EJECUCION)
        tiempo_inicio = time.time()
        numeros_ordenados = merge_sort(numeros_aleatorios)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        # Guardar los números ordenados en un nuevo archivo
        with open(f"MERGE SORT PYTHON/datos_{tamano}_ordenados MERGE SORT PYTHON.txt", "w") as archivo_ordenado:
            for numero in numeros_ordenados:
                archivo_ordenado.write(str(numero) + "\n")

        archivo_tiempo.write(f"Archivo {tamano}: {tiempo_ejecucion} segundos\n")
        nombre_archivo = f"MERGE SORT PYTHON/datos_{tamano}.txt"
        os.remove(nombre_archivo)
