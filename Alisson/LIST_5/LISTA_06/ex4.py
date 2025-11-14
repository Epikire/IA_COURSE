matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

soma_linhas = [0, 0, 0]
soma_colunas = [0, 0, 0]

for i in range(3):
    for j in range(3):
        soma_linhas[i] += matriz[i][j]   
        soma_colunas[j] += matriz[i][j]  
print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print("\nSoma de cada linha:", soma_linhas)
print("Soma de cada coluna:", soma_colunas)
