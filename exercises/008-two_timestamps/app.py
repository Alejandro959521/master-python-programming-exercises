#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    segundos1=(hr1*60)*60
    minutos1=min1*60
    segundos2=(hr2*60)*60
    minutos2=min2*60


    return ((segundos2+minutos2+sec2)-(segundos1+minutos1+sec1))


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))