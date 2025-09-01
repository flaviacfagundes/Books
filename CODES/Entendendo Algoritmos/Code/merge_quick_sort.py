# MERGE SORT VERSUS QUICKSORT

# TEMPO DE EXECUÇÃO O(n)
def imprime_itens(lista):
    for item in lista:
        print(item)

lista_referencia = ['Banana', 'Maça', 'Pessêgo', 'Abacaxi', 'Manga', 'Laranja']

print('')
print(imprime_itens(lista_referencia))
print('')

# TEMPO DE EXECUÇÃO O(n), MESMO COM O TIMESLEEP
from time import sleep

def imprime_itens2(lista):
    for item in lista:
        sleep(1)
        print(item)

print(imprime_itens2(lista_referencia))
print('')
