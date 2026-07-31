# ==========================================================
# ESTRUTURAS CONDICIONAIS EM PYTHON - PARTE 1
# ==========================================================

# As estruturas condicionais permitem que um programa
# tome decisões durante sua execução.
#
# Antes das condicionais, o código normalmente segue
# uma sequência fixa, sendo executado de cima para baixo.
#
# Com as condicionais, o programa pode analisar uma situação
# e escolher qual caminho deve seguir.


# ==========================================================
# O QUE É O IF?
# ==========================================================

# A palavra "if" significa "se" em inglês.
#
# Estrutura básica:
#
# if condição:
#     código que será executado
#
# O código dentro do if será executado somente
# quando a condição for verdadeira.


# ==========================================================
# EXEMPLO 1 - VERIFICANDO A IDADE
# ==========================================================

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")


# ==========================================================
# OPERADORES DE COMPARAÇÃO
# ==========================================================

# == -> Igual a

numero = 10

print(numero == 10)

# Resultado:
# True


# != -> Diferente de

print(numero != 5)

# Resultado:
# True


# > -> Maior que

print(20 > 18)

# Resultado:
# True


# < -> Menor que

print(15 < 18)

# Resultado:
# True


# >= -> Maior ou igual a

print(18 >= 18)

# Resultado:
# True


# <= -> Menor ou igual a

print(15 <= 18)

# Resultado:
# True


# ==========================================================
# DIFERENÇA ENTRE = E ==
# ==========================================================

# Um sinal de igual (=) atribui um valor.

nome = "Lucas"

# Dois sinais de igual (==) comparam valores.

print(nome == "Lucas")

# Resultado:
# True


# ==========================================================
# EXEMPLO 2 - SISTEMA DE SENHA
# ==========================================================

senha = "batatinha"

tentativa_senha = input("Digite sua senha: ")

if tentativa_senha == senha:
    print("Senha correta. Pode entrar.")
    print("Seja bem-vindo!")


# ==========================================================
# VERIFICANDO SE A SENHA ESTÁ INCORRETA
# ==========================================================

senha = "batatinha"

tentativa_senha = input("Digite sua senha: ")

if tentativa_senha != senha:
    print("Senha incorreta.")


# ==========================================================
# INDENTAÇÃO
# ==========================================================

# Em Python, a indentação é obrigatória.
#
# A indentação indica que uma linha
# pertence ao bloco do if.

idade = 20

if idade >= 18:
    print("Você é maior de idade.")
    print("Você pode continuar.")


# ==========================================================
# CÓDIGO FORA DO IF
# ==========================================================

idade = 15

if idade >= 18:
    print("Você é maior de idade.")

print("Fim do programa.")


# O último print() está fora do if.
# Por isso, ele será executado sempre.


# ==========================================================
# PYTHON DIFERENCIA MAIÚSCULAS E MINÚSCULAS
# ==========================================================

# Python é case-sensitive.
#
# "Batatinha" é diferente de "batatinha".

senha = "Batatinha"

tentativa = input("Digite a senha: ")

if tentativa == senha:
    print("Senha correta.")


# ==========================================================
# VALORES BOOLEANOS
# ==========================================================

# Toda comparação retorna:
#
# True  -> Verdadeiro
# False -> Falso

print(10 > 3)

# Resultado:
# True

print(1 > 3)

# Resultado:
# False


# ==========================================================
# TIPO BOOL
# ==========================================================

print(type(True))

# Resultado:
# <class 'bool'>

print(type(False))

# Resultado:
# <class 'bool'>


# True e False começam com letra maiúscula.

# Correto:
# True
# False

# Incorreto:
# true
# false


# ==========================================================
# UTILIZANDO TRUE E FALSE
# ==========================================================

if True:
    print("Esta mensagem sempre será exibida.")


if False:
    print("Esta mensagem nunca será exibida.")


# ==========================================================
# ARMAZENANDO UMA COMPARAÇÃO
# ==========================================================

resultado = 10 > 3

print(resultado)

# Resultado:
# True

print(type(resultado))

# Resultado:
# <class 'bool'>


if resultado:
    print("A comparação é verdadeira.")


# ==========================================================
# EXEMPLO COM RESULTADO FALSO
# ==========================================================

resultado = 1 > 3

print(resultado)

# Resultado:
# False


if resultado:
    print("Esta mensagem não será exibida.")


# ==========================================================
# FLUXO DE EXECUÇÃO
# ==========================================================

idade = 20

print("Início do programa.")

if idade >= 18:
    print("Maior de idade.")

print("Fim do programa.")


# ==========================================================
# RESUMO
# ==========================================================

# if
# Cria uma condição.
#
# ==
# Verifica se dois valores são iguais.
#
# !=
# Verifica se dois valores são diferentes.
#
# >
# Verifica se um valor é maior que outro.
#
# <
# Verifica se um valor é menor que outro.
#
# >=
# Verifica se um valor é maior ou igual.
#
# <=
# Verifica se um valor é menor ou igual.
#
# True
# Representa um resultado verdadeiro.
#
# False
# Representa um resultado falso.
#
# Indentação
# Define quais linhas pertencem a um bloco.


# ==========================================================
# PRÓXIMOS ASSUNTOS
# ==========================================================

# • else
# • elif
# • Operadores lógicos
# • and
# • or
# • not
# • Condicionais aninhadas