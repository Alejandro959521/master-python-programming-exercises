def function(frase):
   oracion = frase.split(" ")
   fraseOrdenada=sorted(oracion) 
   dic={}
   for x in fraseOrdenada:
      if x in dic:
         dic[x]+=1
      elif x is not None: dic[x]=1
   salida=sorted(dic.items())
   return salida      
salida=function("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3")   

print(salida)
for word,freq in salida:
    print(f"{word}:{freq}", end=" ")

# la vaina da !

#print(function("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"))    