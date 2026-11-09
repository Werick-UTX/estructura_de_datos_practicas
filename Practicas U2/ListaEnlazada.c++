#include <iostream>
#include <string>

using namespace std;

class Nodo{
    public:
    std::string dato;
    Nodo* siguiente;

    //Constructor
    Nodo(std::string val){
        dato = val;
        siguiente = nullptr;
    }
};