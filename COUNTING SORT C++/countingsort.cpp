#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdio>
#include <algorithm>
using namespace std;


// Función de ordenamiento Counting sort

vector<int> counting_sort(vector<int>& lista) {
    int max_valor= *max_element(lista.begin(), lista.end()) + 1;
    vector<int> count(max_valor, 0);

    for(int num : lista){
        count[num]++;
    }

    vector<int> ordenada;
    for (int i= 0; i<max_valor; i++){
        while (count[i]>0){
            ordenada.push_back(i);
            count[i]--;
        }
    }

    return ordenada;
}

int main() {
    // Defino una lista de tamaños de datos para generar
    vector<int>tamanos= {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

    // Generar archivos para cada tamaño de datos
    
	ofstream archivo_tiempo("tiempos_countingsort_c++.txt"); // Archivo para guardar los tiempos de ejecucion
    
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
        vector<int> numeros_ordenados = counting_sort(numeros_aleatorios);
        clock_t tiempo_fin = clock();
        double tiempo_ejecucion = double(tiempo_fin - tiempo_inicio) / CLOCKS_PER_SEC;

        // Guardar los numeros ordenados en un nuevo archivo
        
		ofstream archivo_ordenado("datos_" + to_string(tamano) + "_ordenados COUNTING SORT C++.txt");
        for (int numero : numeros_ordenados) {
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
