import random


# Definir la lista de tamaños de datos para generar
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000,7000,8000,9000,10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Generar archivos para cada tamaño de datos
for tamano in tamanos:
    # Generar una lista de números aleatorios
    numeros_aleatorios = [random.randint(0, 100) for _ in range(tamano)]
    
    # Crear el archivo y escribir los números aleatorios
    with open(f"datos_{tamano}.txt", "w") as archivo:
        for numero in numeros_aleatorios:
            archivo.write(str(numero) + "\n")

