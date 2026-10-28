while True:
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if (senha == usuario):
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        break

print("Cadastro realizado com sucesso!")
