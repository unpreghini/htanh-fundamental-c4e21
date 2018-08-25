terms = {"FTP": "File Transfer Protocol",
         "IDM": "Internet Download Manager",
                "APP": "Application", }

while True:

    term = input("Your term: ").upper()

    if term in terms:
        print(term, "means", terms[term])
    else:
        command = input("Term not yet available, do you want to add? (Y/N): "
                        ).upper()

        if command == "Y":
            word = input("Type your word: ")
            meaning = input("Type your definition: ")
            terms['word'] = meaning
            print(word, "is added")

        elif command == "N":
            break
