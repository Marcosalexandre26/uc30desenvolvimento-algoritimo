notas = [5, 8, 7, 9, 6, 10, 4]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade de notas acima de 7:", contador)