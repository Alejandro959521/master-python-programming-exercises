def function(frase):
    # value=[x.strip() for x in frase.split(" ")]

    mayus=0
    minus=0
    for x in frase.strip():

        if x.isupper():
            mayus+=1
        elif x.islower(): 
            minus+=1    
    
    return f"UPPER CASE {mayus} LOWER CASE {minus} "



entrada=input()
print(function(entrada))