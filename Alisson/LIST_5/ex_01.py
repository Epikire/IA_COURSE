""" Faça um programa que contenha um vetor(lista) denominado A para armazenar 6
números inteiros. O programa deve executar os seguintes passos:
a) Atribua os seguintes valores a esse vetor(lista): 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira (simples) a soma entre os valores das
posições [0], A[1] e A[5] do vetor(lista) e mostre na tela esta soma.
c) Modifique o vetor(lista) na posição 4, atribuindo a esta posição o valor
100.
d) Mostre na tela cada valor do vetor(lista) A, um em cada linha. """

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(f"A soma dos valores nas posições 0, 1 e 5 é: {soma}")

A[4] = 100

print("\nValores do vetor A (um por linha): ")
for valor in A:
    print(valor)