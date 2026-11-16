"""Exercício 5 – Soma de dois vetores

Desenvolva um programa em Python que leia 5 números inteiros para o vetor A e outros 5 números inteiros para o vetor B. Em seguida, o programa deverá gerar um terceiro vetor C, no qual cada elemento corresponde à soma dos elementos de mesma posição dos vetores A e B. Ao final, apresente os três vetores.
"""

# Exercício 5 - Soma de dois vetores

# Cria três listas com 5 posições
A = [0] * 5
B = [0] * 5
C = [0] * 5

# Leitura dos elementos do vetor A
print("----- Preenchimento do vetor A -----")

for i in range(5):
    A[i] = int(input(f"Digite o valor A[{i}]: "))

# Leitura dos elementos do vetor B
print("\n----- Preenchimento do vetor B -----")

for i in range(5):
    B[i] = int(input(f"Digite o valor B[{i}]: "))

# Soma dos elementos correspondentes
for i in range(5):

    # Soma os elementos de mesma posição
    # e armazena o resultado no vetor C
    C[i] = A[i] + B[i]

# Apresentação dos três vetores
print("\n----- Resultado -----")
print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)