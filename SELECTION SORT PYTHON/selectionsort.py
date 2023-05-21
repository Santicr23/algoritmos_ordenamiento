import os
import time


# Defino una lista de tamaños de datos para generar
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Función de ordenamiento selection sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j
        lista[i], lista[min_indice] = lista[min_indice], lista[i]
    return lista

# Generar archivos para cada tamaño de datos y crear archivo de tiempo de cada tamaño
with open("SELECTION SORT PYTHON/tiempos_selectionsort_python.txt", "w") as archivo_tiempo:
    for tamano in tamanos:
        # Leer el archivo y obtener los números aleatorios
        with open(f"SELECTION SORT PYTHON/datos_{tamano}.txt", "r") as archivo:
            numeros_aleatorios = [int(linea.strip()) for linea in archivo.readlines()]
        
        # Ordenar los números aleatorios (TOMANDO EL TIEMPO DE EJECUCION)
        tiempo_inicio = time.time()
        numeros_ordenados = selection_sort(numeros_aleatorios)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        
        # Guardar los números ordenados en un nuevo archivo
        with open(f"SELECTION SORT PYTHON/datos_{tamano}_ordenados SELECTION SORT PYTHON.txt", "w") as archivo_ordenado:
            for numero in numeros_ordenados:
                archivo_ordenado.write(str(numero) + "\n")
            
            
        archivo_tiempo.write(f"Archivo {tamano}: {tiempo_ejecucion} segundos\n")
        nombre_archivo = f"SELECTION SORT PYTHON/datos_{tamano}.txt"
        os.remove(nombre_archivo)
