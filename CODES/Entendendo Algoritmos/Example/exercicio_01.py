# Suponha que você tenha uma lista com 128 nomes e esteja fazendo 
# uma pesquisa binária. Qual seria o número máximo de etapas que 
# você levaria para encontrar o nome desejado?

def numero_de_etapas(numero_item_lista):
    cont = 0

    while numero_item_lista > 0:
        print(numero_item_lista)
        numero_item_lista //= 2
        cont += 1

    print(f'{cont - 1} etapas.')
    print('')

numero_de_etapas(128)

# Suponha que você duplique o tamanho da lista. Qual seria o
# número máximo de etapas agora?

numero_de_etapas(256)
