import datetime

date_of_birth = int(input("The date of your birth: "))
current_year = datetime.date.today().year

print("You were born in", date_of_birth)
print("You are", current_year - date_of_birth, "years old!")