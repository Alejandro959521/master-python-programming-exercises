class String_mayus:
    def _init_(self):
        self.input_string = ""
    def string(self):
        self.input_string = input("ingresa un string:")
    def print(self): 
        print("letra en mayuscula:",self.input_string.upper()) 



def test():
    mayuscula=String_mayus()
    
    mayuscula.string()

    mayuscula.print()
test()    
