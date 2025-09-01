# ARRAYS E LISTAS ENCADEADAS

respostas = ['Array', 'Lista Encadeada']

print(f'\nResposta 01: {respostas[1]}')

print(f'\nResposta 02: {respostas[0]}')

print('\nResposta 03: Quando se insere um novo item em um array, todos os outros itens também mudam de posição.')
print('Sendo assim, se for necessário adicionar um novo item, e não possuir espaço para mais um item naquela \nparte da memória, todos os item vão se mover para uma parte da memória que suporte todos eles guardados \num ao lado do outro.')
print('Então, quando se adiciona um novo item, todos os outros depois dele, se deslocam para o proximo espaço \nna memória, e caso não haja memória o suficiente, todos se deslocam para uma parte onde todos caibam.')


print(f'\nResposta 04: Eu diria que não é tão rápido como uma {respostas[1]}, mas não é tão lento como um {respostas[0]}.')
print(f'É, na verdade, um sistema bem eficiente, pois não existem mais do que 26 itens em um alfabeto, portanto \nnão é necessário realocar todos os itens já que todos vão começar com alguma letra do alfabeto. E como \nhá {respostas[1]} dentro de um {respostas[0]}, a inserção de novos itens não é mais um problema.')
print(f'Porém para a consulta dos itens na {respostas[1]}, se torna mais lenta do que se fosse um {respostas[0]}')
print('')
