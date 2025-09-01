def fat(num):
    if num == 1:
        return 1
    else:
        print(num-1)
        return num * fat(num-1)
    
numero = 10
print('')
print(numero)
print(fat(numero))
print('')

# A cada chamada a pilha foi armazanado o resultado de num!
# Sempre que ele foi diferete de 1, o valor foi armazenado, e a função foi chamada novamente
# Sempre armazenando o valor de num, para que no final o resultado possa ser mostrado
