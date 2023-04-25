while True:
    # Lê o nome de usuário e a senha
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    # Verifica se a senha é igual ao nome de usuário
    if senha == nome:
        print("Erro: a senha não pode ser igual ao nome de usuário!")
    else:
        print("Usuário e senha cadastrados com sucesso!")
        break  # Sai do loop
