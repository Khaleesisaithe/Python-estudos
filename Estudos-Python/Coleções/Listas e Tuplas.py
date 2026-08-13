# ==========================================================
# COLEÇÕES EM PYTHON
# LISTAS E TUPLAS
# ==========================================================

# Coleções são estruturas que permitem armazenar
# vários valores dentro de uma única variável.
#
# Neste estudo veremos:
#
# 1. Listas
# 2. Tuplas
#
# ==========================================================


# ==========================================================
# 1. LISTAS
# ==========================================================

# Uma lista é uma coleção de valores.
#
# As listas são representadas por colchetes [].
#
# Exemplo:

frutas = ["maçã", "banana", "laranja"]

print(frutas)

# Resultado:
# ['maçã', 'banana', 'laranja']


# Uma lista pode armazenar vários tipos de dados.

dados = ["Maria", 23, 1.70, True]

print(dados)

# Uma lista também pode conter outras listas.
#
# Isso será estudado com mais profundidade posteriormente.


# ==========================================================
# 2. ÍNDICES DAS LISTAS
# ==========================================================

# Assim como acontece com as strings,
# os elementos de uma lista possuem índices.
#
# O primeiro índice é sempre 0.
#
# Exemplo:
#
# frutas = ["maçã", "banana", "laranja"]
#
# maçã     -> índice 0
# banana   -> índice 1
# laranja  -> índice 2


print(frutas[0])

# Resultado:
# maçã


print(frutas[1])

# Resultado:
# banana


print(frutas[2])

# Resultado:
# laranja


# ==========================================================
# 3. ÍNDICES NEGATIVOS
# ==========================================================

# Também podemos acessar os elementos de trás para frente.
#
# -1 representa o último elemento.

print(frutas[-1])

# Resultado:
# laranja


print(frutas[-2])

# Resultado:
# banana


# ==========================================================
# 4. ALTERANDO UM ITEM DA LISTA
# ==========================================================

# Diferentemente das strings, as listas são mutáveis.
#
# Isso significa que podemos alterar seus elementos.

frutas[2] = "uva"

print(frutas)

# Resultado:
# ['maçã', 'banana', 'uva']


# O elemento que estava no índice 2 foi substituído.


# ==========================================================
# 5. APPEND()
# ==========================================================

# append() adiciona um novo elemento
# ao final da lista.

frutas.append("melancia")

print(frutas)

# Resultado:
# ['maçã', 'banana', 'uva', 'melancia']


# append() modifica a própria lista.
#
# Não precisamos fazer:
#
# frutas = frutas.append(...)
#
# Isso estaria errado.


# ==========================================================
# 6. REMOVE()
# ==========================================================

# remove() remove um elemento pelo seu valor.

frutas.remove("banana")

print(frutas)

# Resultado:
# ['maçã', 'uva', 'melancia']


# O remove() procura o valor informado
# e remove sua primeira ocorrência.


# ==========================================================
# 7. ALTERANDO ELEMENTOS PELO ÍNDICE
# ==========================================================

frutas = ["maçã", "banana", "laranja"]

# Vamos substituir laranja por uva.

frutas[2] = "uva"

print(frutas)

# Resultado:
# ['maçã', 'banana', 'uva']


# ==========================================================
# 8. LEN() EM LISTAS
# ==========================================================

# A função len() também pode ser utilizada
# para descobrir quantos elementos existem
# em uma lista.

frutas = ["maçã", "banana", "laranja"]

print(len(frutas))

# Resultado:
# 3


# IMPORTANTE:
#
# len() informa a quantidade de elementos.
#
# Os índices continuam começando em 0.


# ==========================================================
# 9. INSERT()
# ==========================================================

# insert() permite adicionar um elemento
# em uma posição específica.
#
# Sintaxe:
#
# lista.insert(índice, valor)


frutas = ["maçã", "banana", "laranja"]

frutas.insert(1, "uva")

print(frutas)

# Resultado:
# ['maçã', 'uva', 'banana', 'laranja']


# A uva foi inserida no índice 1.
#
# Os elementos que estavam depois dela
# foram deslocados para a direita.


# ==========================================================
# 10. POP()
# ==========================================================

# pop() remove um elemento pelo índice.

frutas = ["maçã", "banana", "laranja"]

frutas.pop(1)

print(frutas)

# Resultado:
# ['maçã', 'laranja']


# O elemento no índice 1 foi removido.


# ==========================================================
# 11. POP() SEM ÍNDICE
# ==========================================================

# Quando não informamos um índice,
# pop() remove o último elemento.

frutas = ["maçã", "banana", "laranja"]

fruta_removida = frutas.pop()

print(frutas)

print(fruta_removida)

# Resultado:
#
# ['maçã', 'banana']
# laranja


# Uma característica importante do pop()
# é que ele retorna o elemento removido.
#
# Por isso podemos armazená-lo em uma variável.


# ==========================================================
# 12. SORT()
# ==========================================================

# sort() organiza os elementos da lista.
#
# Para strings, a ordenação padrão é alfabética.

frutas = ["laranja", "banana", "maçã"]

frutas.sort()

print(frutas)

# Resultado:
# ['banana', 'laranja', 'maçã']


# sort() modifica a própria lista.


# ==========================================================
# 13. CLEAR()
# ==========================================================

# clear() remove todos os elementos da lista.

frutas = ["maçã", "banana", "laranja"]

frutas.clear()

print(frutas)

# Resultado:
# []


# A lista continua existindo,
# mas agora está vazia.


# ==========================================================
# 14. INDEX()
# ==========================================================

# index() informa o índice em que determinado
# valor está localizado.

frutas = ["maçã", "banana", "laranja"]

posicao = frutas.index("banana")

print(posicao)

# Resultado:
# 1


# ==========================================================
# 15. COUNT()
# ==========================================================

# count() informa quantas vezes determinado
# valor aparece na lista.

frutas = ["maçã", "banana", "maçã", "laranja"]

quantidade = frutas.count("maçã")

print(quantidade)

# Resultado:
# 2


# ==========================================================
# 16. COPY()
# ==========================================================

# Cuidado ao tentar copiar uma lista.
#
# Fazer isso:

frutas = ["maçã", "banana", "laranja"]

frutas2 = frutas

# NÃO cria uma nova lista.
#
# As duas variáveis passam a apontar
# para a mesma lista na memória.


frutas2.append("uva")

print(frutas)
print(frutas2)

# As duas listas terão "uva".


# ==========================================================
# 17. CRIANDO UMA CÓPIA REAL
# ==========================================================

# Para criar uma lista independente,
# podemos utilizar copy().

frutas = ["maçã", "banana", "laranja"]

frutas2 = frutas.copy()

frutas2.append("uva")

print(frutas)

print(frutas2)

# Resultado:
#
# ['maçã', 'banana', 'laranja']
# ['maçã', 'banana', 'laranja', 'uva']


# Agora são duas listas diferentes.


# ==========================================================
# 18. PRINCIPAIS MÉTODOS DAS LISTAS
# ==========================================================

# append()
# Adiciona um elemento ao final.
#
# remove()
# Remove um elemento pelo valor.
#
# insert()
# Adiciona um elemento em uma posição específica.
#
# pop()
# Remove um elemento pelo índice.
#
# sort()
# Ordena a lista.
#
# clear()
# Remove todos os elementos.
#
# index()
# Retorna a posição de um elemento.
#
# count()
# Conta quantas vezes um elemento aparece.
#
# copy()
# Cria uma cópia independente da lista.


# ==========================================================
# 19. TUPLAS
# ==========================================================

# Tuplas são coleções semelhantes às listas.
#
# A principal diferença é:
#
# LISTA  -> mutável
# TUPLA  -> imutável
#
# Uma tupla não pode ser alterada depois de criada.
#
# As tuplas são representadas normalmente
# utilizando parênteses ().


cores = ("vermelho", "verde", "azul")

print(cores)


# ==========================================================
# 20. ÍNDICES EM TUPLAS
# ==========================================================

# Assim como nas listas,
# podemos acessar os elementos pelo índice.

print(cores[0])

# Resultado:
# vermelho


print(cores[1])

# Resultado:
# verde


print(cores[-1])

# Resultado:
# azul


# ==========================================================
# 21. TUPLAS SÃO IMUTÁVEIS
# ==========================================================

# Não podemos alterar um elemento da tupla.

cores = ("vermelho", "verde", "azul")

# O código abaixo causaria um erro:

# cores[1] = "amarelo"


# Erro:
#
# TypeError
#
# Isso acontece porque as tuplas são imutáveis.


# Também não podemos utilizar métodos
# que alterem a estrutura da tupla,
# como append(), remove() ou pop().


# ==========================================================
# 22. O QUE PODEMOS FAZER COM TUPLAS?
# ==========================================================

# Podemos consultar seus elementos.

cores = ("vermelho", "verde", "azul")

print(cores[0])


# Podemos utilizar len():

print(len(cores))

# Resultado:
# 3


# Podemos utilizar index():

print(cores.index("verde"))

# Resultado:
# 1


# Podemos utilizar count():

cores = ("vermelho", "verde", "azul", "verde")

print(cores.count("verde"))

# Resultado:
# 2


# ==========================================================
# 23. QUANDO USAR LISTAS?
# ==========================================================

# Utilize listas quando os dados podem ser modificados.
#
# Exemplos:
#
# • Lista de compras
# • Produtos
# • Alunos
# • Notas
# • Tarefas
# • Itens de um carrinho
# • Dados que serão adicionados ou removidos


lista_de_compras = [
    "arroz",
    "feijão",
    "macarrão"
]

lista_de_compras.append("leite")


# ==========================================================
# 24. QUANDO USAR TUPLAS?
# ==========================================================

# Utilize tuplas quando os dados representam
# informações que não devem ser alteradas.
#
# Exemplos:
#
# • Meses do ano
# • Dias da semana
# • Coordenadas
# • Configurações fixas
# • Valores constantes


dias_da_semana = (
    "segunda",
    "terça",
    "quarta",
    "quinta",
    "sexta",
    "sábado",
    "domingo"
)


# ==========================================================
# 25. LISTA X TUPLA
# ==========================================================

# LISTA
#
# []
# Mutável
# Pode adicionar elementos
# Pode remover elementos
# Pode substituir elementos
#
#
# TUPLA
#
# ()
# Imutável
# Não pode adicionar elementos
# Não pode remover elementos
# Não pode substituir elementos


# ==========================================================
# 26. EXEMPLO PRÁTICO
# ==========================================================

# Lista de produtos de uma loja.

produtos = [
    "arroz",
    "feijão",
    "açúcar"
]

# Novo produto chegou.

produtos.append("café")

print(produtos)


# Produto foi retirado do estoque.

produtos.remove("açúcar")

print(produtos)


# Produto mudou de posição:

produtos.insert(1, "macarrão")

print(produtos)


# ==========================================================
# RESUMO
# ==========================================================

# LISTAS
#
# São coleções mutáveis.
#
# Exemplo:
#
# frutas = ["maçã", "banana", "laranja"]
#
#
# TUPLAS
#
# São coleções imutáveis.
#
# Exemplo:
#
# cores = ("vermelho", "verde", "azul")
#
#
# PRINCIPAIS CONCEITOS APRENDIDOS:
#
# • Coleções
# • Listas
# • Índices
# • Índices negativos
# • Alteração de elementos
# • append()
# • remove()
# • insert()
# • pop()
# • sort()
# • clear()
# • index()
# • count()
# • copy()
# • Tuplas
# • Imutabilidade
# • Diferença entre listas e tuplas