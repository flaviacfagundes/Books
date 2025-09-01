def quicksort(array):
    if len(array) < 2:
        return array  #1
    else:
        pivo = array[0]  #2
        menores = [i for i in array[1:] if i <= pivo]  #3
        maiores = [i for i in array[1:] if i > pivo]  #4
        return quicksort(menores) + [pivo] + quicksort(maiores)

numeros = [98, 65, 21, 44, 37, 63, 19]

print('')
print(quicksort(numeros))
print('')

#1 → Base: arrays com 0 ou 1 elementos já estão ordenados
#2 → Caso recursivo
#3 → Subarray de todos os elementos menores do que o pivô
#4 → Subarray de todos os elementos maiores do que o pivô
