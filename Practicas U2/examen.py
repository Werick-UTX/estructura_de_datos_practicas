matriz = [ [1,2,3],
          [4,5,6],
          [7,8,9] ]

def suma_diagonal_principal(matriz, indice=0):
    if indice >= len(matriz): #B
        return 0
    else:
                    #R
        sumaDiagonal = matriz[indice][indice] + suma_diagonal_principal(matriz,indice+1)
    return sumaDiagonal

print(suma_diagonal_principal(matriz))