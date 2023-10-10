"""
Programa: busca
Descrição: 
Autor:
Data:
Versão:
"""



# Atribuição de variáveis

lista = [1, 5, 2, 87, 31]

achou = False
x = 0



# Entrada de dados
p = int(input("Digite o valor a procurar: "))


# Processamento de dados

while x < len(lista):
    if lista[x] == p:
        achou = True
        break
    x += 1     # é a sintaxe de x=x+1


# Saída de dados

if achou:
    print(f"O valor {p} foi achado na posição {x}.")
else:
    print(f"O valor {p} não encontrado.")
