#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  valor=f"{num%10}{num//10}"
  return int(valor)
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
