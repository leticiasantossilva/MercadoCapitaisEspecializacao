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

posicao = 0


# Entrada de dados
p = int(input("Digite o valor a procurar: "))


# Processamento de dados

for elemento in lista:
    if elemento == p:
        achou = True
        posicao = lista[elemento]
        break


# Saída de dados

if achou:
    print(f"O valor {p} foi achado na posição {lista[posicao]}.")
else:
    print(f"O valor {p} não encontrado.")
