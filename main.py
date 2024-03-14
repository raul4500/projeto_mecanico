from classes import *

x = 0
while x==0 or x == 1:
    if x == 0:
        print("\nPrimeiramente, cadastre-se!\n")
        n = input("Digite o nome de usuário: ")
        s = input("Digite a senha: ")
        funcionario = Funcionario(n, s)
        x = 1
    elif x == 1:
        print("\nFaça login para acessar o programa!\n")
        n = input("Digite o nome de usuário: ")
        s = input("Digite a senha: ")
        if funcionario.verificarLogin(n, s) == True:
            print("Login realizado com sucesso.")
            x = 2
        else:
            print("Nome de usuário ou senha incorretos.")
        


print("\no que deseja fazer?\n")
sla = int(input("1 - cadastrar pedido\n\n2 - ver pedidos\n\n3 - sair\n\nDigite o numero da açao:"))
if sla == 1:
    n = input("nome do cliente:")
    c = input("cpf do cliente:")
    e = input("endereço do cliente:")
    t = input("telefone do cliente:")
                
    m = input("marca do carro:")
    a = input("ano do carro:") 
    p = input("placa do carro:")
    s = int(input("tipo de serviço:\n\n1 - Reparo automotivo\n\n2 - trocar óleo\n\n3 - Alinhamento e/ou balanceamento\n\n4 - Manutenção de embreagem\n\n5 - outro\n\n6 - sair\n\nNumero da açao:"))
                
    cliente = Cliente(n, c, e, t)
    pedido = Pedidos(m, a, p, s)
    
    print(cliente.mostrarCliente())
                
elif sla == 2:
    pass
elif sla == 3:
    pass
else:
    print("opçao inválida!")