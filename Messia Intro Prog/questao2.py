# Solicita ao usuário o número de maçãs compradas
num_macas = int(input("Digite o número de maçãs compradas: "))

# Calcula o custo total da compra
if num_macas < 12:
    custo_total = num_macas * 1.30
else:
    custo_total = num_macas * 1.00

# Exibe o custo total
print(f"O custo total da compra é R$ {custo_total:.2f}")
