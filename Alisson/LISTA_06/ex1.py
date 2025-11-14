matriz = []  
soma = 0     

for i in range(5):
    linha = []
    for j in range(5):
        num = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(num)
        soma += num  
    matriz.append(linha)


print("\nMatriz digitada:")
for linha in matriz:
    print(linha)


print("\nA soma de todos os elementos é:", soma)

