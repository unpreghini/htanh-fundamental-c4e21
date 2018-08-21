my_hobbies = ['Python', 'Movies']

print(my_hobbies)

your_hobby = input("What is your hobby? ")

my_hobbies.append(your_hobby)

print(*my_hobbies, sep=", ")
