"""Exercício 3 – Contagem de números pares e ímpares

Desenvolva um programa em Python que leia 10 números inteiros e armazene-os em um vetor. O programa deverá identificar e apresentar (mensagem na tela) a quantidade de números pares e ímpares armazenados.
"""

# Exercício 3 - Contagem de números pares e ímpares

# Cria uma lista com 10 posições
vetor = [0] * 10

# Inicializa os contadores
pares = 0
impares = 0

# Leitura dos valores
for i in range(10):
    vetor[i] = int(input(f"Digite o valor {i}: "))

    # O operador % retorna o resto da divisão
    # Se o resto da divisão por 2 for zero, o número é par
    if vetor[i] % 2 == 0:
        pares += 1

    # Caso contrário, o número é ímpar
    else:
        impares += 1

# Apresentação dos resultados
print("\n----- Resultado -----")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")