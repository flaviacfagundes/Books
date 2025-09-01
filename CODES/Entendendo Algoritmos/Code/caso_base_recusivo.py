# # LOOP INFINITO
# def regressiva(i):
#     print(i)
#     regressiva(i- 1)

# regressiva(10)

# LOOP COM CASO-BASE E CASO-RECURSIVO
def printVazio():
    print('')

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

printVazio()
regressiva(10)
printVazio()
