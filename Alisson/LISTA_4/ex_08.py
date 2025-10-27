""" 8) Escreva um algoritmo que receba dez números do usuário e imprima a metade de cada
número."""

print("---- Calculadora da metade de 10 número ----")

for i in range (1,11):
    numero = float(input(f"\nDigite o {i}º número: "))
    metade = numero / 2

    print(f"A metade de {numero:.0f} é {metade}")

print("|||||  FIM DO CALCULO |||||")