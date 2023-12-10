# Inicializar las coordenadas en (0, 0)
x, y = 0, 0

# Definir la secuencia de movimientos

movements = [("ARRIBA", 5), ("ABAJO", 3), ("IZQUIERDA", 3), ("DERECHA", 2)]

# Iterar sobre cada movimiento en la secuencia
for move in movements:
    # Obtener la dirección y la cantidad de pasos del movimiento actual
    direction, steps = move
    
    # Actualizar las coordenadas según la dirección y la cantidad de pasos
    if direction == "ARRIBA":
        y += steps
    elif direction == "ABAJO":
        y -= steps
    elif direction == "IZQUIERDA":
        x -= steps
    elif direction == "DERECHA":
        x += steps

# Calcular la distancia desde el punto original usando el teorema de Pitágoras
distance = round((x**2 + y**2)**0.5)

# Imprimir la distancia
print(distance)