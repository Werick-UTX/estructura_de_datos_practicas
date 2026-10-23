historial_navegacion = []

# OPERACION PARA APILAR (PUSH)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("historial cargado", historial_navegacion)

# OPERACION CIMA (TOP-PEEK)
pagina_actual = historial_navegacion[-1]
print("pagina actual en pantalla:", pagina_actual)

# OPERACION PARA DESAPILAR (POP)
pagina_cerrada = historial_navegacion.pop()
print("saliendo de:", pagina_cerrada)
print("historial despues de presionar 'Atras'", historial_navegacion)

# OPERACION TAMAÑO (SIZE)
total_paginas = len(historial_navegacion)
print("paginas guardadas", total_paginas)

# OPERACION VACIA (EMPTY)
sin_paginas = len(historial_navegacion) == 0
print("¿El historial esta vacio", sin_paginas)