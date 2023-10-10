"""
Programa subtrai.py
Descrição: Este programa lê doir números do teclado, calcula o resultado da subtração e coloca o resultado na tela.
Autor: Nelson Seixas dos Santos
Data: 05/10/2023
Versão: 0.0.3
"""

# Definição de funções

def subtrai(x: float, y: float) -> float:
    return x - y


def entrada():
    numeros = []
    i = 0
    while i < 2:    # Importante para interromper o while
        numeros.append(float(input("Digite o primeiro número: ")))
        i += 1  # Isto é o mesmo que escrever i = i+1
    return numeros


def saida(numero_1: float, numero_2: float, subtracao: float) -> None:
    print(f"O resultado da subtração do número {numero_1} do número {numero_2} é igual a {subtracao}.")
#




# Atribuição de variáveis

subtracao: float = 0.0

dados: list = []



# Entrada de dados

"""
numero_1 = float(input("Digite o primeiro número: "))

numero_2 = float(input("Digite o segundo número: "))
"""

dados = entrada()




# Processamento de dados

subtracao = subtrai(dados[0], dados[1])




# Saída de dados

"""
print(f"O resultado da subtração do número {numero_1} do número {numero_2} é igual a {subtracao}.")
"""

saida(dados[0], dados[1], subtracao)


