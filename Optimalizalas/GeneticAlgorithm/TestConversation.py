#Intervalum transformed into [0,255]

interval=[1.0,10.0]
number=10.12

transNumber=int((number-interval[0])/(interval[1]-interval[0])*1023)

strNumber='{0:010b}'.format(transNumber)
print transNumber

nm=transNumber/1023.0*(interval[1]-interval[0])+interval[0]
print number,nm
