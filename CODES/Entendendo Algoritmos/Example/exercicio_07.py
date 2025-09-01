# Escreva uma função recursiva que conte o número de itens em uma lista

print('\nRESPOSTA 01:')

def contarItens(lista):
    if lista == []:
        return 0
    return 1 + contarItens(lista[1:])

print('')
print(contarItens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Encontre o valor mais alto em uma lista

print('\nRESPOSTA 02:')

def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print('')
print(maximo([23, 87, 46, 91, 35, 12]))

# Você se lembra da pesquisa binária? Ela também é um algoritmo do tipo dividir para conquistar.
# Voc~e consegue determinar o caso-base e o caso-recursivo para a pesquisa binéria?

print('\nRESPOSTA 03:')

print('\nO caso base é se o array possuir apenas um item. Se o item que você está procurando combina')
print('com o item presente no array, você encontrou. Caso contrário, não está no array.')
print('')
