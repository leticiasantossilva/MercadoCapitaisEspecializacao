"""
Programa subtrai.py
Descrição: Este programa lê doir números do teclado, calcula o resultado da subtração e coloca o resultado na tela.
Autor: Nelson Seixas dos Santos
Data: 05/10/2023
Versão: 0.0.1
"""

# Importação de módulos

import es

import operacao


# Definição de funções




# Atribuição de variáveis

subtracao: float = 0.0

dados: list = []



# Entrada de dados

dados = es.entrada()



# Processamento de dados

subtracao = operacao.subtrai(dados[0], dados[1])


# Saída de dados

es.saida(dados[0], dados[1], subtracao)


