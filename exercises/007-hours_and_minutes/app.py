#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  
  return ((secs//60)//60,secs//60)

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(7320))