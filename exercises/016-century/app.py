#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
def century(year):
  año=year-1
  return int((año//100)+1)



#Invoke the function with any given year. 
print(century(2001))