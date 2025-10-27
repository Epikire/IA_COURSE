# ============================================================
# MATRIZ 5x5: 1 na diagonal principal, 0 no resto (identidade)
# Versão hiper-comentada para calouros
# ============================================================

# 'tamanho' guarda o número de linhas e colunas (5, porque é 5x5).
tamanho = 5

# 'identidade' será a nossa matriz (lista de listas). Começa vazia: [].
# Cada 'linha' que criarmos (também uma lista) será colocada aqui dentro depois.
identidade = []

# Vamos construir a matriz linha por linha.
# 'for i in range(tamanho)' cria um laço com i = 0, 1, 2, 3, 4 (5 valores).
# Obs: 'range(5)' não inclui o 5, para no 4.
for i in range(tamanho):  # i representa o índice da LINHA atual

    # Começamos uma nova 'linha' vazia (lista).
    # Ex.: primeiro será [], depois vamos colocar 5 números nela usando append.
    linha = []

    # Agora criamos as colunas dessa linha.
    # 'for j in range(tamanho)' faz j = 0, 1, 2, 3, 4 (5 valores).
    for j in range(tamanho):  # j representa o índice da COLUNA atual

        # (i == j) testa se estamos numa posição da DIAGONAL PRINCIPAL.
        # Ex.: [0][0], [1][1], [2][2], [3][3], [4][4].
        if i == j:
            # Se for diagonal, colocamos 1.
            # Por quê 1? Porque na matriz IDENTIDADE a diagonal principal é toda de 1,
            # e isso faz a identidade "não mudar" um vetor/matriz quando multiplica.
            linha.append(1)   # append adiciona o '1' NO FINAL da lista 'linha'.
        else:
            # Se NÃO for diagonal (posição fora da diagonal), colocamos 0.
            # Por quê 0? Para garantir que só a diagonal tenha 1;
            # os zeros "zeram" os outros produtos na multiplicação de matrizes.
            linha.append(0)   # adiciona o '0' ao final da lista 'linha'.

    # Quando a linha tiver 5 números, colocamos a linha completa dentro da matriz.
    # Ex.: a primeira linha pode virar [1, 0, 0, 0, 0], e assim por diante.
    identidade.append(linha)   # agora 'identidade' recebe essa 'linha' como mais um elemento.

# Impressão simples da matriz, uma linha por vez.
# '\n' apenas pula uma linha antes de imprimir o título.
print("\nMatriz 5x5 (identidade):")

# Outro laço para mostrar cada linha da matriz 'identidade'.
for i in range(tamanho):  # i = 0..4
    # Aqui usamos 'print(identidade[i])' para imprimir a lista que representa a linha i.
    # Vai aparecer com colchetes mesmo, o que é ótimo para visualização simples:
    # [1, 0, 0, 0, 0]
    # [0, 1, 0, 0, 0]
    # ...
    print(identidade[i])
