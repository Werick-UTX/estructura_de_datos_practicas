def insercion(lista):
    a = lista.copy()
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and a[j] > clave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = clave
    return a


def seleccion(lista):
    a = lista.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubbleSort(lista):
    b = lista.copy()
    n = len(b)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                swapped = True
    return b




def leer_lista():
    entrada = input("Ingrese números separados por comas: ")
    return [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]


def main():
    listaIngresada = leer_lista()

    while True:
        print(
            f"""
            Lista actual: {listaIngresada}

            Selecciona una opción: 
            1. Ordenar con algoritmo de Burbuja
            2. Ordenar con algoritmo de Selección
            3. Ordenar con algoritmo de Inserción
            4. Ordenar con algoritmo de QuickSort
            5. Ingresar nueva lista
            6. Salir
            """
        )

        try:
            op = int(input("Opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if op == 1:
            print(f"\nResultado Burbuja: {bubbleSort(listaIngresada)}")
        elif op == 2:
            print(f"\nResultado Selección: {seleccion(listaIngresada)}")
        elif op == 3:
            print(f"\nResultado Inserción: {insercion(listaIngresada)}")
        elif op == 4:
            print("\nResultado QuickSort: {}")
        elif op == 5:
            listaIngresada = leer_lista()
        elif op == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()