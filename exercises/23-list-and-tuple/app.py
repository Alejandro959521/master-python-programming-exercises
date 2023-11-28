# Lee la secuencia de números desde la consola
entrada_usuario = input("Ingrese una secuencia de números separados por comas: ")

# Divide la entrada en una lista de números
numeros_lista = entrada_usuario.split(',')

# Convierte la lista en una tupla
numeros_tupla = tuple(numeros_lista)

# Imprime los resultados
print("Lista:", numeros_lista)
print("Tupla:", numeros_tupla)