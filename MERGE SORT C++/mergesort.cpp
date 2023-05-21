#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdio>
using namespace std;

void merge_sort(vector<int>& lista, int inicio, int fin);
void merge(vector<int>& lista, int inicio, int mitad, int fin);
// Función de ordenamiento Merge sort
void merge_sort(vector<int>& lista, int inicio, int fin) {
    if (inicio < fin) {
        int mitad = inicio + (fin - inicio) / 2;
        merge_sort(lista, inicio, mitad);
        merge_sort(lista, mitad + 1, fin);
        merge(lista, inicio, mitad, fin);
    }
}

void merge(vector<int>& lista, int inicio, int mitad, int fin) {
    int n1 = mitad - inicio + 1;
    int n2 = fin - mitad;

    vector<int> izquierda(n1);
    vector<int> derecha(n2);

    for (int i = 0; i < n1; i++) {
        izquierda[i] = lista[inicio + i];
    }
    for (int j = 0; j < n2; j++) {
        derecha[j] = lista[mitad + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = inicio;

    while (i < n1 && j < n2) {
        if (izquierda[i] <= derecha[j]) {
            lista[k] = izquierda[i];
            i++;
        } else {
            lista[k] = derecha[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        lista[k] = izquierda[i];
        i++;
        k++;
    }

    while (j < n2) {
        lista[k] = derecha[j];
        j++;
        k++;
    }
}

int main() {
    // Defino una lista de tamaños de datos para generar
    vector<int>tamanos= {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

    // Generar archivos para cada tamaño de datos
    
	ofstream archivo_tiempo("tiempos_mergesort_c++.txt"); // Archivo para guardar los tiempos de ejecucion
    
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
        merge_sort(numeros_aleatorios, 0, numeros_aleatorios.size() - 1);
        clock_t tiempo_fin = clock();
        double tiempo_ejecucion = double(tiempo_fin - tiempo_inicio) / CLOCKS_PER_SEC;

        // Guardar los numeros ordenados en un nuevo archivo
        
		ofstream archivo_ordenado("datos_" + to_string(tamano) + "_ordenados MERGE SORT C++.txt");
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
