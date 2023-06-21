def playing():
    print('*' * 20)
    print(' Hangman Game')
    print('*' * 20)

    secret_word = "banana"
    correct_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    correct = False    

    while (not correct and not hanged):

        guessing_letters = input("Qual letra? ")
        guessing_letters = guessing_letters.strip()

        index = 0
        for letra in secret_word:
            if (guessing_letters.upper() == letra.upper()):
                correct_letters[index] = letra
            index = index + 1

        print(correct_letters)
    print('Game over')

if(__name__ == "__main__"):
    playing()
