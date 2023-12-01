def password(word):

    array=[x.strip() for x in word.split(",")]
    #print(array)
    salida=[]
    for y in array:
        
        frase=y.replace(" ", "")
        #print(frase)
        mayus=False
        minus=False
        number=False
        simbols=False
        if len(frase) >=6 and len(frase) <= 12:

            for z in frase:
                #print(z)           
                if  z.isupper():
                    mayus = True
                elif z.isdigit():
                    number = True                  
                elif z.islower(): 
                    minus = True
                elif z == "@" or z == "#" or z == "@": 
                    simbols = True 
                
            if mayus and minus and number and simbols:
                mayus=False  
                minus=False 
                number=False
                simbols=False  
                salida.append(frase)              
                
            else :
                print("debe contener al menos una letra y un numero una mayuscula y una minuscula y un caracter especial") 
                mayus=False  
                minus=False 
                number=False
                simbols=False   

        else: print("contraseña debe de tener el numero de caracteres especificado")    
    return ",".join(salida)  

entrada=input()
print(password(entrada))    

# todo una locura pero da !!!