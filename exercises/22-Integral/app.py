def generate_dict(n):
    dict={}
    for x in range(1,n+1):
        dict[x]=x*x
    return dict    
             
print( generate_dict(8))