import random

words = ["champions", "microsoft", "macintosh", "revolution", "manchester"]

word = random.choice(words)

jumble = ' '.join(random.sample(word, k=len(word)))

print('Welcome to Word Jumble!')

while True:
    print('\nThe Jumble is:', jumble)
    guess = input('Your Guess: ')
    if guess == word:
        print("\nHura! You got it!\n")
        print('Thanks for playing')
        break

    print("Sorry, that's not it :(")
