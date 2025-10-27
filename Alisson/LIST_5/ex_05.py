""" 5. Faça um programa para ler a nota da prova de 15 alunos e armazene num
vetor(lista), calcule e imprima a média geral. """

alunos = 15
notas = []

print(f"---- Leitura das Notas de {alunos} Alunos ---")
print(f"Digite as notas: ")

for i in range(alunos):

    while True:
        try:
            entrada_str = input(f"Digite a nota do aluno {i + 1}: ")
            entrada_valida = entrada_str.replace(',', '.')

            nota = float(entrada_valida)

            if nota < 0:
                print("Nota inválida. A nota não pode ser negativa. Tente novamente!")
            
            else:
                notas.append(nota)

                break
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


soma = sum(notas)
media = soma / len(notas)

print(f" ---- Cálculo da Média Conclúido ----")
print(f"Número de alunos: {len(notas)}")
print(f"Soma total das notas: {soma:.2f}")
print(f"\nA média da turma é: {media:.2f}")

