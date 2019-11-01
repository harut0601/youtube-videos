password = input("Please input your password: ")

if len(password) > 50:
    print("The password must contain less than 50 characters.")
elif len(password) < 3:
    print("The password must contain more than 3 characters.")
else:    
    print("The password is accepted!")