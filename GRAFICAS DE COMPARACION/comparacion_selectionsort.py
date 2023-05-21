import matplotlib.pyplot as plt
# Leer los tiempos de ejecución de Python desde el archivo
tiempos_python = []
with open("TIEMPOS\\tiempos_selectionsort_python.txt", "r") as archivo_tiempo_python:
    for linea in archivo_tiempo_python:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_python.append(tiempo)

# Leer los tiempos de ejecución de C++ desde el archivo
tiempos_cmasmas = []
with open("TIEMPOS\\tiempos_selectionsort_c++.txt", "r") as archivo_tiempo_cmasmas:
    for linea in archivo_tiempo_cmasmas:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_cmasmas.append(tiempo)

# Tamaños de archivos correspondientes a los tiempos
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

plt.plot(tiempos_python,label='Python')
plt.plot(tiempos_cmasmas,label='C++')
plt.xlabel('Tamaños de archivos')  #nota: la etiqueta si aparece en la grafica pero en pantalla completa
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución del algoritmo SELECTION SORT')
plt.legend()
plt.xticks(range(len(tamanos)),tamanos,rotation=45)
plt.grid(True)
plt.show()