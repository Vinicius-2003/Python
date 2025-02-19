import os


def menu():
    print("""
    Menu
    1 - Add 
    2 - Delete
    3 - Show list
    4 - Exit
""")


list = []
while (True):
    menu()

    option = int(input("Option : "))

    if option == 1:
        os.system('cls')
        item_added = input("Add to the list : ").lower()
        list.append(item_added)

        for item in enumerate(list):
            print(item)

    elif option == 2:
        os.system('cls')
        item_index = int(input("Item number to delete : "))

        try:
            del list[item_index]

        except ValueError:  # tratamento de erro!
            print("Item number invalid")

        except IndexError:  # tratamento de erro!
            print("Index number invalid")

    elif option == 3:
        for item in enumerate(list):
            print("{} ".format(item), end="")

    elif option == 4:
        break
