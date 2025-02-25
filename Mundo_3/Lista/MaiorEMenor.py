list_of_numbers = []


for a in range(0,5):
    a = int(input(("Enter a number : ")))
    list_of_numbers.append(a)


print(list_of_numbers)

maior = max(list_of_numbers)

if list_of_numbers.count(maior) > 1:
    print("More than one 8 in the list")
    print(f'O maior valor digitado foi {maior} e se encontra nas posição : ', end=' ')
    for num in list_of_numbers:
        if num == maior:
            print(list_of_numbers.index(num)+1)
else:
    print(f'O maior valor digitado foi {maior} e se encontra nas posição : {list_of_numbers.index(maior)+1}')
