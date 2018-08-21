items = ['Soccer', 'Python', 'Web']
item_size = len(items)
print("Hi there, here is your favorite items:")
for index, item in enumerate(items, start=1):
    print(index, ". ", item, sep="")

print('*' * 30)

while True:
    command = input("Select action: C, R, U, D: ").upper()

    if command == "C":
        add = input("Type your additional item: ")
        items.append(add)
        print('*' * 30)

        print("These are your new favorite items:")

        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")

        print('*' * 30)

    elif command == "R":
        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")
        print('*' * 30)

    elif command == "U":
        position = int(input("Position to update? "))

        if (position - 1) in range(item_size):
            replace_item = input("Your replacing favorite? ")
            items[position - 1] = replace_item
        else:
            raise Exception("Invalid input")

        print('*' * 30)

        print("These are your new favorite items:")

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

        print("These are your new favorite items:")

        for index, item in enumerate(items, start=1):
            print(index, ". ", item, sep="")

        print('*' * 30)

    else:
        raise ValueError("Command not found, please try again")
