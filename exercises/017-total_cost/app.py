#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    total_centavos = (d * 100 + c) * n
    total_dolares = total_centavos // 100
    total_centavos %= 100
    return (total_dolares, total_centavos)
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(45,33,33))    
