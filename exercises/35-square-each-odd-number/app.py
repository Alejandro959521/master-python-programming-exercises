def function(frase):
    value=[x.strip() for x in frase.split(",")]
    value2=[]
    print(value)
    for y in value:
        
        if int(y) % 2 != 0 :    
            value2.append(y)
    return ",".join(value2)
    

entrada=input()
print(function(entrada))

# values = raw_input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print ",".join(numbers)