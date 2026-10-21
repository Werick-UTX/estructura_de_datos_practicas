from collectios import deque
import time

def sitema():
    cola_turnos = deque()
    cola_turnos.append("Tio Urix")
    cola_turnos.append("Tio Lemus")
    cola_turnos.append("Tio Señor Tesillos")

    print("Listas de cola_turnos: ")
    for turno in cola_turnos:
        print(turno)
    print("Iniciando atencion en ventanilla")
    while len(cola_turnos) > 0:
        turno_actual = cola_turnos
