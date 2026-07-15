# ==========================================================
# STRINGS EM PYTHON
# ==========================================================

# String (str) é um tipo de dado utilizado para armazenar textos.
#
# Além de armazenar informações, as strings possuem diversos
# métodos que permitem manipular seu conteúdo.
#
# Alguns dos métodos mais utilizados são:
#
# • title()
# • upper()
# • lower()


# ----------------------------------------------------------
# MÉTODO title()
# ----------------------------------------------------------

# O método title() transforma a primeira letra de cada palavra
# em maiúscula e as demais em minúsculas.

nome = "lucas matheus"

print(nome.title())

# Resultado:
# Lucas Matheus

# Observe que utilizamos:
#
# nome.title()
#
# e não:
#
# title(nome)
#
# Isso acontece porque title() é um método pertencente
# ao tipo de dado string.


# Outro exemplo

cidade = "são josé dos campos"

print(cidade.title())

# Resultado:
# São José Dos Campos


# ----------------------------------------------------------
# MÉTODO upper()
# ----------------------------------------------------------

# O método upper() converte TODAS as letras
# da string para maiúsculas.

nome = "Lucas Matheus"

print(nome.upper())

# Resultado:
# LUCAS MATHEUS


# Exemplos

print("python".upper())

# PYTHON

print("Data Science".upper())

# DATA SCIENCE


# ----------------------------------------------------------
# MÉTODO lower()
# ----------------------------------------------------------

# O método lower() converte TODAS as letras
# para minúsculas.

nome = "LUCAS MATHEUS"

print(nome.lower())

# Resultado:
# lucas matheus


# Outro exemplo

texto = "PyThOn"

print(texto.lower())

# Resultado:
# python


# ----------------------------------------------------------
# AS STRINGS SÃO IMUTÁVEIS
# ----------------------------------------------------------

# Um detalhe importante:
#
# Os métodos title(), upper() e lower()
# NÃO alteram a variável original.
#
# Eles apenas retornam uma NOVA string.

nome = "Lucas"

print(nome.upper())

# Resultado:
# LUCAS

print(nome)

# Resultado:
# Lucas

# Perceba que a variável continua exatamente igual.


# Se quisermos salvar a alteração,
# devemos fazer uma nova atribuição.

nome = nome.upper()

print(nome)

# Resultado:
# LUCAS

# Agora sim a variável passou a armazenar
# o novo valor.


# O mesmo acontece com lower() e title().

nome = nome.lower()

print(nome)

# Resultado:
# lucas


# ----------------------------------------------------------
# PADRONIZAÇÃO DE DADOS
# ----------------------------------------------------------

# Imagine que um usuário possa digitar seu nome
# da forma que desejar.

# Exemplos:

# LUCAS
# Lucas
# lucas
# LuCaS

# Todos representam a mesma pessoa,
# porém escritos de maneiras diferentes.

# Podemos padronizar essas informações.

nome = "LuCaS"

print(nome.lower())

# lucas

print(nome.upper())

# LUCAS

print(nome.title())

# Lucas

# Essa técnica é muito utilizada em cadastros,
# sistemas de login, bancos de dados e formulários.


# ----------------------------------------------------------
# CONCATENAÇÃO DE STRINGS
# ----------------------------------------------------------

# Concatenar significa unir duas ou mais strings.

primeiro_nome = "Lucas"
sobrenome = "Shippuden"

nome_completo = primeiro_nome + " " + sobrenome

print(nome_completo)

# Resultado:
# Lucas Shippuden

# Observe que adicionamos um espaço (" ")
# entre as duas palavras.


# ----------------------------------------------------------
# MAIS EXEMPLOS DE CONCATENAÇÃO
# ----------------------------------------------------------

print("Olá, " + nome_completo + "!")

# Resultado:
# Olá, Lucas Shippuden!


print("Bem-vindo ao Python, " + primeiro_nome + ".")

# Resultado:
# Bem-vindo ao Python, Lucas.


curso = "Python"

print(primeiro_nome + " está estudando " + curso + ".")

# Resultado:
# Lucas está estudando Python.


cidade = "São Paulo"

print(nome_completo + " mora em " + cidade + ".")

# Resultado:
# Lucas Shippuden mora em São Paulo.


# Também podemos armazenar o resultado
# em outra variável.

mensagem = "Olá, " + nome_completo + "!"

print(mensagem)


# ----------------------------------------------------------
# ONDE ISSO É UTILIZADO?
# ----------------------------------------------------------

# Manipulação de strings está presente em praticamente
# qualquer aplicação.

# Exemplos:

# • Cadastro de usuários
# • Login
# • Sistemas bancários
# • Redes sociais
# • Lojas virtuais
# • APIs
# • Chatbots
# • Inteligência Artificial
# • Ciência de Dados


# ----------------------------------------------------------
# STRINGS NA CIÊNCIA DE DADOS
# ----------------------------------------------------------

# Em Ciência de Dados é muito comum trabalhar
# com grandes quantidades de textos.

# Exemplos:

# Nome dos clientes
# Cidade
# Estado
# País
# E-mails
# Comentários
# Avaliações de produtos
# Mensagens de redes sociais

# Imagine uma base de dados como esta:

# lucas
# LUCAS
# Lucas
# LuCaS

# Apesar de representarem a mesma pessoa,
# o computador entende que são textos diferentes.

# Podemos padronizar tudo utilizando lower().

nome = "LuCaS"

nome = nome.lower()

print(nome)

# Resultado:
# lucas

# Isso facilita:
#
# • Pesquisas
# • Agrupamentos
# • Filtros
# • Geração de relatórios
# • Machine Learning
# • Limpeza de dados (Data Cleaning)

# Grande parte do trabalho de um Cientista de Dados
# consiste justamente em limpar, organizar e padronizar
# informações antes de analisá-las.


# ==========================================================
# RESUMO
# ==========================================================

# title()
# Primeira letra de cada palavra em maiúscula.

# upper()
# Todas as letras em maiúsculas.

# lower()
# Todas as letras em minúsculas.

# +
# Une (concatena) duas ou mais strings.

# Strings são imutáveis.
# Os métodos retornam uma nova string.
# Para salvar a alteração, faça uma nova atribuição:

# nome = nome.lower()
# nome = nome.upper()
# nome = nome.title()