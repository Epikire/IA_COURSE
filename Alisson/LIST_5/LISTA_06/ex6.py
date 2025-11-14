matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        num = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

x = int(input("\nDigite o valor que deseja buscar: "))

encontrado = False

for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print(f"\nValor {x} encontrado na posição: linha {i}, coluna {j}")
            encontrado = True

if not encontrado:
    print("\nElemento não encontrado.")
