from tkinter import *
import tkinter as tk
from tkinter import messagebox
import csv

co0 = "#D9D9D9"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

file_name = 'usuarios.dat'

def janela1():
    def verificar():
        senha = senha_entry.get()
        # Verificar se o nome de usuário e a senha correspondem aos armazenados no arquivo "users.dat"
        with open('usuarios.dat', 'r', newline = '') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] == senha:
                    janela.destroy()  
                    janela2()     
                    return True
                else:
                    messagebox.showerror("Login", "invalido")
                    return False
    janela = tk.Tk()
    janela.geometry('260x270')
    janela.maxsize(width=260, height=270)
    janela.minsize(width=260, height=270)
    janela.title("Login")

    frame_cima = Frame(janela, width=310, height=70, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=310, height=230, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

    # Criar os widgets
    login = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Ivy 25", bg=co1)
    login.place(x=5, y=5)

    linha = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="#660101")
    linha.place(x=-2, y=45)

    senha = tk.Label(frame_baixo, text="senha:", bg=co1)
    senha.place(x=10, y=30)
    senha_entry = tk.Entry(frame_baixo, show="*", relief="flat", width=25)
    senha_entry.place(x=10, y=60)

    login = tk.Button(frame_baixo, text="enter", command=verificar, width=25, height=2, bg="#660101", relief="flat")
    login.place(x=10, y=120)

    janela.mainloop()

def janela3(): 
    def voltar():
        janela.destroy()
        janela2()       
    
    def avançar():
        janela.destroy()
        janela4()
        
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("INFO")
    
    frame_cima = Frame(janela, width=350, height=60, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_medio = Frame(janela, width=350, height=250, bg=co0, relief='flat')
    frame_medio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=350, height=200, bg=co0, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)
    
    titulo = tk.Label(frame_cima, text="Cadastrar Cliente", font="Arial 18", bg=co0)
    titulo.place(x=70, y=10)
       
    nome = tk.Label(frame_medio, text="nome:", bg=co0)
    nome.grid(row=0, column=1, sticky=NSEW)
    nome = tk.Entry(frame_medio, relief="flat", width=25)
    nome.grid(row=1, column=1, sticky=NSEW)
    
    
    cpf = tk.Label(frame_medio, text="cpf:", bg=co0)
    cpf.grid(row=2, column=1, sticky=NSEW)
    cpf = tk.Entry(frame_medio, relief="flat", width=25)
    cpf.grid(row=3, column=1, sticky=NSEW)
    
    endereço = tk.Label(frame_medio, text="endereço:", bg=co0)
    endereço.grid(row=4, column=1, sticky=NSEW)
    endereço = tk.Entry(frame_medio, relief="flat", width=25)
    endereço.grid(row=5, column=1, sticky=NSEW)
    
    telefone = tk.Label(frame_medio, text="telefone:", bg=co0)
    telefone.grid(row=6, column=1, sticky=NSEW)
    telefone = tk.Entry(frame_medio, relief="flat", width=25)
    telefone.grid(row=7, column=1, sticky=NSEW)

    sair = tk.Button(frame_baixo, text="Voltar", command = voltar, width=13, height=2, bg="#951C1C", relief="flat")
    sair.place(x=20, y=60)
    
    proximo = tk.Button(frame_baixo, text="Próximo", command = avançar, width=13, height=2, bg="#951C1C", relief="flat")
    proximo.place(x=220, y=60)
    
    janela.mainloop()

def janela2():
    def sair():
        janela.destroy()
    def criarPedido():
        janela.destroy()
        janela3()
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("INFO")

    ccliente = tk.Button( text="Criar Pedido", width=33, command=criarPedido, height=3, bg="orange", relief="flat")
    ccliente.place(x=50, y=10)

    cpedido = tk.Button( text="Ver Pedidos", width=33, height=3, bg="orange", relief="flat")
    cpedido.place(x=50, y=100)

    sair = tk.Button( text="Sair",command = sair, width=20, height=2, bg="red", relief="flat")
    sair.place(x=100, y=200)

def janela4():
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("INFO")
print("hello")
janela3()
