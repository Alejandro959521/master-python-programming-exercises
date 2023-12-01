
def secuence (numbers):
    frase = [word.strip() for word in numbers.split(',')] 
    frase2=[]
    for x in frase:
        if int(x) >=1000 and int(x)<=3000:
            frase2.append(x)
    return ",".join(frase2)

entrada=input()
print(secuence(entrada))