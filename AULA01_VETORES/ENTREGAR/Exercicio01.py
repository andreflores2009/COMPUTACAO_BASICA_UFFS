# -*- coding: utf-8 -*-
"""
Exercício 1 – Preenchimento de três vetores

Desenvolva um programa em Python que permita ao usuário preencher três vetores (listas), denominados A, B e C, cada um contendo 5 números inteiros. Após o preenchimento, o programa deverá apresentar todos os elementos dos três vetores.
"""

# Exercício 1 - Preenchimento de três vetores

# Cria três listas com 5 posições, inicialmente preenchidas com zero
A = [0] * 5
B = [0] * 5
C = [0] * 5

# Preenchimento do vetor A
print("----- Preenchimento do vetor A -----")

for i in range(5):
    A[i] = int(input(f"Digite o valor A[{i}]: "))

# Preenchimento do vetor B
print("\n----- Preenchimento do vetor B -----")

for i in range(5):
    B[i] = int(input(f"Digite o valor B[{i}]: "))

# Preenchimento do vetor C
print("\n----- Preenchimento do vetor C -----")

for i in range(5):
    C[i] = int(input(f"Digite o valor C[{i}]: "))

# Apresentação dos elementos dos três vetores
print("\n----- Valores armazenados -----")

print("Vetor A:", A)
print("Vetor B:", B)
print("Vetor C:", C)
