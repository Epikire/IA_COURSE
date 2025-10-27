""" 2. Implemente um programa que leia um conjunto de números reais armazenando-
os em um vetor(lista). Após, calcule o quadrado dos componentes deste

vetor(lista), armazenando o resultado em outro vetor(lista). Os conjuntos têm 10
elementos cada. Ao final, imprima todos os vetores(listas). """

tamanho = 10

vetor_numero = []
vetor_quadrado = []

print(f"Digite {tamanho} números reais: ")

for i in range (tamanho):
    while True:
        try:
            entrada = input(f"Digite o {i + 1}º número: ")
            numero = float(entrada.replace(",", "."))
            vetor_numero.append(numero)

            break

        except ValueError:
            print("Entrada inválida. Por favor, digite um número real.")

vetor_quadrados = [num ** 2 for num in vetor_numero]

print(f"Vetor Original: {vetor_numero}")
print(f"Vetor Quadrados: {vetor_quadrados}")

