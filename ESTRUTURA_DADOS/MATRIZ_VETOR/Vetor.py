# ============================================================
# EXERCÍCIO DE VETORES
# Objetivo: criar um vetor (lista) com 6 números, somar posições específicas,
# modificar um elemento e imprimir cada valor em uma linha.
# ============================================================

# (a) Criar o vetor A com exatamente 6 números inteiros.
# Em Python, um "vetor" simples pode ser representado por uma LISTA, que usa colchetes [].
# Dentro dos colchetes, colocamos os números separados por vírgula.
A = [1, 0, 5, -2, -5, 7]  # aqui temos 6 valores: posições 0,1,2,3,4,5 (nessa ordem)

# (b) Somar os valores nas posições A[0], A[1] e A[5].
# A[0] significa: pegue o elemento na posição 0 (o primeiro elemento).
# A[1] significa: pegue o elemento na posição 1 (o segundo elemento).
# A[5] significa: pegue o elemento na posição 5 (o sexto elemento).
# Os parênteses () aqui NÃO são necessários para a soma, mas ajudam a leitura.
soma = (A[0] + A[1] + A[5])

# Mostrar (imprimir) a soma na tela.
# print() é uma função (tem parênteses) que escreve algo no console.
print("Soma de A[0] + A[1] + A[5] =", soma)

# (c) Modificar o vetor na posição 4, colocando o valor 100.
# Atenção: posição 4 é o QUINTO elemento porque começamos em 0.
# A[4] do jeito que está hoje vale -5; vamos trocar por 100.
A[4] = 100  # o sinal de igual (=) faz a ATRIBUIÇÃO (troca o valor)

# (d) Mostrar na tela cada valor do vetor A, um por linha.
# Vamos usar um laço "for" para percorrer os índices de 0 até o último índice.
# range(len(A)) cria uma sequência de números: 0,1,2,3,4,5 (porque len(A) == 6).
for i in range(len(A)):
    # A cada volta do laço, i é um número de índice.
    # A[i] acessa o elemento que está naquele índice.
    print("A[", i, "] =", A[i])