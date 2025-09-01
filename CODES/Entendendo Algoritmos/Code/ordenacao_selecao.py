def buscarMenor(array):
    menor = array[0]  #1
    menor_indice = 0  #2
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

def ordenacaoPorSelecao(array):  #3
    newArray = []
    for i in range (len(array)):
        menor = buscarMenor(array)  #4
        newArray.append(array.pop(menor))
    return newArray

def printVazio():
    print('')

listaDeNumeros = [3, 7, 4, 11, 45, 32, 29, 2, 23, 37]

printVazio()
print(ordenacaoPorSelecao(listaDeNumeros))
printVazio()

### Código para ordenar um Array do menor para o maior

#1 → Armazena o menor valor
#2 → Armazena o índice do menor valor
#3 → Ordenações em um Array
#4 → Encontra o menor elemento do Array e adiciona ao novo Array
