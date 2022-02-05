import sys, random

NEWLINE = '\n'

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

class Colour:
    GREEN = '\x1b[5;30;42m'
    AMBER = '\x1b[5;30;43m'
    RED = '\x1b[5;30;41m'
    NONE = '\x1b[0m'

def output(colour, text, newline: bool = False) -> None:
    sys.stdout.write(f"{colour} {text} {Colour.NONE}{NEWLINE if newline else ''} ")

def get_valid_input() -> str:
    while True:
        guess = input("Guess a word >> ").upper()
        if len(guess) == 5 and guess.isalpha() and guess.lower() in words:
            return guess
        else:
            output(Colour.RED, "Invalid input. Please enter a 5 letter word.", newline=True)

def game():
    word = words[int(len(words) * (random.random()))]
    word = word.upper()
    attempt = 1
    share_str = ''
    while attempt <= 6:
        guess = get_valid_input()
        for i in range(len(guess)):
            if word[i] == guess[i]:
                output(Colour.GREEN, f"{guess[i]}")
                share_str += '🟩'
            elif guess[i] in word:
                output(Colour.AMBER, f"{guess[i]}")
                share_str += '🟨'
            else:
                output(Colour.NONE, f"{guess[i]}")
                share_str += '⬛'
        print()
        share_str += '\n'
        if guess == word:
            output(Colour.GREEN, f"You win! The word was {word}. It took you {attempt} attempts.", newline=True)
            break
        else:
            output(Colour.RED, f"Incorrect. You have {6 - attempt} attempts left.", newline=True)
            attempt += 1
    else:
        output(Colour.RED, f"You lose! The word was {word}.", newline=True)

    if input('\nShare results? >> ') in ['y', 'Y']:
        print(f"\n{'I beat CDEs wordle!' if attempt <= 6 else 'I lost CDEs wordle...'} The word was {word}. {f'I took {attempt}/6 tries.' if attempt <= 6 else ''}\n\n{share_str}")

game()
