""" 6. Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os
valores lidos na ordem inversa. Utilizar laço de repetição e vetor(lista). """

tamanho = 6
lista = []

print(f"---- Leitura de {tamanho} Valores Inteiros ----")

for i in range(tamanho):
    while True:
        try:
            entrada_str = input(f"Digite o {i + 1}º valor inteiro: ")
            numero = int(entrada_str)

            lista.append(numero)

            break
        
        except ValueError:
            print(f"Entrada Inválida. Por favor, digite um número INTEIRO.")


print(f"Valores lidos na ordem original: {lista}")
print(f"Valors lidos na ordem inversa:")

for i in range(len(lista) -1, -1, -1):
    print(lista[i], end=)
