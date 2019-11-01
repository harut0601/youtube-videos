#We need to import math library at first!
import math

a = int(input("A side of the right triangle: "))
b = int(input("B side of the right triangle: "))


#after running program user will input values for a and b and as we know the formula c^2=a^2+b^2 in other words c=sqrt(a^2+b^2)

c_side = math.sqrt(a**2 + b**2) #math.sqrt is the sqrt of the value we input, we need to make the input int(), because sqrt will not work with string

print("The side C is:", int(c_side)) #we can make the value to int not to get .0 at the end!