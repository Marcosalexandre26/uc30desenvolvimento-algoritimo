def controle_financeiro(mesada, gastos):
    total = sum(gastos)
    if total < mesada:

        print("João não gastou muito dinheiro")

    elif total == mesada:
        
        print("João usou exatamente sua mesada.")

    else:
        print("João usou mais do que tinha.")


mesada = 1000
gastos = [220, 180, 400, 100]
controle_financeiro(mesada, gastos)