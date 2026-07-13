# ==========================================================
# VARIÁVEIS
# ==========================================================

# Uma variável é um espaço na memória utilizado para armazenar um valor.
# Neste exemplo, a variável "texto" recebe uma string (texto).

texto = "Estamos criando uma variável em texto."

print(texto)


# ----------------------------------------------------------
# ALTERANDO O VALOR DE UMA VARIÁVEL
# ----------------------------------------------------------

# Uma variável pode receber um novo valor a qualquer momento.
# O valor antigo é substituído pelo novo.

texto = "Agora você alterou o valor da variável."

print(texto)


# ----------------------------------------------------------
# ORDEM DE EXECUÇÃO
# ----------------------------------------------------------

# O Python executa o código de cima para baixo, linha por linha.
#
# Exemplo:
#
# texto = "Olá!"
# print(texto)
#
# Saída:
# Olá!
#
# Se removermos o primeiro print(), nada será exibido naquele momento.
# O Python continuará executando normalmente as próximas linhas.
#
# Exemplo:
#
# texto = "Primeiro valor"
#
# texto = "Segundo valor"
# print(texto)
#
# Saída:
# Segundo valor
#
# Isso acontece porque a variável recebeu um novo valor
# antes de ser exibida.


# ----------------------------------------------------------
# NameError E TRACEBACK
# ----------------------------------------------------------

# Se tentarmos utilizar uma variável antes de criá-la,
# o Python exibirá um erro chamado NameError.
#
# Exemplo:

# print(texto)
# texto = "Estamos criando uma variável."

# Resultado:
#
# NameError: name 'texto' is not defined
#
# O Traceback é o relatório de erro mostrado pelo Python.
# Ele informa:
#
# • Em qual arquivo ocorreu o erro;
# • Em qual linha aconteceu;
# • Qual foi o tipo do erro;
# • Uma descrição do problema.
#
# Aprender a ler o Traceback é uma das habilidades mais
# importantes para qualquer programador Python.


# ----------------------------------------------------------
# ERROS DE DIGITAÇÃO (SyntaxError e NameError)
# ----------------------------------------------------------

# Pequenos erros de digitação também fazem o programa falhar.
#
# Exemplos:
#
# ptint(texto)
#
# Resultado:
# NameError
#
# O Python procurará uma função chamada "ptint",
# mas ela não existe.
#
#
# print(teSto)
#
# Resultado:
# NameError
#
# Como "teSto" nunca foi criado como variável,
# o Python exibirá um erro.
#
# Sempre que ocorrer um erro, ele será mostrado no terminal
# juntamente com o Traceback.


# ----------------------------------------------------------
# REGRAS PARA CRIAR VARIÁVEIS
# ----------------------------------------------------------

# Existem algumas regras importantes para nomear variáveis.


# 1) Utilize apenas:
#
# • Letras (A-Z, a-z)
# • Números (0-9)
# • Underscore (_)
#
# Exemplos válidos:
#
# nome
# idade
# nome_completo
# aluno1


# 2) A variável NÃO pode começar com um número.
#
# Correto:
#
# idade1
# aluno2
#
# Incorreto:
#
# 1idade
# 123nome


# 3) Espaços não são permitidos.
#
# Correto:
#
# nome_completo
#
# Incorreto:
#
# nome completo


# 4) Não utilize palavras reservadas do Python.
#
# Exemplos:
#
# if
# else
# for
# while
# class
# def
# import
# return
#
# Essas palavras fazem parte da linguagem.


# 5) Python diferencia letras maiúsculas e minúsculas.
#
# Exemplo:
#
# nome = "João"
# Nome = "Maria"
#
# São duas variáveis completamente diferentes.


# 6) Escolha nomes claros e descritivos.
#
# Evite:
#
# x
# y
# a1
# abc
#
# Prefira:
#
# nome
# idade
# salario
# nota_final
# quantidade_produtos
#
# Um bom nome facilita a leitura do código e torna a
# manutenção muito mais simples.


# ----------------------------------------------------------
# BOAS PRÁTICAS
# ----------------------------------------------------------

# ✔ Utilize nomes que façam sentido.
#
# ✔ Escreva tudo em letras minúsculas.
#
# ✔ Separe palavras utilizando underscore (_).
#
# Exemplo:
#
# nome_completo = "Felipe França"
#
# Isso é muito mais legível do que:
#
# nc = "Felipe França"
#
# Um código bem escrito é mais fácil de entender,
# revisar e manter, tanto por você quanto por outros
# programadores.