class generator:
    def __init__(self,n):
        self.n=n
    def ciclo(self):
        for x in range(self.n + 1):
            if x % 7 == 0:
                yield x



valor=40
numeros=generator(valor)

for x in numeros.ciclo():
    print(x)       
 