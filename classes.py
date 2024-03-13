class Adm:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

class Funcionario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha        

class Cliente:
    def __init__(self, nome, cpf, endereço, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereço = endereço
        self.telefone = telefone
    
    def mostrar(self):
        print(self.nome)
        
class Pedidos:
    def __init__(self, m, a, p, s):
        self.marca = m
        self.ano = a
        self.placa = p
        self.serviço = s
        