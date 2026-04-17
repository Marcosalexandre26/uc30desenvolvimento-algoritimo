try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Magro")
    else:
        if imc <= 24.9:
            print("Normal")
        else:
            print("Acima do peso")

except:
    print("Erro! Digite apenas números.")