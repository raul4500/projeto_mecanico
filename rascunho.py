from classes import *
import csv

file_name = 'clientes.dat'
file = 'pedidos.dat'

def cadastrar_cliente(n, c, e, t):
    with open('clientes.dat', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([n, c, e, t])
    print("cliente cadastrado com sucesso.")

def cadastrar_pedido(m, a, p, s):
    with open('pedidos.dat', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([m, a, p, s])
    print("pedido cadastrado com sucesso.")

def main():
    while True:
        sla = int(input("1 - cadastrar pedido\n\n2 - ver pedidos\n\n3 - sair\n\nDigite o numero da açao:"))
        if sla == 1:
                n = input("nome do cliente:")
                c = input("cpf do cliente:")
                e = input("endereço do cliente:")
                t = input("telefone do cliente:")
                
                m = input("marca do carro:")
                a = input("ano do carro:")
                p = input("placa do carro:")
                s = input("tipo de serviço:\n\n1 - Reparo automotivo\n\n2 - trocar óleo\n\n3 - Alinhamento e/ou balanceamento\n\n4 - Manutenção de embreagem\n\n5 - outro\n\n6 - sair\n\nNumero da açao:")
                
                cadastrar_cliente(n, c, e, t)
                cadastrar_pedido(m, a, p, s)
                
        elif sla == 2:
                break
        elif sla == 3:
                break
        else:
                print("opçao inválida!")
if __name__ == "__main__":
    main()