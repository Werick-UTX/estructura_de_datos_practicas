import array

# Crear un array de enteros ('i') con restricciones de tipo
# Todos los elementos deben ser del mismo tipo
numeros = array.array('i', [5, 12, 18, 7, 24, 3, 30])

# 1. Filtrar solo los números pares mayores a 10 usando una lista por comprensión
pares_mayores_10 = array.array('i', [x for x in numeros if x % 2 == 0 and x > 10])

# 2. Modificar elementos in-place (multiplicar por 10)
for i in range(len(pares_mayores_10)):
    pares_mayores_10[i] *= 10

# Convertir a lista si necesitas imprimirlo con formato legibles
print("Array original:", numeros.tolist())
print("Array procesado:", pares_mayores_10.tolist())
# Salida: Array procesado: [120, 180, 240, 300]

