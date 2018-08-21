rows = int(input("Enter rows: "))
column = int(input("Enter columns: "))

for i in range(rows):
    for _ in range(column):
        print("x", end=" ")
    print()
