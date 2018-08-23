sizes = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Anh and these are my sheeps size:")
print(sizes)

biggest = max(sizes)

print("Now my biggest sheep has size", biggest, "let's shear it!")

default_size = sizes.index(biggest)

sizes[default_size] = 8

print("After shearing, this is my flock:")
print(sizes)

sizes = [size + 50 for size in sizes]

print("One month has passed, here is my flock:")
print(sizes)
