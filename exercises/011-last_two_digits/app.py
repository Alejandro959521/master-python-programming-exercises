#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(numero):
    if numero > 9: return int(str(numero)[-2:])
    else: return numero
    

# Ejemplo de uso
print(last_two_digits(2323))