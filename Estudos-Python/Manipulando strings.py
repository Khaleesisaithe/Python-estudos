# ==========================================================
# MANIPULAÇÃO DE STRINGS EM PYTHON
# ==========================================================
#
# Strings são utilizadas para representar textos em Python.
#
# Podemos manipular strings para:
#
# • Acessar caracteres específicos
# • Fazer fatiamentos
# • Contar caracteres ou ocorrências
# • Encontrar posições dentro do texto
# • Verificar se determinado texto existe em uma string
# • Alterar maiúsculas e minúsculas
# • Remover espaços
# • Substituir partes de um texto
# • Padronizar dados
#
# Esses recursos são muito importantes em:
#
# • Automação
# • Tratamento de dados
# • Ciência de Dados
# • APIs
# • Arquivos CSV
# • Processamento de texto
# • Sistemas de cadastro
#
# ==========================================================


# ==========================================================
# 1. INDEXAÇÃO DE STRINGS
# ==========================================================

# Cada caractere de uma string possui uma posição.
#
# Essa posição é chamada de índice (index).
#
# IMPORTANTE:
#
# O Python começa a contar os índices a partir do ZERO.
#
# Exemplo:
#
# Palavra:  M E L A N C I A
# Índice:   0 1 2 3 4 5 6 7 8
#
# Portanto:
#
# M -> índice 0
# E -> índice 1
# L -> índice 2
# A -> índice 3
# N -> índice 4
# C -> índice 5
# I -> índice 6
# A -> índice 7


fruta = "melancia"

print(fruta[0])

# Resultado:
# m


print(fruta[2])

# Resultado:
# l


print(fruta[5])

# Resultado:
# c


# ==========================================================
# 2. ÍNDICES NEGATIVOS
# ==========================================================

# Também podemos acessar uma string de trás para frente.
#
# Para isso utilizamos índices negativos.
#
# Exemplo:
#
# M E L A N C I A
# -8 -7 -6 -5 -4 -3 -2 -1
#
# O índice -1 representa o último caractere.


print(fruta[-1])

# Resultado:
# a


print(fruta[-2])

# Resultado:
# i


print(fruta[-3])

# Resultado:
# c


# ==========================================================
# 3. FATIAMENTO DE STRINGS
# ==========================================================

# Podemos pegar uma parte da string utilizando:
#
# string[início:fim]
#
# O índice inicial é incluído.
#
# O índice final NÃO é incluído.
#
# Essa é uma regra muito importante do Python.


fruta = "melancia"

print(fruta[0:3])

# Resultado:
# mel
#
# Índices utilizados:
#
# 0 -> m
# 1 -> e
# 2 -> l
#
# O índice 3 não é incluído.


# ==========================================================
# 4. PEGANDO OS PRIMEIROS CARACTERES
# ==========================================================

# Quando não informamos o índice inicial,
# o Python começa automaticamente do índice 0.

print(fruta[:3])

# Resultado:
# mel


print(fruta[:5])

# Resultado:
# melan


# ==========================================================
# 5. PEGANDO DO MEIO ATÉ O FINAL
# ==========================================================

# Quando não informamos o índice final,
# o Python continua até o final da string.

print(fruta[2:])

# Resultado:
# lancia


print(fruta[4:])

# Resultado:
# ncia


# ==========================================================
# 6. FATIAMENTO COM ÍNDICES NEGATIVOS
# ==========================================================

print(fruta[-3:])

# Resultado:
# cia


print(fruta[:-2])

# Resultado:
# melanc


# ==========================================================
# REGRA IMPORTANTE DO FATIAMENTO
# ==========================================================

# Em:
#
# fruta[0:3]
#
# O Python começa no índice 0
# e para antes do índice 3.
#
# Portanto:
#
# 0 -> incluído
# 1 -> incluído
# 2 -> incluído
# 3 -> NÃO incluído


# ==========================================================
# 7. LEN()
# ==========================================================

# A função len() retorna a quantidade
# de caracteres de uma string.
#
# Diferentemente dos índices,
# a contagem começa considerando
# a quantidade real de caracteres.


frase = "Eu amo Python"

print(len(frase))

# Resultado:
# 13


# Atenção:
#
# O espaço também é considerado um caractere.


# Podemos armazenar o resultado em uma variável.

tamanho_frase = len(frase)

print(tamanho_frase)

# Resultado:
# 13


print(f"A frase possui {tamanho_frase} caracteres.")


# ==========================================================
# 8. COUNT()
# ==========================================================

# O método count() informa quantas vezes
# determinado valor aparece dentro de uma string.


frase = "Eu amo Python"

quantidade = frase.count("o")

print(quantidade)

# Resultado:
# 2


# A letra "o" aparece duas vezes:
#
# Eu amO PythOn


# Podemos procurar palavras ou trechos maiores.

frase = "Python é muito legal. Eu amo Python."

print(frase.count("Python"))

# Resultado:
# 2


# ==========================================================
# 9. FIND()
# ==========================================================

# O método find() retorna o índice da primeira ocorrência
# de determinado caractere ou trecho.


frase = "Eu amo Python"

posicao = frase.find("m")

print(posicao)

# Resultado:
# 4


# Podemos confirmar utilizando a indexação:

print(frase[4])

# Resultado:
# m


# ==========================================================
# FIND() QUANDO NÃO ENCONTRA O TEXTO
# ==========================================================

# Se o valor procurado não existir,
# find() retorna -1.


print(frase.find("Java"))

# Resultado:
# -1


# Isso pode ser utilizado para verificar
# se determinado texto foi encontrado.


# ==========================================================
# 10. VERIFICANDO SE UM TEXTO EXISTE
# ==========================================================

# Podemos utilizar o operador "in"
# para verificar se determinado texto
# está presente em uma string.


frase = "Eu amo Python"

if "Python" in frase:
    print("Python está na frase.")


# Resultado:
# Python está na frase.


if "Java" in frase:
    print("Java está na frase.")
else:
    print("Java não está na frase.")


# Resultado:
# Java não está na frase.


# ==========================================================
# 11. LOWER()
# ==========================================================

# lower() transforma todos os caracteres
# da string em letras minúsculas.


frase = "Eu Amo Python"

print(frase.lower())

# Resultado:
# eu amo python


# IMPORTANTE:
#
# O método não altera a variável original.


print(frase)

# Resultado:
# Eu Amo Python


# Para salvar a alteração:

frase = frase.lower()

print(frase)

# Resultado:
# eu amo python


# ==========================================================
# 12. UPPER()
# ==========================================================

# upper() transforma todos os caracteres
# da string em letras maiúsculas.


frase = "Eu amo Python"

print(frase.upper())

# Resultado:
# EU AMO PYTHON


# Assim como lower(), upper()
# não altera a variável original.


# Para armazenar a alteração:

frase = frase.upper()

print(frase)

# Resultado:
# EU AMO PYTHON


# ==========================================================
# 13. CAPITALIZE()
# ==========================================================

# capitalize() transforma a primeira letra
# da string em maiúscula.


frase = "eu amo python"

print(frase.capitalize())

# Resultado:
# Eu amo python


# Apenas a primeira letra da string
# será capitalizada.


# ==========================================================
# 14. STRIP()
# ==========================================================

# strip() remove espaços em branco
# do início e do final da string.


frase = "     Eu amo Python     "

print(frase.strip())

# Resultado:
# Eu amo Python


# Os espaços no meio da frase
# não são removidos.


# ==========================================================
# 15. LSTRIP()
# ==========================================================

# lstrip() remove os espaços
# do lado esquerdo da string.


frase = "     Python     "

print(frase.lstrip())

# Resultado:
# Python


# Os espaços da direita permanecem.


# ==========================================================
# 16. RSTRIP()
# ==========================================================

# rstrip() remove os espaços
# do lado direito da string.


frase = "     Python     "

print(frase.rstrip())

# Resultado:
#      Python


# Os espaços da esquerda permanecem.


# ==========================================================
# 17. REPLACE()
# ==========================================================

# replace() substitui uma parte da string
# por outra.


frase = "Eu amo Python"

print(frase.replace("Python", "Java"))

# Resultado:
# Eu amo Java


# Podemos substituir caracteres.

frase = "Eu amo Python"

print(frase.replace("o", "X"))

# Resultado:
# Eu amX PythXn


# IMPORTANTE:
#
# replace() também não altera a variável original
# automaticamente.


# Para salvar a alteração:

frase = frase.replace("Python", "Java")

print(frase)


# ==========================================================
# 18. TITLE()
# ==========================================================

# title() coloca a primeira letra
# de cada palavra em maiúscula.


frase = "eu amo python"

print(frase.title())

# Resultado:
# Eu Amo Python


# Isso pode ser útil para padronizar
# nomes e títulos.


# ==========================================================
# 19. COMBINANDO MÉTODOS
# ==========================================================

# Podemos utilizar vários métodos
# em sequência.


nome = "     lucas matheus     "

nome = nome.strip().title()

print(nome)

# Resultado:
# Lucas Matheus


# Primeiro:
#
# strip()
#
# Remove os espaços extras.
#
# Depois:
#
# title()
#
# Capitaliza cada palavra.


# ==========================================================
# 20. PADRONIZAÇÃO DE DADOS
# ==========================================================

# Esse tipo de manipulação é muito importante
# na Ciência de Dados.
#
# Imagine que uma base de dados possui:

nome1 = " Lucas "
nome2 = "LUCAS"
nome3 = "lucas"


# Para o computador, inicialmente,
# esses valores são diferentes.


# Podemos padronizá-los:

nome1 = nome1.strip().lower()
nome2 = nome2.strip().lower()
nome3 = nome3.strip().lower()


print(nome1)
print(nome2)
print(nome3)

# Resultado:
#
# lucas
# lucas
# lucas


# Agora podemos comparar os valores
# de maneira mais confiável.


# ==========================================================
# 21. STRINGS E CIÊNCIA DE DADOS
# ==========================================================

# Na Ciência de Dados, dados de texto frequentemente
# precisam ser tratados antes da análise.
#
# Exemplos de problemas:
#
# • Espaços extras
# • Letras maiúsculas e minúsculas
# • Erros de padronização
# • Textos duplicados
# • Valores escritos de formas diferentes
#
# Métodos como:
#
# strip()
# lower()
# upper()
# replace()
# title()
#
# ajudam no processo de limpeza e padronização.


# ==========================================================
# 22. RESUMO DOS PRINCIPAIS RECURSOS
# ==========================================================

# string[índice]
# Acessa um caractere específico.
#
# string[início:fim]
# Faz o fatiamento da string.
#
# len(string)
# Retorna a quantidade de caracteres.
#
# string.count()
# Conta quantas vezes um valor aparece.
#
# string.find()
# Encontra a posição da primeira ocorrência.
#
# "texto" in string
# Verifica se determinado texto existe.
#
# string.lower()
# Converte para minúsculas.
#
# string.upper()
# Converte para maiúsculas.
#
# string.capitalize()
# Coloca a primeira letra da string em maiúscula.
#
# string.title()
# Coloca a primeira letra de cada palavra em maiúscula.
#
# string.strip()
# Remove espaços do início e do final.
#
# string.lstrip()
# Remove espaços do lado esquerdo.
#
# string.rstrip()
# Remove espaços do lado direito.
#
# string.replace()
# Substitui partes da string.