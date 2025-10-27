""" 4. Fazer um programa para ler 15 valores e, em seguida, mostrar o valor e a posição
onde se encontram o maior e o menor valor. """

tamanho = 15
valor = []

print(f"Digite {tamanho} números.")

for i in range(tamanho):
    
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º Número: ")
            entrada_valida = entrada_str.replace(',', ".")

            numero = float(entrada_valida)

            valor.append(numero)

            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

maior_valor = valor[0]
posicao_maior = 0
menor_valor = valor[0]
posicao_menor = 0

for i in range(1, tamanho):
    if valor[i] > maior_valor:
        maior_valor = valor[i]
        posicao_maior = i
    
    if valor[i] < menor_valor:
        menor_valor = valor[i]
        posicao_menor = i

print(f"----- Processamento Concluido ----")

print(f"\nA lista digitada foi {valor}\n")
print(f"O maior valor digitado foi: {maior_valor}")
print(f"Ele foi encontrado na posição: {posicao_maior}")
print(f"\nO menor valor digitado foi: {menor_valor}")
print(f"Ele foi encontrado na posição: {posicao_menor}")

