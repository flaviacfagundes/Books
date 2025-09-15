print("\nPergunta: Quais destas funções hash são consistentes? ")
print("\n 1 | f(x) = 1  →  Retorna '1' para qualquer entrada")
print(" 2 | f(x) = rand()  →  Retorna um núemro aleatório a cada execução")
print(" 3 | f(x) = proximo_espaco_vazio()  →  Retorna o índice do próximo espaço livre da tabela hash")
print(" 4 | f(x) = len(x)  →  Usa o comprimento da string como índice")

reposta = ["Consistente", "Inconsistente"]

print(f"\nRespostas: \n\n1 | {reposta[0]}\n2 | {reposta[1]}\n3 | {reposta[1]}\n4 | {reposta[0]}")
print("")
