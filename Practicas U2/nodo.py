class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    #Creacion de un Nodo Individual

nodo_singular = Nodo("Primer Dato")

print(nodo_singular.dato)
print(nodo_singular.siguiente)