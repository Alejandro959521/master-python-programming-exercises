#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  
  numero_dia_semana = (k + 3) % 7
    
  return numero_dia_semana
     



#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(100))