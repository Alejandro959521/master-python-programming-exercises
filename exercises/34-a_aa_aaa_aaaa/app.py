def function(value):
    digito=value.strip()
    
    a=digito
    aa=digito+digito
    aaa=digito+digito+digito
    aaaa=digito+digito+digito+digito
   

    return int(a)+int(aa)+int(aaa)+int(aaaa)

entrada=input()
print(function(entrada))    