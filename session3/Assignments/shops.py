items = ["T-shirts", "Jeans", "Hoodie", "Shorts", "Hat", "Shoes"]
item_size = len(items)
print("Hello, Welcome to C4E Shop")
print("Our items on sale for today:")
for index, item in enumerate(items, start=1):
    print(index, ". ", item, sep="")

print('*' * 30)

while True:
    command = input("Select action: C, R, U, D: ").upper()

    if command == "C":
        add = input("Type your additional item: ")
        items.append(add)
        print('*' * 30)

        print("Our items on sale for today:")

        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")

        print('*' * 30)

    elif command == "R":
        print("Our items on sale for today:")
        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")
        print('*' * 30)

    elif command == "U":
        print("Our items on sale for today:")
        position = int(input("Position to update? "))

        if (position - 1) in range(item_size):
            replace_item = input("Your replacing item? ")
            items[position - 1] = replace_item
        else:
            raise Exception("Invalid input")

        print('*' * 30)

        print("Our items on sale for today:")

        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")

        print('*' * 30)

    elif command == "D":

        removal = input("Item to remove? ")

        if removal in items:
            items.remove(removal)
        else:
            raise ValueError("Invalid input: Item not found")

        print('*' * 30)

        print("Our items on sale for today:")

        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")

        print('*' * 30)

    else:
        raise ValueError("Command not found, please try again")
