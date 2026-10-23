from collections import deque
cola=deque()

#AGREGAR ELEMENTOS A LA COLA (ENCOLAR)
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")

#SACAR EL PRIMER ELEMENTO QUE LLEGO (DESENCOLAR)
atendido=cola.popleft()

#MOSTRAR RESULTADOS
print("Atendido",atendido)
print("cola restante:",cola)