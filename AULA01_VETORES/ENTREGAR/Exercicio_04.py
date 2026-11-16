"""Exercício 4 – Soma e média dos elementos

Desenvolva um programa em Python que leia 8 números e armazene-os em um vetor. Após o preenchimento, o programa deverá calcular e apresentar a soma de todos os elementos e a média dos valores armazenados.
"""

# Exercício 4 - Soma e média dos elementos

# Cria uma lista com 8 posições
vetor = [0] * 8

# Leitura dos 8 números
print("----- Leitura dos valores -----")

for i in range(8):
    vetor[i] = float(input(f"Digite o valor {i}: "))

# Inicializa a variável que armazenará a soma
soma = 0

# Percorre todos os elementos da lista
for i in range(8):

    # Acrescenta o valor atual à soma
    soma += vetor[i]

# Calcula a média dividindo a soma por 8
media = soma / 8

# Apresentação dos resultados
print("\n----- Resultado -----")
print(f"Soma dos elementos: {soma:.2f}")
print(f"Média dos elementos: {media:.2f}")