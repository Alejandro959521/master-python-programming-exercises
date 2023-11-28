import math
def print_formula(n1,n2,n3):
    n1=round(math.sqrt((2*50*n1)/30))
    n2=round(math.sqrt((2*50*n2)/30))
    n3=round(math.sqrt((2*50*n3)/30))
    
    return f"{n1},{n2},{n3}"

print(print_formula(100,150,180))
