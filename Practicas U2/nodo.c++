#include <iostream>
#include <string>
using namespace std;

class Nodo{
    public:

    std::string dato;
    Nodo* siguiente; //Es el puntero, guarda la dirección de memoria siguiente.
    
    //constructor
    Nodo(std::string val){
        dato = val;
        siguiente = nullptr;
    }
};

int main(){

    Nodo* nodo_singular = new Nodo("Primer dato"); //Creacion dle nodo con memoria dinamica


    //acceso a los atributos
    std::cout <<nodo_singular -> dato << std::endl;
    std::cout <<nodo_singular -> siguiente << std::endl;

    delete nodo_singular; //Liberar memoria asignada

    return 0;
}