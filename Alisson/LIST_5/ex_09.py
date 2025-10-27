""" 9. Implemente um programa que receba 10 números inteiros e mostre:
• Os números pares digitados;
• A soma dos números pares digitados;
• Os números ímpares digitados;
• A quantidade de números ímpares digitados; """


total_numero = 10

numeros_impares = []
numeros_pares = []

soma_pares = 0

print(f"---- Leitura de {total_numero} Números Inteiros ----")

for i in range(total_numero):
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º número inteiro: ")
            numero = int(entrada_str)

            break
        except ValueError:
            print(f"Entrada Inválida. Por favor, digite um número inteiro. ")

    if numero % 2 == 0:
        numeros_pares.append(numero)
        soma_pares += numero

    else:
        numeros_impares.append(numero)

print("\n" + "=" * 30)
print("---- ANÁLISE DOS NÚMEROS ----")
print("=" * 30)

if numeros_pares:
    print(f"Os números pares digitados foram: {numeros_pares}")

else:
    print(f"Nenhum número par foi digitado.")

print(f"A soma dos números pares é: {soma_pares}")

print("-" * 30)

if numeros_impares:
    print(f"Os números impares digitados foram: {numeros_impares}")

else:
    print(f"Nenhum número impar foi digitado.")

print(f"A quantidade de números impares digitados é: {len(numeros_impares)}")
