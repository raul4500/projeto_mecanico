class Adm:
    def __init__(self, senha):
        self.__senha = senha

class Funcionario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha   
        
    def verificarLogin(self, n, s):
        if n == self.nome and s == self.senha:
            return True
        else:
            return False

class Cliente:
    def __init__(self, nome, cpf, endereço, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereço = endereço
        self.telefone = telefone
    
    def mostrarCliente(self):
        return [self.nome,self.cpf,self.endereço,self.telefone]
        
class Pedidos:
    def __init__(self, m, a, p, s):
        self.marca = m
        self.ano = a
        self.placa = p
        self.serviço = s
    
    def mostrarPedido(self):
        return [self.marca,self.ano,self.placa,self.serviço]
       