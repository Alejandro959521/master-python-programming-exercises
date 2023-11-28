# def matriz(n,m):

    
#     colum=[]
#     for y in range(n):
#         fila=[]
        
#         for x in range(m):
#             fila.append(x*y)
#             colum.append(fila)
           
#     return colum

# print(matriz(3,5))



def two_dimensional_array(nList, nElements):
    dimensions=[int(x) for x in "{},{}".format(nList,nElements).split(',')]
    print("esto es dimencions",dimensions)
    rowNum=dimensions[0]    
    colNum=dimensions[1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    print("multilist",multilist)
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col

    return (multilist)

print(two_dimensional_array(3,5))

#  esta verga no la entendi !!!
