#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdio>
using namespace std;


void quick_sort(vector<int>& lista, int inicio, int fin) {
    if (inicio < fin) {
        int pivot = lista[fin];
        int i = inicio - 1;
        for (int j = inicio; j <= fin - 1; j++) {
            if (lista[j] < pivot) {
                i++;
                swap(lista[i], lista[j]);
            }
        }
        swap(lista[i + 1], lista[fin]);
        int pivot_index = i + 1;
        quick_sort(lista, inicio, pivot_index - 1);
        quick_sort(lista, pivot_index + 1, fin);
    }
}

int main() {
    // Defino una lista de tamaños de datos para generar
    vector<int>tamanos= {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

    // Generar archivos para cada tamaño de datos
    
	ofstream archivo_tiempo("tiempos_quicksort_c++.txt"); // Archivo para guardar los tiempos de ejecucion
    
	for (int tamano : tamanos) {
        // Leer el archivo y obtener los numeros aleatorios
        vector<int> numeros_aleatorios;
        
        ifstream archivo("datos_"+ to_string(tamano) +".txt");
        int numero;
        while(archivo >> numero) {
            numeros_aleatorios.push_back(numero);
        }
        archivo.close();

        // Ordenar los numeros aleatorios (TOMANDO EL TIEMPO DE EJECUCION)
        clock_t tiempo_inicio = clock();
        quick_sort(numeros_aleatorios, 0,numeros_aleatorios.size()-1);
        clock_t tiempo_fin = clock();
        double tiempo_ejecucion = double(tiempo_fin - tiempo_inicio) / CLOCKS_PER_SEC;

        // Guardar los numeros ordenados en un nuevo archivo
        
		ofstream archivo_ordenado("datos_" + to_string(tamano) + "_ordenados QUICK SORT C++.txt");
        for (int numero : numeros_aleatorios) {
            archivo_ordenado<<numero<< endl;
        }
        archivo_tiempo<< "Archivo "<<to_string(tamano)<< ": "<< tiempo_ejecucion<< " segundos"<< endl;
        archivo_ordenado.close();
        
		string nombre_archivo = "datos_" + to_string(tamano) + ".txt";
        remove(nombre_archivo.c_str());
    }
	archivo_tiempo.close();
	return 0;
}
