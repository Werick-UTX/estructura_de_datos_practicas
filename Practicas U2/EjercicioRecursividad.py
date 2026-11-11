def limpiar_feed(publicaciones: list) -> list:
    if len(publicaciones) <= 1:
        return publicaciones
    
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

print(limpiar_feed(["Post A", "Post B", "Post B", "Post C", "Post B"]))