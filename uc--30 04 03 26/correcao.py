# --- Parte 1: Quadrado ou Cubo ---
numero = int(input("Digite um valor: "))

if numero % 2 == 0:
    resultado = numero ** 2
else:
    resultado = numero ** 3

print("Resultado:", resultado)


# --- Parte 2: Verificação de usuário e senha ---
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == "procopio" and senha == "12345":
    print("Seja bem-vindo!")
else:
    print("Usuário e senha não conferem!")


# --- Parte 3: Sistema de tentativas de senha ---
nome = input("Digite seu nome: ")
senhaCorreta = "123456"

tentativa = 3

while tentativa > 0:
    senha = input("Digite sua senha: ")

    if senha == senhaCorreta:
        print(f"Olá {nome}! Seja bem-vindo!")
        break
    else:
        tentativa -= 1

        if tentativa == 2:
            print("Senha incorreta! Você tem 2 tentativas.")
        elif tentativa == 1:
            print("Senha incorreta! Você tem 1 tentativa.")
        else:
            print("Senha bloqueada!")