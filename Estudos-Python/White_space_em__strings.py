# ==========================================================
# WHITE SPACE E CARACTERES DE ESCAPE
# ==========================================================

# Em programação, o termo "White Space" (espaço em branco)
# refere-se a caracteres que organizam o texto, mas normalmente
# não representam letras ou números.
#
# Alguns exemplos são:
#
# • Espaço
# • Tabulação (Tab)
# • Quebra de linha
#
# Em Python utilizamos alguns caracteres especiais
# para representar esses espaços dentro das strings.
#
# Esses caracteres são chamados de
# "Caracteres de Escape" (Escape Sequences).


# ----------------------------------------------------------
# \n -> QUEBRA DE LINHA
# ----------------------------------------------------------

# O caractere \n faz com que o texto continue
# na próxima linha.

print("Nome:\nFelipe")

# Resultado:
#
# Nome:
# Felipe


print("Python\nJava\nC++")

# Resultado:
#
# Python
# Java
# C++


# Outro exemplo

print("Primeira linha.\nSegunda linha.\nTerceira linha.")

# Resultado:
#
# Primeira linha.
# Segunda linha.
# Terceira linha.


# ----------------------------------------------------------
# \t -> TABULAÇÃO
# ----------------------------------------------------------

# O caractere \t adiciona uma tabulação.
#
# É semelhante à tecla TAB do teclado.

print("Nome:\tFelipe")

# Resultado:
#
# Nome:    Felipe


print("Python\tJava\tC++")

# Resultado:
#
# Python      Java      C++


# Também podemos utilizar vários \t.

print("A\t\tB\t\tC")

# Resultado:
#
# A        B        C


# ----------------------------------------------------------
# COMBINANDO \n E \t
# ----------------------------------------------------------

# Podemos utilizar os dois caracteres juntos.

print("Linguagens de programação:\n\tPython\n\tJava\n\tC++")

# Resultado:
#
# Linguagens de programação:
#     Python
#     Java
#     C++


# Outro exemplo

print("Cadastro:\n\tNome: Felipe\n\tIdade: 23\n\tCidade: São Paulo")

# Resultado:
#
# Cadastro:
#     Nome: Felipe
#     Idade: 23
#     Cidade: São Paulo


# ----------------------------------------------------------
# OUTROS CARACTERES DE ESCAPE
# ----------------------------------------------------------

# Existem vários caracteres especiais em Python.

# \\  -> Exibe uma barra invertida (\)

print("C:\\Users\\Felipe")

# Resultado:
#
# C:\Users\Felipe


# \" -> Exibe aspas duplas

print("Ele disse: \"Olá!\"")

# Resultado:
#
# Ele disse: "Olá!"


# \' -> Exibe aspas simples

print('Ela respondeu: \'Tudo bem!\'')

# Resultado:
#
# Ela respondeu: 'Tudo bem!'


# ----------------------------------------------------------
# ONDE ISSO É UTILIZADO?
# ----------------------------------------------------------

# Os caracteres de escape aparecem em diversas situações:
#
# • Mensagens no terminal
# • Relatórios
# • Arquivos de texto
# • Logs de sistemas
# • Menus de programas
# • Chatbots
# • Jogos
# • APIs


# ----------------------------------------------------------
# EXEMPLO PRÁTICO
# ----------------------------------------------------------

print("===== MENU =====")
print("1 - Cadastrar")
print("2 - Alterar")
print("3 - Excluir")
print("4 - Sair")

# Também poderíamos escrever assim:

print("===== MENU =====\n1 - Cadastrar\n2 - Alterar\n3 - Excluir\n4 - Sair")


# ----------------------------------------------------------
# CURIOSIDADE
# ----------------------------------------------------------

# Apesar de aparecerem como apenas dois caracteres
# (barra invertida + letra),
# o Python interpreta cada sequência como um único
# caractere especial.
#
# Exemplos:
#
# \n -> Nova linha
# \t -> Tabulação
#
# O usuário vê apenas o resultado final na tela,
# e não os caracteres de escape.


# ==========================================================
# RESUMO
# ==========================================================

# \n
# Quebra uma linha.

# \t
# Adiciona uma tabulação (TAB).

# \\
# Exibe uma barra invertida.

# \"
# Exibe aspas duplas.

# \'
# Exibe aspas simples.

# Os caracteres de escape tornam a exibição
# dos textos muito mais organizada.