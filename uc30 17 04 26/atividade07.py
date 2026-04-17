vendas = [10, 16, 20, 8, 15, 12]

soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print("Soma dos valores pares:", soma)