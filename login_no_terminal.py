import csv


file_name = 'usuarios.dat'

def verificar_login(nome, senha):
            with open('usuarios.dat', 'r', newline='') as file:
                reader = csv.reader(file)
                for linha in reader:
                    if linha[0] == nome and linha[1] == senha:
                        return True
                return False

def cadastrar_usuario(nome, senha):
            with open('usuarios.dat', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nome, senha])
            print("Usuário cadastrado com sucesso.")

def main():
    while True:
        opcao = input("Selecione uma opção:\n1. Cadastrar usuário\n2. Fazer login\n3. Sair\nOpção: ")
        if opcao == '1':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, senha)
        elif opcao == '2':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            if verificar_login(nome, senha):
                print("Login realizado com sucesso.")
            else:
                print("Nome de usuário ou senha incorretos.")
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()