# Assignment 1
# ICS3U
# <karim gahelrasoul>
# March 29, 2018

###### uncomment this when you are ready to work on it
def CtoF (C):
    F = 1.8* C+32
    return F

def FtoC (F):
 C = (0.55556) * (F-32)
 return C

print('print 1 for celcius, 2 for farenheight')
x = int(input())

if x == 1:
    temperature1 = int(input('enter your number in farenheight'))
    print(int(round(FtoC(temperature1))))
elif x == 2:
    temperature2 = int(input('enter your number in celcius'))
    print(int(round(CtoF(temperature2))))
else:
    print('neither')
    
    


