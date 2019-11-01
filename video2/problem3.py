temperature = int(input("The outside temperature: "))
unit = input("(C)elsius or (F)ahrenheit: ")

if unit.upper() == "C":
    final_temperature = (temperature * 1.8 + 32)
elif unit.upper() == "F":
    final_temperature = ((temperature - 32) * 5/9)
else:
    print("Please try again!")
    final_temperature = "Not defined"
    
if unit.upper() == "C":
    unit = "Fahrenheit"
elif unit.upper() == "F":
    unit = "Celsius"
    
print(final_temperature, unit)