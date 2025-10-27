""" 7. Faça um programa que leia um vetor(lista) de 5 posições para números reais e,
depois, um código inteiro. Se o código lido for zero, finalize o programa; se for 1,
mostre o vetor(lista) na ordem direta; se for 2, mostre o vetor(lista) na ordem
inversa. Caso o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido. """

tamanho = 5
numeros = []

print(f"---- Leitura de {tamanho} Números Reais ----")
print(f"Por favor, digite 5 números: ")

for i in range(tamanho):
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º Número: ")
            entrada_valida = entrada_str.replace(',', '.')
            
            numero = float(entrada_valida)
            numeros.append(numero)

            break
        except ValueError:
            print("Entrada Inválida. Por favor, digite um número real.")

print("\n---- Leitura Concluida ----")
print(f"Lista lida: {numeros}")

while True:
    print("\n" + "=" * 30)
    print("      MENU DE OPÇÕES")
    print("=" * 30)

    print("   1: Mostrar lista na ordem direta")
    print("   2: Mostrar lista na ordem inversa")
    print("   0: Finalizar")
    print("-" * 30)

    try:
        codigo_str = input("Digite o código desejado: ")
        codigo = int(codigo_str)

        if codigo == 0:
            print("Finalizando o programa...")
            break

        elif codigo == 2:
            print("\n---- Lista na Ordem Inversa ----")

            for i in range(len(numeros) - 1, -1, -1):
                print(numeros[i])
        
        elif codigo == 1:
            print("\n ---- Lista na Ordem Direta ----")

            for num in numeros:
                print(num)
        
        else:
            print(f"Código '{codigo}' é inválido. Tente novamente.")
    
    except ValueError:
        print(f"Código '{codigo_str}' é inválido. Digite apenas 0, 1 ou 2.")

print("Programa encerrado.")