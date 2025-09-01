
A janela Python Shell é um ambiente REPL, usado para executar os fragmentos de código do Python, normalmente uma instrução de cada vez.

> **O que significa REPL?**
> É uma abreviação de "read-eval-print-loop" (ler-interpretar-imprimir-repetir) e descreve uma ferramenta de programação interativa que permite experimentar os fragmentos de um código como quiser.


# Vamos Entender O Primeiro Código


![[Pasted image 20250810185946.png]]

**Python** é o nome dado à linguagem de programação, e **IDLE** é o nome dado ao IDE predefinido do Python. Quando você instala o Python 3 no computador, um **interpretador** é instalado também. Essa é a tecnologia que executa o código Python.

A primeira linha de código **importa** uma funcionalidade preexistente da ==biblioteca padrão== do Python, que é um grande estoque de módulos de software fornecendo muito código predefinido (de alta qualidade) e reutilizável.

- O submódulo `datetime` fornece um mecanismo para calcular o tempo.
- Outro módulo, chamado `os` fornece um modo independente da plataforma para interagir com seu sistema operacional.


# Biblioteca Padrão

A biblioteca padrão do Python é muito rica e fornece muito código reutilizável.
Uma coleção de funções afins compõe um módulo, e há muitos módulos na biblioteca padrão.

>**Funções + Módulos = Biblioteca Padrão**

 A função faz parte do módulo que vem como parte da biblioteca padrão.

- O módulo `sys` existe para ajuda-lo a aprender mais sobre o sistema do seu interpretador. Eis como determinar a identidade do sistema operacional subjacente, primeiro importando o módulo `sys`, e então acessando o atributo `platform`

![[Pasted image 20250810205041.png]]

- Veja como determinar qual versão do Python está em execução:

![[Pasted image 20250810205322.png]]

- Veja como descobrir o nome da pasta na qual seu código está operando usando a função `getcwd`. Como qualquer módulo, você começa importando o módulo antes de chamar a função:

![[Pasted image 20250810205606.png]]

- Você pode acessar variáveis de ambiente do sistema, em conjunto (usando o atributo `environ`), ou individualmente (com a função `getenv`):

![[Pasted image 20250810205902.png]]

- É comum ter que trabalhar com datas (horas), e a biblioteca padrão fornece o módulo `datetime`. A função `date.today` fornece a data de hoje:

![[Pasted image 20250810210139.png]]

- Você pode acessar os valores do dia, mês e ano separadamente anexando um acesso do atributo à chamada para d`date.today

![[Pasted image 20250810210430.png]]

- Também é possível chamar a função `date.isoformat` que converte a data atual em uma string:

![[Pasted image 20250810210627.png]]

- O módulo `time` é capaz de informar que horas são. Basta importar o módulo e chamar a função `strftime` e especifique como você deseja que a hora seja exibida. Nesse caso, estamos interessados nos valores das horas (%H) e minutos (%M) do momento atual no formato 24 horas:

![[Pasted image 20250810211022.png]]

- Para descobrir o dia da semana e se é antes ou depois do meio-dia, usar a especificação %A e %p com `strftime`

![[Pasted image 20250810211309.png]]

- Exemplos com a biblioteca HTML:

![[Pasted image 20250810211919.png]]
![[Pasted image 20250810211937.png]]


# As Estruturas de Dados Vem Predefinidas


O Python tem algumas **estruturas de dados** predefinidas poderosas. Uma delas é a ==lista==, que pode ser considerada um array poderoso. Como os ==arrays== em muitas linguagens, as listas no Python ficam entre colchetes [].

As **listas** no Python podem conter qualquer dado de qualquer tipo, e você pode até misturar os tipos de dados em uma lista.

Em geral, o **final da linha marca o final de uma instrução** no Python, mas pode haver exceções a essa regra geral, e listas com várias linhas são apenas uma delas.

![[Pasted image 20250810213313.png]]

Essa lista existe, foi atribuída à variável `odds` (graças ao uso do **operador de atribuição, =**) e contém os números mostrados.


# As Variáveis São Atribuídas Dinamicamente


No Python, as variáveis ganham vida na primeira vez em que você as usa, e **seu tipo não precisa ser declarado previamente**. As variáveis obtêm as informações do tipo a partir do tipo de objeto ao qual são atribuídas.

A terceira linha de código chama um método denominado `today` que vem com o submódulo `datetime`, que faz parte do módulo `datetime`. Você pode dizer que `today` está sendo chamado devido aos parênteses adicionados padrão ().

Quando `today` é chamado, retorna um "objeto-hora", que contém partes da informação sobre a hora atual. Estes são os **atributos** da hora atual, que você pode acessar via sintaxe de **notação de ponto** habitual. Neste programa estamos interessados no atributo minuto, que podemos acessar anexando `.minute`. E o valor resultante é atribuído à variável `right_this_minute`.



# Operador in


O operador `in` verifica se uma coisa está *dentro* de outra. O operador `in` retorna `True` ou `False`. Se o calor de `right_this_minute` estiver em `odds`, a instrução `if` será avaliada como `True`, e o bloco de código associado a instrução `if` será executado.

**É fácil identificar os blocos no Python, pois estão sempre recuados.**

- A função `print()` exibe uma mensagem na tela.

O Python usa o **recuo** para demarcar um bloco de código, que os programadores Python preferem chamar de **suíte**, em vez de bloco.