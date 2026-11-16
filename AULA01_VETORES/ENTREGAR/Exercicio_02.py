"""Exercício 2 – Menor valor do vetor

Desenvolva um programa em Python que leia 10 números inteiros e armazene-os em um vetor. Ao final, o programa deverá apresentar o menor valor encontrado e a posição (índice) em que ele se encontra.
"""

# Exercício 2 - Menor valor do vetor

# Cria uma lista com 10 posições
vetor = [0] * 10

# Variável utilizada para armazenar o menor valor
# Inicialmente recebe um valor muito grande
menor = 1000000

# Armazena a posição do menor valor encontrado
menorIndice = 0

# Leitura dos 10 números
for i in range(10):
    vetor[i] = int(input(f"Digite o valor {i}: "))

    # Verifica se o número digitado é menor que o atual
    if vetor[i] < menor:

        # Atualiza o menor valor
        menor = vetor[i]

        # Guarda o índice em que o menor valor foi encontrado
        menorIndice = i

# Apresentação dos resultados
print("\n----- Resultado -----")
print(f"O menor valor do vetor é {menor}")
print(f"O menor valor está no índice {menorIndice}")