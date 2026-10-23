from collections import deque
import time
cola_reproduccion=deque()

#EL USUARIO AGREGA CANCIONES
cola_reproduccion.append("1.Antologia")
cola_reproduccion.append("2.Historia de amor")
cola_reproduccion.append("3.Historia entre tus dedos")

#MOSTRAR LAS CANCIONES EN ESPERA
print("canciones en espera:")
for cancion in cola_reproduccion:
    print(" _",cancion)
    print("iniciando reproduccion")
    
#El reproductor procesa la cola cancion por cancion (desencolar)
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora{cancion_actual}")
    
    time.sleep(1) #simula la duracion del tema
    print(f"finalizó:{cancion_actual}")
    
    #Muestra cuantas canciones quedan en la cola
    print(f"Quedan({len(cola_reproduccion)}) canciones en la cola")
print("la cola de reproducción ha terminado.")