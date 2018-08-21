items = ['Soccer', 'Python', 'Web']
item_size = len(items)
print("Hi there, here is your favorite items:")
for index, item in enumerate(items, start=1):
    print(index, ". ", item, sep="")

print('*' * 30)

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
