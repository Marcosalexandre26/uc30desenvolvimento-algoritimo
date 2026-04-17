total = 0.0

while True:
    valor = float(input("Digite o valor do item (0 para finalizar): "))
    
    if valor == 0:
        break
    
    total += valor

print("Total da compra: R$", total)