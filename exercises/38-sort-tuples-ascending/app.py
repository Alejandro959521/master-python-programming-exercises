
def order(frase):
    palabras = [palabra.split(",") for palabra in frase.replace("\n", "").split(",")]
    
    tuplas = [(palabras[i][0], palabras[i][1], palabras[i][2]) for i in  range(0, len(palabras)) if i % 3 == 0]

    #array2=[]
    #print(array)
    #print(frases)
    #tuplas=[i for i in array]
    # for y in array:
        
    #     tupla=tuple(y,)
    #     array2.append(tupla)
    # return array2   
    return tuplas
frase=input() 
print(order(frase))    

#  from operator import itemgetter, attrgetter
# def sort_tuples_ascending(tuples):
#     l = []
#     l.append(tuple(tuples.split(",")))
#     return (sorted(l, key=itemgetter(0,1,2)))









