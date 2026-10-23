pila = []

for i in range(1, 11):
    pila.append(f"Plato {i}")

print("Pila inicial:", pila)

print("Plato en la cima:", pila[-1])

for i in range(4):
    plato = pila.pop()
    print("Plato retirado:", plato)

print("Elementos restantes:", len(pila))
print("¿La pila está vacía?", len(pila) == 0)

while len(pila) > 0:
    plato = pila.pop()
    print("Retirando:", plato)

print("Pila final:", pila)
print("¿La pila está vacía?", len(pila) == 0)