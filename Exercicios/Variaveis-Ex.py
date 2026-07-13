# ==========================================================
#               EXERCÍCIOS - VARIÁVEIS EM PYTHON
# ==========================================================
#
# Regras:
# 1. Resolva um exercício por vez.
# 2. Não olhe as soluções antes de tentar.
# 3. Após terminar todos, compare com as respostas.
#
# ==========================================================


# ==========================================================
# EXERCÍCIO 1
# ==========================================================
#
# Crie uma variável chamada "nome".
# Armazene seu nome nela.
# Depois exiba o conteúdo utilizando print().
#
# Sua resposta abaixo:
#

nome = "Khaleesi"

print (nome)


# ==========================================================
# EXERCÍCIO 2
# ==========================================================
#
# Crie uma variável chamada "idade".
# Guarde sua idade nela.
# Depois imprima essa variável.
#
# Sua resposta abaixo:
#

idade = "24"

print (idade)


# ==========================================================
# EXERCÍCIO 3
# ==========================================================
#
# Crie três variáveis:
#
# nome
# idade
# cidade
#
# Depois imprima cada uma delas.
#
# Sua resposta abaixo:
#

nome = "Sarah Mulins"
idade = "10"
cidade = "Jardim Granja, SJC"

print (nome)
print (idade)
print (cidade)

# ==========================================================
# EXERCÍCIO 4
# ==========================================================
#
# Crie uma variável chamada "comida".
# Guarde sua comida favorita.
#
# Depois altere essa variável para outra comida.
#
# Imprima apenas o valor final.
#
# Sua resposta abaixo:
#

comida = "Pizza e Strogonoff"

print (comida)


# ==========================================================
# EXERCÍCIO 5
# ==========================================================
#
# Crie uma variável chamada "numero".
#
# Guarde qualquer número.
#
# Depois altere esse número.
#
# Imprima o novo valor.
#
# Sua resposta abaixo:
#

numero = "365"

print (numero)

numero = "456"

print (numero)


# ==========================================================
# EXERCÍCIO 6
# ==========================================================
#
# Crie uma variável chamada "profissao".
#
# Guarde uma profissão.
#
# Depois imprima:
#
# Minha profissão é:
#
# Na linha seguinte imprima a variável.
#
# Sua resposta abaixo:
#

profissao = "Programadora"

print ("Minha proffisao é:")
print (profissao)


# ==========================================================
# EXERCÍCIO 7
# ==========================================================
#
# Analise o código abaixo.
#
# texto = "Python"
# texto = "Java"
#
# O que será impresso?
#
# Faça o teste.
#
# Sua resposta abaixo:
#

texto = "Python"
texto = "Java"

print (texto)

# ==========================================================
# EXERCÍCIO 8
# ==========================================================
#
# O código abaixo possui um erro.
#
# print(nome)
#
# nome = "Carlos"
#
# Descubra:
#
# 1. Qual é o erro?
# 2. Por que ele acontece?
#
# Escreva sua resposta abaixo:
#
# ERRO "PRINT" ESTA POSICIONADO ANTES 


# ==========================================================
# EXERCÍCIO 10 (DESAFIO)
# ==========================================================
#
# Antes de executar, tente descobrir qual será a saída.
#
# numero = 10
#
# numero = 30
#
# numero = 50
#
# print(numero)
#
# Depois execute e veja se acertou.
#
# Sua resposta abaixo:
#

numero = 10
numero = 30
numero = 50

print(numero)







# ==========================================================
# ==========================================================
#                    SOLUÇÕES
# ==========================================================
# ==========================================================


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 1
# ==========================================================

nome = "Maria"

print(nome)

# Correção:
# Você criou uma variável do tipo texto (string)
# e exibiu seu conteúdo.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 2
# ==========================================================

idade = 23

print(idade)

# Correção:
# A variável idade normalmente utiliza um número inteiro (int).


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 3
# ==========================================================

nome = "Maria"
idade = 23
cidade = "São Paulo"

print(nome)
print(idade)
print(cidade)

# Correção:
# Foram criadas três variáveis diferentes e exibidas com print().


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 4
# ==========================================================

comida = "Pizza"

comida = "Lasanha"

print(comida)

# Correção:
# O valor da variável foi alterado.
# O valor anterior deixou de existir.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 5
# ==========================================================

numero = 10

numero = 50

print(numero)

# Correção:
# Variáveis podem receber novos valores quantas vezes forem necessárias.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 6
# ==========================================================

profissao = "Programador"

print("Minha profissão é:")
print(profissao)

# Correção:
# Você utilizou um texto fixo junto com uma variável.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 7
# ==========================================================

texto = "Python"

texto = "Java"

print(texto)

# Saída:
# Java

# Correção:
# O último valor atribuído à variável é o que será armazenado.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 8
# ==========================================================

# print(nome)
#
# nome = "Carlos"

# Resultado:
#
# NameError:
# name 'nome' is not defined

# Correção:
# O Python executa o código de cima para baixo.
# Como a variável ainda não existia quando print() foi chamado,
# ocorreu um NameError.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 9
# ==========================================================

nome = "Maria"
idade = 23
cidade = "São Paulo"
altura = 1.70
profissao = "Programadora"

print(nome)
print(idade)
print(cidade)
print(altura)
print(profissao)

# Correção:
# Foram utilizadas variáveis de tipos diferentes:
# string, inteiro e número decimal.


# ==========================================================
# SOLUÇÃO - EXERCÍCIO 10
# ==========================================================

numero = 10

numero = 30

numero = 50

print(numero)

# Saída:
# 50

# Correção:
# A variável sempre armazena apenas o último valor recebido.


# ==========================================================
# PARABÉNS!
# ==========================================================
#
# Se você conseguiu resolver a maioria sem consultar as respostas,
# já compreendeu os conceitos fundamentais sobre variáveis.
#
# Próximos assuntos recomendados:
#
# • Tipos de dados (int, float, str, bool)
# • input()
# • Operadores matemáticos
# • Operadores relacionais
# • Operadores lógicos
# • Estruturas condicionais (if, elif e else)
#
# Continue praticando. Programação se aprende escrevendo código,
# corrigindo erros e entendendo por que eles aconteceram.
#
# ==========================================================