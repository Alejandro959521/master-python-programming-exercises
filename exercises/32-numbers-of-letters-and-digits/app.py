def function(frase):
    # value=[x.strip() for x in frase.split(" ")]

    letters=0
    digits=0
    for x in frase.strip():

        if x.isalpha():
            letters+=1
        elif x.isdigit(): 
            digits+=1    
    
    return f"LETTERS {letters} DIGITS {digits} "



entrada=input()
print(function(entrada))