""" 3. Faça um programa que receba do usuário um vetor(lista) com 20 posições. Em
seguida deverá ser impresso o maior e o menor elemento do vetor(lista). """

tamanho = 20
vetor = []

print(f"Digite {tamanho} números. ")

for i in range(tamanho):
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º número: ")

            entrada_valida = entrada_str.replace(',', ".")

            numero = float(entrada_valida)

            vetor.append(numero)

            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número. ")

maior = max(vetor)
menor = min(vetor)

print("--- Processamento Concluido ---")
print(f"\n O maior elemento da lista é: {maior}")
print(f"\n O menor elemento da lista é: {menor}")
