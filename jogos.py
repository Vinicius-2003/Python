import Guess
import Hangman

print('*' * 20)
print(' Choose your game')
print('*' * 20)

print('(1) Hangman Game (2) Guessing Game ')

game = int(input("Which game will you play ? "))

if game == 1:
    print("Playing Hangman Game...\n")
    Hangman.playing()
elif game == 2:
    print("Playing Guessing Game...\n")
    Guess.playing()