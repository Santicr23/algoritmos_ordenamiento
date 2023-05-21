import matplotlib.pyplot as plt

tiempos_bubble= []
with open("TIEMPOS\\tiempos_bubblesort_c++.txt", "r") as archivo_tiempo_bubble:
    for linea in archivo_tiempo_bubble:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_bubble.append(tiempo)

tiempos_counting = []
with open("TIEMPOS\\tiempos_countingsort_c++.txt", "r") as archivo_tiempo_counting:
    for linea in archivo_tiempo_counting:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_counting.append(tiempo)

tiempos_heap = []
with open("TIEMPOS\\tiempos_heapsort_c++.txt", "r") as archivo_tiempo_heap:
    for linea in archivo_tiempo_heap:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_heap.append(tiempo)

tiempos_insertion = []
with open("TIEMPOS\\tiempos_insertionsort_c++.txt", "r") as archivo_tiempo_insertion:
    for linea in archivo_tiempo_insertion:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_insertion.append(tiempo)

tiempos_merge = []
with open("TIEMPOS\\tiempos_mergesort_c++.txt", "r") as archivo_tiempo_merge:
    for linea in archivo_tiempo_merge:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_merge.append(tiempo)


tiempos_quick = []
with open("TIEMPOS\\tiempos_quicksort_c++.txt", "r") as archivo_tiempo_quick:
    for linea in archivo_tiempo_quick:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_quick.append(tiempo)

tiempos_selection = []
with open("TIEMPOS\\tiempos_selectionsort_c++.txt", "r") as archivo_tiempo_selection:
    for linea in archivo_tiempo_selection:
        tiempo = float(linea.split(":")[1].strip().split()[0])
        tiempos_selection.append(tiempo)


# Tamaños de archivos correspondientes a los tiempos
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]


plt.plot(tiempos_bubble,label='Bubble Sort')
plt.plot(tiempos_counting,label='Counting Sort')
plt.plot(tiempos_heap,label='Heap Sort')
plt.plot(tiempos_insertion,label='Insertion Sort')
plt.plot(tiempos_merge,label='Merge Sort')
plt.plot(tiempos_quick,label='Quick Sort')
plt.plot(tiempos_selection,label='Selection Sort')

plt.xlabel('Tamaños de archivos')  #nota: la etiqueta si aparece en la grafica pero en pantalla completa
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de los algoritmos de ordenamiento en C++')
plt.legend()
plt.xticks(range(len(tamanos)),tamanos,rotation=45)
plt.grid(True)
plt.show()