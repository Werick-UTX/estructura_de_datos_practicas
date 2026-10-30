import numpy as np
#Con numpy

A_np = np.array([[10,15],
                 [20,5]])

B_np = np.array([[5,12],
                 [15,8]])

#Nativo
A = [[10,15],
    [20,5]]

B = [[5,12],
    [15,8]]


#Nativo
totalVentasNa = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]


precio = 50
ingresosNa = [
    [totalVentasNa[i][j] * precio for j in range(len(totalVentasNa[0]))]
    for i in range(len(totalVentasNa))
]

    
    
#Productos vendidos
print("Total de productos vendidos (Sábado + Domingo):")
for fila in totalVentasNa:
    print(fila)

totalVenta = A_np+ B_np
print(f"\nTOTAL DE PRODUCTOS VENDIDOS (Sabado + Domingo):  \n {totalVenta}")

#Productos a 50

ingresos = totalVenta * 50
print(f"\n INGRESOS TOTAL EN PESOS (a 50 pesos cada producto):  \n {ingresos}")

print("\nIngreso total en pesos (a 50 pesos por producto):")
for fila in ingresosNa:
    print(fila)