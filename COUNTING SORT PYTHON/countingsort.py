import os
import time


# Defino una lista de tamaños de datos para generar
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Función de counting sort
def counting_sort(lista):
    max_valor = max(lista) + 1
    count = [0] * max_valor

    for num in lista:
        count[num] += 1

    ordenada = []
    for i in range(max_valor):
        ordenada.extend([i] * count[i])

    return ordenada


# Generar archivos para cada tamaño de datos y crear archivo de tiempo de cada tamaño
with open("COUNTING SORT PYTHON/tiempos_countingsort_python.txt", "w") as archivo_tiempo:
    for tamano in tamanos:
        # Leer el archivo y obtener los números aleatorios
        with open(f"COUNTING SORT PYTHON/datos_{tamano}.txt", "r") as archivo:
            numeros_aleatorios = [int(linea.strip()) for linea in archivo.readlines()]
        
        # Ordenar los números aleatorios (TOMANDO EL TIEMPO DE EJECUCION)
        tiempo_inicio = time.time()
        numeros_ordenados = counting_sort(numeros_aleatorios)
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        
        # Guardar los números ordenados en un nuevo archivo
        with open(f"COUNTING SORT PYTHON/datos_{tamano}_ordenados COUNTING SORT PYTHON.txt", "w") as archivo_ordenado:
            for numero in numeros_ordenados:
                archivo_ordenado.write(str(numero) + "\n")
            
            
        archivo_tiempo.write(f"Archivo {tamano}: {tiempo_ejecucion} segundos\n")
        nombre_archivo = f"COUNTING SORT PYTHON/datos_{tamano}.txt"
        os.remove(nombre_archivo)

        