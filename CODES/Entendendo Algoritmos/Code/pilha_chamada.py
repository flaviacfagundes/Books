def sauda(nome):
    print(f'\nOlá, {nome}!')  #1
    sauda2(nome)   #2
    print('Preparando para dizer tchau...')  #3
    tchau()  #4

def sauda2(nome):
    print('Como você está?')

def tchau():
    print('Ok, tchau!')
    print('')

sauda('Flávia')

#1 → Primeiro vai chamar a o print da função sauda
#       Na pinha, só possui essa função

#2 → Depois chama a função sauda2()
#       A função sauda2() é inserida (push) no topo da pilha, e é retirada (pop) quando executada

#3 → Senso assim, a função sauda volta ao topo da lista e executa o outro print

#4 → Então a função tchau() é chamada e executada
#       A funcção tchau() vai então para o topo da lista, e só é retirada quando executada
