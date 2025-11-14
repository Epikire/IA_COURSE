vendas = []

for i in range(12):
    linha = []
    print(f"\nDigite as vendas do mês {i+1}:")
    for j in range(4):
        valor = float(input(f"Semana {j+1}: "))
        linha.append(valor)
    vendas.append(linha)

total_mes = []
for i in range(12):
    soma_mes = sum(vendas[i])  
    total_mes.append(soma_mes)

total_semana = []
for j in range(4):
    soma_semana = 0
    for i in range(12):
        soma_semana += vendas[i][j]
    total_semana.append(soma_semana)

total_ano = sum(total_mes)
print("\nTotal vendido em cada mês:")
for i in range(12):
    print(f"Mês {i+1}: R$ {total_mes[i]:.2f}")

print("\nTotal vendido em cada semana (no ano todo):")
for j in range(4):
    print(f"Semana {j+1}: R$ {total_semana[j]:.2f}")

print(f"\nTotal vendido no ano: R$ {total_ano:.2f}")
