items = ['Soccer', 'Python', 'Web']
item_size = len(items)
print("Hi there, here is your favorite items:")
for index, item in enumerate(items, start=1):
    print(index, ". ", item, sep="")

print('*' * 30)

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
