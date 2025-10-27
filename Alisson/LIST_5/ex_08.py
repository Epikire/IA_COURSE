""" 8. Implemente um programa que leia dois conjuntos de números reais, armazenando-
os em vetor(lista)es. Após, calcule o produto escalar entre eles. Os conjuntos têm

5 elementos cada. Ao final, imprimir os dois conjuntos e o produto escalar, sendo
que o produto escalar é dado por: x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn. """


tamanho = 5

vetor_a = []
print(f"\n ---- Leitura do Conjunto 1 ----")

for i in range(tamanho):
    
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º número: ")
            entrada_valida = entrada_str.replace(',', '.')

            numero = float(entrada_valida)
            vetor_a.append(numero)

            break

        except ValueError:
            print(f"Entrada Inválida. Por favor, digite um número real. ")

vetor_b = []
print(f"\n ---- Leitura do Conjunto 2 ----")

for i in range(tamanho):

    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º Número: ")
            entrada_valida = entrada_str.replace(',', '.')

            numero = float(entrada_valida)
            vetor_b.append(numero)

            break

        except ValueError:
            print(f"Entrada Inválida. Por favor, digite um número real.")

escalar = 0.0

for i in range(tamanho):
    escalar += vetor_a[i] * vetor_b[i]

print("\n" + "=" * 30)
print("---- CÁLCULO DO PRODUTO ESCALAR ----")
print("=" * 30)

print(f"Conjunto 1: {vetor_a}")
print(f"Conjunto 2: {vetor_b}")

print(f"\n Produto Escalar: {escalar:.2f}")