from collections import deque
import time


cola_turnos = deque()


cola_turnos.append("Turno A01 - Erick Cruz Gonzalez")
cola_turnos.append("Turno A02 - Leonardo Naranjado de la Rosa")
cola_turnos.append("Turno A03 - Flor Cortez Valderrabano")


print("Turnos emitidos en la fila del banco:")
for cliente in cola_turnos:
    print(f"- {cliente}")


print("\nIniciando atención en ventanilla\n")

while cola_turnos:
    cliente = cola_turnos.popleft()

    print(f"Llamando a ventanilla: {cliente}")
    time.sleep(1)

    print(f"Atención finalizada: {cliente}")
    print(f"(Clientes restantes en la fila: {len(cola_turnos)})\n")

print("Se han atendido todos los turnos. Fila vacía.")