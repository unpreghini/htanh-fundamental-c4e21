sizes = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Anh and these are my sheeps size:")
print(sizes)

months = 5

for i in range(months):
    print("MONTH", i + 1, ":")
    sizes = [size + 50 for size in sizes]
    print("One month has passed, here is my flock:")
    print(sizes)

    biggest = max(sizes)

    print("Now my biggest sheep has size", biggest, "let's shear it!")

    default_size = sizes.index(biggest)

    sizes[default_size] = 8

    print("After shearing, this is my flock:")
    print(sizes)
    print()

total = sum(sizes)
price = 3
profit = total * price

print("My flock has size in total:", total)
print("I would get ", total, " * ", price, "$ = ", profit, "$", sep="")
