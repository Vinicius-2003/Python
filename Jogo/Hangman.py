def playing():
    print('*' * 20)
    print(' Hangman Game')
    print('*' * 20)

    secret_word = "banana".upper()
    correct_letters = ["_" for letter in secret_word]

    errors = 0

    print(correct_letters)

    while (True):

        guessing_letters = input("Qual letra? ")
        guessing_letters = guessing_letters.strip().upper()
        if(guessing_letters in secret_word):
            index = 0
            for letter in secret_word:
                if (guessing_letters == letter):
                    correct_letters[index] = letter
                index += 1
        else:
            errors += 1
            print("Você têm {} de {}".format(6 - errors,len(secret_word)))

        if(errors == 6):
            break
        if("_" not in correct_letters):
            break
        print(correct_letters)

    if("_" not in correct_letters):
        print('Você ganhou o jogo!')
    else:
        print("Você perdeu :/")

    print('Game over')

if(__name__ == "__main__"):
    playing()
