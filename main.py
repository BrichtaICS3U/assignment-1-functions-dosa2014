# Assignment 1
# ICS3U
# <karim gahelrasoul>
# March 28, 2018

###### uncomment this when you are ready to work on it
def CtoF (C):
    F = 1.8* C+32
    return F

def FtoC (F):
 C = (0.55556) * (F-32)
 return C

temperature = int(input('Enter your temperature in Celsius: '))
print(round(CtoF(temperature)))


