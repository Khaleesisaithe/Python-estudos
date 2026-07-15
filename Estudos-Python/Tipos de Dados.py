# ==========================================================
# TIPOS DE DADOS
# ==========================================================

# Um tipo de dado define quais valores uma variável pode armazenar
# e quais operações podem ser realizadas com esses valores.
#
# Os quatro tipos básicos mais utilizados em Python são:
#
# • str   -> Texto (String)
# • int   -> Número inteiro (Integer)
# • float -> Número decimal (Floating Point Number)
# • bool  -> Valor lógico (Boolean)


# ----------------------------------------------------------
# STRING (str)
# ----------------------------------------------------------

# Uma string é uma sequência de caracteres utilizada para representar
# textos dentro do programa.
#
# Strings podem conter:
#
# • Letras
# • Números
# • Símbolos
# • Espaços
#
# Elas devem estar entre aspas simples (' ')
# ou aspas duplas (" ").

texto = "Olá, mundo!"
nome = "Felipe"
frase = "Python é uma linguagem de programação."

print(texto)
print(nome)
print(frase)

# Tipo:
# str


# ----------------------------------------------------------
# INTEGER (int)
# ----------------------------------------------------------

# O tipo int representa números inteiros,
# ou seja, números que NÃO possuem casas decimais.

idade = 23
ano = 2026
quantidade = 1500

print(idade)
print(ano)
print(quantidade)

# Tipo:
# int


# ----------------------------------------------------------
# FLOAT (float)
# ----------------------------------------------------------

# O tipo float representa números com casas decimais.
#
# Em Python utiliza-se ponto (.)
# em vez de vírgula (,).
#
# Exemplo:
#
# Correto:
# 3.14
#
# Incorreto:
# 3,14

pi = 3.14159
altura = 1.75
temperatura = 28.5

print(pi)
print(altura)
print(temperatura)

# Tipo:
# float


# ----------------------------------------------------------
# BOOLEAN (bool)
# ----------------------------------------------------------

# O tipo bool representa valores lógicos.
#
# Existem apenas dois valores possíveis:
#
# True
# False
#
# Atenção:
# Em Python escrevemos True e False
# sempre com a primeira letra maiúscula.

ativo = True
logado = False

print(ativo)
print(logado)

# Tipo:
# bool


# ----------------------------------------------------------
# DESCOBRINDO O TIPO DE UMA VARIÁVEL
# ----------------------------------------------------------

# Podemos utilizar a função type()
# para descobrir qual é o tipo de um valor.

nome = "Python"

print(type(nome))

# Resultado:
# <class 'str'>


idade = 23

print(type(idade))

# Resultado:
# <class 'int'>


altura = 1.80

print(type(altura))

# Resultado:
# <class 'float'>


ativo = True

print(type(ativo))

# Resultado:
# <class 'bool'>


# ----------------------------------------------------------
# PYTHON X JAVA
# ----------------------------------------------------------

# Uma das maiores diferenças entre Python e Java
# é a forma como declaramos as variáveis.

# Em Python, NÃO precisamos informar o tipo da variável.
# O próprio Python identifica automaticamente.

nome = "Carlos"
idade = 20
altura = 1.80
ativo = True

# O Python entende sozinho que:
#
# nome -> str
# idade -> int
# altura -> float
# ativo -> bool


# Em Java é diferente.
#
# O tipo precisa ser informado antes do nome da variável.

# Exemplo em Java:

# String nome = "Carlos";
# int idade = 20;
# double altura = 1.80;
# boolean ativo = true;

# Isso é chamado de tipagem estática.
#
# Já o Python utiliza tipagem dinâmica,
# pois o tipo é identificado automaticamente
# durante a execução do programa.


# ----------------------------------------------------------
# RESUMO
# ----------------------------------------------------------

# str
# Utilizado para armazenar textos.

# int
# Utilizado para armazenar números inteiros.

# float
# Utilizado para armazenar números com casas decimais.

# bool
# Utilizado para representar valores lógicos
# (True ou False).


# ==========================================================
# CURIOSIDADE
# ==========================================================

# Em Python tudo é um objeto.
#
# Isso significa que até mesmo números,
# textos e valores booleanos possuem
# propriedades e métodos próprios.
#
# Exemplo:

print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))

# Resultado:
#
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
#
# Conforme você evoluir nos estudos,
# entenderá melhor o conceito de objetos
# e programação orientada a objetos (POO).