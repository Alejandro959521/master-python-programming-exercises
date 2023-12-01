def function(secuence):
    frase = [word.strip() for word in secuence.split(',')] 
    frase2=[]
    for x in frase:
        intp = int(x, 2)
        if (intp % 5 != 0):
            continue
        else: frase2.append(x)

    return ",".join(frase2)

entrada=input()
print(function(entrada))

# no se porque no me pasan los test si la vaina da !!!