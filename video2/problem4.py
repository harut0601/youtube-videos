import math

value = float(input("The value of sin/cos here: "))
unit = input("sin/cos")

if unit.upper() == "SIN":
    sin = value
    cos = math.sqrt(1 - float(sin)**2)
    tg = sin/cos
    ctg = 1/tg
elif unit.upper() == "COS":
    cos = value
    sin = math.sqrt(1 - float(cos)**2)
    tg = sin/cos
    ctg = cos/sin #or 1/tg
else:
    print("Error...")
    
print("sin =", sin)
print("cos =", cos)
print("tg =", tg)
print("ctg =", ctg)