usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")

def listar_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    
    print("=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['nome']} | E-mail: {usuario['email']}")
        print()

def menu():
    while True:
        print("=== SISTEMA DE CADASTRO ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuário")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuario()
        elif opcao == "3":
            print("Parando o sistema...")
            break
        else:
            print("Opção inválida.\n")

menu()
        
  
