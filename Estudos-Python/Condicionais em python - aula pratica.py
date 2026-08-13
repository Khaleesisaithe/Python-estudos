# ==========================================================
# AULA PRÁTICA - CONDICIONAIS EM PYTHON
# ==========================================================
#
# Nesta aula, vamos praticar:
#
# • if
# • elif
# • else
# • Operadores de comparação
# • Operadores lógicos
# • and
# • match/case
# • Entrada de dados com input()
# • Conversão de dados com float()
#
# As estruturas condicionais permitem que o programa
# tome decisões de acordo com uma condição.
#
# Exemplo:
#
# Se a nota for maior ou igual a 6:
#     O aluno foi aprovado.
#
# Caso contrário:
#     O aluno não foi aprovado.


# ==========================================================
# EXERCÍCIO 1 - VERIFICADOR DE NOTA
# ==========================================================

# Objetivo:
#
# Criar um programa que verifica se uma pessoa
# atingiu a nota mínima para ser aprovada.


# A variável armazena a nota mínima necessária.

nota_minima = 6


# input() recebe a resposta do usuário.
#
# float() converte a resposta para um número decimal.

nota = float(input("Digite sua nota: "))


# O programa compara a nota informada
# com a nota mínima.

if nota >= nota_minima:
    print("Parabéns, você passou!")


# Explicação:
#
# nota >= nota_minima
#
# Significa:
#
# "A nota é maior ou igual à nota mínima?"
#
# Se a resposta for True:
#
# A mensagem será exibida.
#
# Se a resposta for False:
#
# Nenhuma mensagem será exibida.


# Exemplo:
#
# Nota: 8
#
# Resultado:
#
# Parabéns, você passou!


# ==========================================================
# EXERCÍCIO 2 - COMPARANDO NOMES
# ==========================================================

# Objetivo:
#
# Criar um programa que recebe dois nomes
# e verifica se eles são diferentes.


nome1 = input("Digite um nome: ")

nome2 = input("Digite outro nome: ")


# != significa:
#
# "É diferente de?"

if nome1 != nome2:
    print("Os nomes são diferentes!")


# Se os nomes forem iguais,
# nenhuma mensagem será exibida.


# Exemplo 1:
#
# Primeiro nome:
# Pedro
#
# Segundo nome:
# Rodrigo
#
# Resultado:
#
# Os nomes são diferentes!


# Exemplo 2:
#
# Primeiro nome:
# João
#
# Segundo nome:
# João
#
# Resultado:
#
# Nenhuma mensagem será exibida.


# ==========================================================
# EXERCÍCIO 3 - VERIFICADOR DE IDADE
# ==========================================================

# Objetivo:
#
# Verificar se uma pessoa possui a idade mínima
# para participar de um evento.


idade = int(input("Digite sua idade: "))


# A idade mínima é 15 anos.

if idade >= 15:
    print("Você pode participar do evento.")


# Explicação:
#
# Se a idade for:
#
# 15 ou maior:
#
# A pessoa poderá participar.
#
# Menor que 15:
#
# Nenhuma mensagem será exibida.


# Exemplos:
#
# Idade: 16
#
# Resultado:
#
# Você pode participar do evento.
#
#
# Idade: 15
#
# Resultado:
#
# Você pode participar do evento.
#
#
# Idade: 14
#
# Resultado:
#
# Nenhuma mensagem será exibida.


# ==========================================================
# EXERCÍCIO 4 - AVALIAÇÃO DE FILMES
# ==========================================================

# Objetivo:
#
# Receber uma nota e classificar a avaliação
# do filme.

#elif no Python
#O elif (abreviação de else if) é usado para testar múltiplas condições em sequência.
#
#🎯 Por que usar?
#Evita o efeito "escadinha" (vários if e else aninhados).
#
#Garante um código limpo, organizado e fácil de ler.
#
#⚙️ Regra de Ouro da Execução
#O Python avalia as condições de cima para baixo e PARA no primeiro teste verdadeiro (True).
#
#Apenas um bloco de código será executado.
#
#Se o if for verdadeiro, todos os elif e o else abaixo são ignorados.


nota = float(
    input("Qual nota você dá para esse filme? ")
)


# O Python verifica as condições
# de cima para baixo.

if nota >= 9:
    print("Excelente!")

elif nota >= 7:
    print("Muito bom!")

elif nota >= 5:
    print("Regular.")

else:
    print("Ruim.")


# Explicação:
#
# Se a nota for:
#
# 9 ou maior:
# Excelente!
#
# De 7 até 8.99:
# Muito bom!
#
# De 5 até 6.99:
# Regular.
#
# Menor que 5:
# Ruim.


# Importante:
#
# A ordem das condições é importante.
#
# O Python executa apenas o primeiro
# bloco verdadeiro. 



# ==========================================================
# EXERCÍCIO 5 - FRETE GRÁTIS
# ==========================================================

# Objetivo:
#
# Verificar se uma pessoa pode receber
# frete grátis.


valor_da_compra = 105

ta_no_programa = True


# O operador and exige que as duas
# condições sejam verdadeiras.

if valor_da_compra >= 100 and ta_no_programa:
    print("Frete grátis aplicado!")

else:
    print("Frete não disponível no momento!")


# Explicação:
#
# Condição 1:
#
# A compra é maior ou igual a R$ 100?
#
# Condição 2:
#
# A pessoa participa do programa?
#
# As duas condições precisam ser True.


# Exemplo:
#
# valor_da_compra = 105
#
# ta_no_programa = True
#
# Resultado:
#
# Frete grátis aplicado!


# Se uma das condições for False:
#
# O frete não será aplicado.


# ==========================================================
# OPERADOR LÓGICO AND
# ==========================================================

# True and True
#
# Resultado:
# True


# True and False
#
# Resultado:
# False


# False and True
#
# Resultado:
# False


# False and False
#
# Resultado:
# False


# ==========================================================
# EXERCÍCIO 6 - MEIOS DE TRANSPORTE
# ==========================================================

# Objetivo:
#
# Identificar o tipo de transporte
# informado pelo usuário.


transporte = input(
    "Digite um meio de transporte: "
)


# match verifica o valor informado
# e executa o case correspondente.


match transporte:

    case "carro":
        print("Veículo terrestre.")

    case "bicicleta":
        print("Veículo sustentável.")

    case "avião" | "helicóptero":
        print("Transporte aéreo.")

    case _:
        print("Transporte desconhecido.")


# Explicação:
#
# case "carro":
#
# Executa o código se o usuário
# digitar "carro".
#
#
# case "avião" | "helicóptero":
#
# O símbolo | significa "ou".
#
# O mesmo código será executado
# para avião ou helicóptero.
#
#
# case _:
#
# É o caso padrão.
#
# Será executado quando nenhuma
# das opções anteriores for encontrada.


# ==========================================================
# IMPORTANTE - MATCH É CASE-SENSITIVE
# ==========================================================

# Python diferencia letras maiúsculas
# e minúsculas.
#
# "carro" é diferente de "Carro".
#
# Para evitar esse problema,
# podemos usar lower().


transporte = input(
    "Digite um meio de transporte: "
).lower()


match transporte:

    case "carro":
        print("Veículo terrestre.")

    case "bicicleta":
        print("Veículo sustentável.")

    case "avião" | "helicóptero":
        print("Transporte aéreo.")

    case _:
        print("Transporte desconhecido.")


# Agora o programa aceita:
#
# carro
# CARRO
# Carro
# CaRrO
#
# Todos serão convertidos para:
#
# carro


# ==========================================================
# RESUMO DA AULA
# ==========================================================

# if
#
# Executa um bloco se uma condição
# for verdadeira.
#
#
# elif
#
# Verifica uma nova condição.
#
#
# else
#
# É executado quando nenhuma condição
# anterior for verdadeira.
#
#
# and
#
# Exige que todas as condições
# sejam verdadeiras.
#
#
# match
#
# Compara um valor com diferentes casos.
#
#
# case
#
# Define uma possibilidade.
#
#
# case _
#
# Define o caso padrão.
#
#
# input()
#
# Recebe uma informação do usuário.
#
#
# int()
#
# Converte um valor para número inteiro.
#
#
# float()
#
# Converte um valor para número decimal.
#
#
# lower()
#
# Converte o texto para letras minúsculas.


