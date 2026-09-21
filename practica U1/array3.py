fruit=["Manzana","Platano","Uvas"]
first_element=fruit[0]
#Actualizar
fruit[1]="Pera"
#Agregar Valores
fruit.append("Sandia")
#Dentro de un contenedor en el arreglo
fruit.insert(2,"mango")
#De manera masiva
fruit.extend(["Melon","Kiwi","Fresa"])
print(fruit)
#Eliminar
retirado=fruit.pop(2)
#Elimminar ultimo elemento
ultimo=fruit.pop
#Eiminar elemento en su primera aparicion
fruit.remove("Manzana")
#Borrar casilla directamente 
del fruit[0]


#Busqueda
if "Sandia" in fruit:
    pos=fruit.index("Sandia")
    print(f"La Sandia está en la casilla{pos}")
    print (fruit)

