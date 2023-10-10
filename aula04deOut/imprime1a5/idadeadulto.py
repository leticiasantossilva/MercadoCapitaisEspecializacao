"""
Programa: idadeadulto
Descrição: Um programa que pergunte a idade de uma pessoa. Se a
idade for maior do que 18 anos, o programa imprime na tela o
texto ”Oi! Você  ́e um adulto.”
Autor:
Data:
Versão:
"""



# Atribuição de variáveis



# Entrada de dados

idade = int(input("Qual a sua idade?"))



# Processamento de dados

if idade >= 18:
    frase = "Você é um adulto."
else:
    frase = "Você é uma criança."


# Saída de dados
print(frase)
