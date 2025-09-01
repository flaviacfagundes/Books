# PILHA DE CHAMADA

# Pergunta
print('\nPergunta: Supunha que eu forneça uma pilha de chamada como está:')
print('\n ----------------- ')
print(' |    SAUDA 2    | ')
print(' | NOME | FLÁVIA | ')
print(' ----------------- ')
print(' |     SAUDA     | ')
print(' | NOME | FLÁVIA | ')
print(' ----------------- ')
print('\nQuais informações você pode retirar baseando-se apenas nesta pilha de chamada?')

# Resposta
print('\nResposta: A função principal é a função SAUDA, que armazena uma variável NOME,') 
print('dentro da função SAUDA ela chama a função SAUDA 2. Quando SAUDA 2 é chamada, SAUDA') 
print('fica parcialmente completa, ela entra em pausa até SAUDA 2 ser executada e, então') 
print('volta a ser executada com o valor da variável nome ainda armazenado nela.') 
print('E a função SAUDA 2 usa a mesma variável NOME para ser executada. Depois de SAUDA 2 ser') 
print('executada ela vai ser removida pilha para que SAUDA termine de ser executada.')
print('')
