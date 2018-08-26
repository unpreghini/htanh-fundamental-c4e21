text = input("Enter your text: ").lower()
characters = list(text)
counts = {}

for character in characters:
    if character != " ":
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1

counts = sorted(counts.items())

for count in counts:
    print(count[0], "", count[1])
