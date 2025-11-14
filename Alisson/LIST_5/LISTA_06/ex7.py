respostas = []
for i in range(5):
    linha = []
    print(f"\nDigite as respostas do aluno {i+1}:")
    for j in range(10):
        r = input(f"Questão {j+1}: ").strip().upper()  
        linha.append(r)
    respostas.append(linha)

gabarito = []
print("\nDigite o gabarito das 10 questões:")
for j in range(10):
    g = input(f"Gabarito da questão {j+1}: ").strip().upper()
    gabarito.append(g)

resultado = [0, 0, 0, 0, 0]  

for i in range(5):  
    for j in range(10):  
        if respostas[i][j] == gabarito[j]:
            resultado[i] += 1

print("\nPontuação dos alunos:")
for i in range(5):
    print(f"Aluno {i+1}: {resultado[i]} acertos")
