my_hobbies = ['Python', 'Movies']

print(my_hobbies)

your_hobby = input("Anything else? ")

my_hobbies.append(your_hobby)

size = range(len(my_hobbies))

for i in size:
    print(i + 1, my_hobbies[i], end='\n')
