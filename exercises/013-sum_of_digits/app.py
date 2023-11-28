#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  numero=str(num)
  return int(numero[0])+int(numero[1])+int(numero[2])


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))