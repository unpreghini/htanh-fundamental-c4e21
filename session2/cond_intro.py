birth_year = int(input("Enter year of birth: "))
age = 2018 - birth_year
print("Your age:", age)

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
