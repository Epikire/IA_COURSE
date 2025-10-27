""" 10) Criar um algoritmo que imprima todos os números de 1 até 100, inclusive, e a média
de todos eles. """

soma = 0

for i in range (1,101):
    contador = i + 1
    print(f"{i}º Valor: {i}")

    soma = soma + i

media = soma / contador

print(f"A media dos valores é: {media}")