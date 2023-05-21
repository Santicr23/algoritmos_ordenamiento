#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdio>
using namespace std;

// Función de ordenamiento Heap Sort
void heapify(vector<int>& lista, int n, int i){
    int padre = i;
    int izquierda= 2 * i + 1;
    int derecha= 2 * i + 2;

    if(izquierda < n && lista[izquierda]> lista[padre]){
        padre = izquierda;
    }

    if(derecha < n && lista[derecha]> lista[padre]){
        padre = derecha;
    }

    if(padre != i){
        swap(lista[i],lista[padre]);
        heapify(lista,n, padre);
    }
}

void heapSort(vector<int>& arr){
    int n= arr.size();

    for(int i= n/2 - 1; i>= 0; i--){
        heapify(arr, n, i);
    }

    for(int i= n-1; i>= 0; i--){
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    // Defino una lista de tamaños de datos para generar
    vector<int> tamanos = {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

    // Generar archivos para cada tamaño de datos
    ofstream archivo_tiempo("tiempos_heapsort_c++.txt"); // Archivo para guardar los tiempos de ejecución

    for (int tamano : tamanos){
        // Leer el archivo y obtener los números aleatorios
        vector<int> numeros_aleatorios;
        ifstream archivo("datos_" + to_string(tamano) + ".txt");
        int numero;
        while(archivo >> numero){
            numeros_aleatorios.push_back(numero);
        }
        archivo.close();

        // Ordenar los números aleatorios (TOMANDO EL TIEMPO DE EJECUCIÓN)
        clock_t tiempo_inicio = clock();
        heapSort(numeros_aleatorios);
        clock_t tiempo_fin = clock();
        double tiempo_ejecucion = double(tiempo_fin - tiempo_inicio) / CLOCKS_PER_SEC;

        // Guardar los números ordenados en un nuevo archivo
        ofstream archivo_ordenado("datos_" + to_string(tamano) + "_ordenados HEAPSORT C++.txt");
        for (int numero : numeros_aleatorios) {
            archivo_ordenado << numero << endl;
        }
        archivo_tiempo<< "Archivo "<< to_string(tamano)<< ": "<< tiempo_ejecucion<<" segundos"<< endl;
        archivo_ordenado.close();
        
        string nombre_archivo = "datos_" + to_string(tamano) + ".txt";
        remove(nombre_archivo.c_str());
    }

    archivo_tiempo.close();
    return 0;
}

