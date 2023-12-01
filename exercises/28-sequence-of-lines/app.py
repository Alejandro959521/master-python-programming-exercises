
def lines(frase):

    secu=[x for x in "{}".format(frase).split(" ")]
    secu2= " ".join(secu)
    secu3=secu2.upper()
    
    return secu3

#frase = input(" ")

print(lines("Hello world Practice makes perfect"))