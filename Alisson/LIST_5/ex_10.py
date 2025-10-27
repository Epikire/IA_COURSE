""" 10. Faça um programa para ler 10 números DIFERENTES a serem armazenados em
um vetor(lista). Os dados deverão ser armazenados no vetor(lista) na ordem que
forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado
anteriormente, o programa deverá pedir para ele digitar outro número. Note que
cada valor digitado pelo usuário deve ser pesquisado no vetor(lista), verificando
se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor(lista)
final que foi digitado, ou seja, sem nenhuma repetição. """


tamanho = 10
vetor = []

print(f" ---- Leitura de {tamanho} Números Diferentes ----")
print(f"O programa não aceitará números repetidos.")
print("=" * 30)

while len(vetor) < tamanho:
    texto = f"Digite o {len(vetor) + 1}º número: "

    try:
        entrada_str = input(texto)
        entrada_valida = entrada_str.replace(",", ".")

        numero = float(entrada_valida)

        if numero in vetor:
            print(f"   -> ERRO: O número {numero} já foi digitado.")
            print(f"   -> Por favor, digite um número diferente. \n")
        
        else:
            vetor.append(numero)
            print(f"   -> Número {numero} adicionado com sucesso.\n")
    
    except ValueError:
        print(f"   -> ERRO: Entrada {entrada_str} não é um número válido.")


print("=" * 30)
print("Coleta Concluída!")
print(f"A lista final com {tamanho} números únicos é:")
print(vetor)
