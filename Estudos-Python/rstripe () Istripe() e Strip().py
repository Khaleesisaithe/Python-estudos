# ==========================================================
# REMOVENDO ESPAÇOS EM BRANCO
# ==========================================================

# Durante o uso de um programa, é comum que o usuário
# digite espaços antes ou depois de um texto.
#
# Exemplo:
#
# "   Lucas"
# "Lucas   "
# "   Lucas   "
#
# Esses espaços podem causar problemas em comparações,
# pesquisas e cadastros.
#
# Para resolver isso, Python oferece três métodos:
#
# • strip()
# • lstrip()
# • rstrip()


# ----------------------------------------------------------
# strip()
# ----------------------------------------------------------

# O método strip() remove os espaços
# do INÍCIO e do FINAL da string.
#
# Os espaços do meio NÃO são alterados.

nome = "      Lucas Matheus      "

print(nome.strip())

# Resultado:
#
# Lucas Matheus


# Outro exemplo

cidade = "     São Paulo     "

print(cidade.strip())

# Resultado:
#
# São Paulo


# Observe que a variável original continua igual.

print(nome)

# Resultado:
#
#       Lucas Matheus


# Para salvar a alteração:

nome = nome.strip()

print(nome)

# Resultado:
#
# Lucas Matheus


# ----------------------------------------------------------
# lstrip()
# ----------------------------------------------------------

# O método lstrip() remove apenas os espaços
# do lado esquerdo (Left Strip).

texto = "      Python"

print(texto.lstrip())

# Resultado:
#
# Python


# Os espaços da direita permanecem.

texto = "      Python      "

print(texto.lstrip())

# Resultado:
#
# Python


# ----------------------------------------------------------
# rstrip()
# ----------------------------------------------------------

# O método rstrip() remove apenas os espaços
# do lado direito (Right Strip).

texto = "Python      "

print(texto.rstrip())

# Resultado:
#
# Python


texto = "      Python      "

print(texto.rstrip())

# Resultado:
#
#       Python


# ----------------------------------------------------------
# COMPARAÇÃO DOS TRÊS MÉTODOS
# ----------------------------------------------------------

texto = "     Python     "

print(texto.strip())

# Resultado:
#
# Python


print(texto.lstrip())

# Resultado:
#
# Python_____


print(texto.rstrip())

# Resultado:
#
# _____Python

# (Os traços representam os espaços que permaneceram.)


# ----------------------------------------------------------
# STRINGS CONTINUAM IMUTÁVEIS
# ----------------------------------------------------------

# Assim como upper(), lower() e title(),
# esses métodos NÃO alteram a variável original.

nome = "     Lucas     "

print(nome.strip())

print(nome)

# Resultado:
#
# Lucas
#
#      Lucas


# Para alterar definitivamente:

nome = nome.strip()

print(nome)

# Resultado:
#
# Lucas


# ----------------------------------------------------------
# REMOVENDO OUTROS CARACTERES
# ----------------------------------------------------------

# strip() também pode remover caracteres específicos.

texto = "....Python...."

print(texto.strip("."))

# Resultado:
#
# Python


texto = "#####Python#####"

print(texto.strip("#"))

# Resultado:
#
# Python


texto = "___Lucas___"

print(texto.strip("_"))

# Resultado:
#
# Lucas


# Também funciona com letras.

texto = "xxxPythonxxx"

print(texto.strip("x"))

# Resultado:
#
# Python


# ----------------------------------------------------------
# ONDE ISSO É UTILIZADO?
# ----------------------------------------------------------

# Esses métodos aparecem em praticamente
# qualquer sistema.

# Exemplos:

# • Cadastro de usuários
# • Login
# • Formulários
# • Bancos de dados
# • APIs
# • Arquivos CSV
# • Planilhas
# • Ciência de Dados
# • Machine Learning


# ----------------------------------------------------------
# EXEMPLO PRÁTICO
# ----------------------------------------------------------

# Imagine que um usuário digitou:

nome = "      Lucas      "

# Antes de salvar no banco:

nome = nome.strip()

print(nome)

# Resultado:
#
# Lucas

# Agora o dado foi padronizado.