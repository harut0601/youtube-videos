weight = int(input("Your weight: "))    #To make an input box for getting weight info
unit = input("Lbs or Kg")    #To get the info about unit(also getting from user thanks to input form)

#Here we need to write a code to make it work!!!

if unit.upper() == "LBS":  #or unit.lower() == "lbs", that is for making the code case sensitive!
    print("Your weight is:", float(weight)*0.45, "Kg!")
elif unit.lower() == "kg":
    print("Your weight is:", float(weight)/0.45, "Lbs!")
else:
    print("You entered an invalid unit, please make sure to use either Lbs or Kg!")
     
