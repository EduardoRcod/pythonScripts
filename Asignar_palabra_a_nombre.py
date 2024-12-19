def asignar_palabras_a_nombres(palabras, nombres):
    asignaciones = {}

    for i, nombre in enumerate(nombres):
        indice_palabra = i % len(palabras)  # Ciclo circular de palabras
        palabra_asignada = palabras[indice_palabra]
        asignaciones[nombre] = palabra_asignada

    return asignaciones

# Listas de palabras y nombres
lista_palabras = ["rojo", "verde", "azul", "amarillo"]
lista_nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]

# Llamada a la función y obtener las asignaciones
asignaciones = asignar_palabras_a_nombres(lista_palabras, lista_nombres)

# Imprimir las asignaciones
for nombre, palabra in asignaciones.items():
    print(f"{nombre} -> {palabra}")
