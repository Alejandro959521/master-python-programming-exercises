
# def separation():
#     l=input("ingrese una seria de palabras separadas en comas:")
#     frase=[x for x in "{}".format(l).split(",")]
#     frase.sort()
#     return (','.join(frase))

# print(separation())    

# Lee la secuencia de palabras desde la consola
input_sequence = input("Ingrese una secuencia de palabras separadas por comas: ")

# Divide la entrada en una lista de palabras
words = [word.strip() for word in input_sequence.split(',')]

# Ordena las palabras alfabéticamente
sorted_words = sorted(words)

# Imprime las palabras ordenadas, separadas por comas
result = ",".join(sorted_words)
print(result)
