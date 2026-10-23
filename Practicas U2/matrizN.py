#Creación de Matriz de 3x3 
matriz = [ [10,20,30],
          [50,60,70],
          [70,80,90] ]

#Acceder a elementos matris [Fila][Columna]
print(matriz[1][2])

#Modificar un elemento
matriz[0][0] = 100

#Recorrer la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ") 
    print(" ")
        #el parametro end permite indicar que se agrege algo en la ultima linea                
                