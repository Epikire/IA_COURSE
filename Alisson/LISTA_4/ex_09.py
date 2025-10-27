""" 9) Criar um algoritmo que imprima todos os números de 1 até 100, inclusive, e a soma de
todos eles. """

soma = 0

for i in range (1,101):
    contador = i + 1
    print(f"i: {i}")
    
    soma = soma + i

print(f"\nA soma de todos eles é: {soma}")