# SOMA DE ARRAYS DE NÚMEROS - COM LOOP

def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print('')
print(soma([1, 2, 3, 4]))
print('')

# SOMA DE ARRAYS DE NÚMEROS - COM RECURSÃO

def somarArray(array):
    if array == []:
        return 0
    return array[0] + somarArray(array[1:])

print(somarArray([1, 2, 3, 4]))
print('')
