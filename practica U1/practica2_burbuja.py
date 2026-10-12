calificaciones = [85, 92, 78, 100, 60, 74, 88, 95, 81, 67, 90, 83, 70, 99, 76]

lista_asc = calificaciones.copy()
n = len(lista_asc)

swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if lista_asc[i] > lista_asc[i + 1]:
            lista_asc[i], lista_asc[i + 1] = lista_asc[i + 1], lista_asc[i]
            swapped = True

print("Orden Ascendente:", lista_asc)

lista_desc = calificaciones.copy()
n = len(lista_desc)

swapped = True
while swapped:
    swapped = False
    for i in range(n - 1):
        if lista_desc[i] < lista_desc[i + 1]:
            lista_desc[i], lista_desc[i + 1] = lista_desc[i + 1], lista_desc[i]
            swapped = True

print("Orden descendente:", lista_desc)