from tkinter import *
import tkinter as tk
from tkinter import messagebox
import csv

co0 = "#D9D9D9"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

senhas = 'senhas.dat'

def janela1():
    def verificar():
        senha = senha_entry.get()
        # Verificar se o nome de usuário e a senha correspondem aos armazenados no arquivo "users.dat"
        with open(senhas, 'r', newline = '') as file:
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

    frame_cima = Frame(janela, width=310, height=70, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=310, height=230, bg=co0, relief='flat')
    frame_baixo.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

    # Criar os widgets
    login = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Ivy 25", bg=co0)
    login.place(x=5, y=5)

    linha = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="#660101")
    linha.place(x=-2, y=45)

    senha = tk.Label(frame_baixo, text="senha:", bg=co0)
    senha.place(x=10, y=30)
    senha_entry = tk.Entry(frame_baixo, show="*", relief="flat", width=25)
    senha_entry.place(x=10, y=60)

    login = tk.Button(frame_baixo, text="enter",fg=co1, command=verificar, width=25, height=2, bg="#660101", relief="flat")
    login.place(x=10, y=120)

    janela.mainloop()
    
def janela2():
    def sair():
        janela.destroy()
    def criarPedido():
        janela.destroy()
        janela3()
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("HOME")
    janela.winfo_rgb(co0)

    ccliente = tk.Button(text="Criar Pedido", width=33,fg=co1, command=criarPedido, height=3, bg="orange", relief="flat")
    ccliente.place(x=50, y=50)

    cpedido = tk.Button(text="Ver Pedidos", width=33,fg=co1, height=3, bg="orange", relief="flat")
    cpedido.place(x=50, y=140)

    sair1 = tk.Button(text="Sair",command = sair,fg=co1, width=20, height=2, bg="red", relief="flat")
    sair1.place(x=100, y=240)
    janela.mainloop()
    
def janela3(): 
    def voltar():
        janela.destroy()
        janela2()       
    
    def verificar():
        n = nome_entry.get()
        c = cpf_entry.get()
        e = endereço_entry.get()
        t = telefone_entry.get()
        
        
        janela.destroy()
        janela4()
        
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)

    
    frame_cima = Frame(janela, width=350, height=60, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_medio = Frame(janela, width=350, height=250, bg=co0, relief='flat')
    frame_medio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=350, height=200, bg=co0, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)
    
    titulo = tk.Label(frame_cima, text="Cadastrar Cliente", font="Arial 18", bg=co0)
    titulo.place(x=70, y=10)
       
    
    nome = tk.Label(frame_medio, text="nome:", bg=co0)
    nome.grid(row=0, column=2, sticky=NSEW)
    nome_entry = tk.Entry(frame_medio, relief="flat", width=25)
    nome_entry.grid(row=1, column=2, sticky=NSEW)
    
    
    cpf = tk.Label(frame_medio, text="cpf:", bg=co0)
    cpf.grid(row=2, column=1, sticky=NSEW)
    cpf_entry = tk.Entry(frame_medio, relief="flat", width=25)
    cpf_entry.grid(row=3, column=1, sticky=NSEW)
    
    endereço = tk.Label(frame_medio, text="endereço:", bg=co0)
    endereço.grid(row=4, column=1, sticky=NSEW)
    endereço_entry = tk.Entry(frame_medio, relief="flat", width=25)
    endereço_entry.grid(row=5, column=1, sticky=NSEW)
    
    telefone = tk.Label(frame_medio, text="telefone:", bg=co0)
    telefone.grid(row=6, column=1, sticky=NSEW)
    telefone_entry = tk.Entry(frame_medio, relief="flat", width=25)
    telefone_entry.grid(row=7, column=1, sticky=NSEW)

    sair = tk.Button(frame_baixo, text="Voltar",fg=co1, command = voltar, width=13, height=2, bg="#951C1C", relief="flat")
    sair.place(x=20, y=60)
    
    proximo = tk.Button(frame_baixo, text="Próximo",fg=co1, command = verificar, width=13, height=2, bg="#951C1C", relief="flat")
    proximo.place(x=220, y=60)
    
    janela.mainloop()

def janela4():
    def voltar():
        janela.destroy()
        janela3()       
    
    def verificar():
        m = marca_entry.get()
        a = ano_entry.get()
        p = placa_entry.get()
        d = descricao_entry.get()
         
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)

    
    frame_cima = Frame(janela, width=350, height=60, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_medio = Frame(janela, width=350, height=250, bg=co0, relief='flat')
    frame_medio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=350, height=200, bg=co0, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)
    
    titulo = tk.Label(frame_cima, text="Cadastrar Pedido", font="Arial 18", bg=co0)
    titulo.place(x=70, y=10)
       
    marca = tk.Label(frame_medio, text="marca:", bg=co0)
    marca.grid(row=0, column=1, sticky=NSEW)
    marca_entry = tk.Entry(frame_medio, relief="flat", width=25)
    marca_entry.grid(row=1, column=1, sticky=NSEW)
    
    
    ano = tk.Label(frame_medio, text="ano:", bg=co0)
    ano.grid(row=2, column=1, sticky=NSEW)
    ano_entry = tk.Entry(frame_medio, relief="flat", width=25)
    ano_entry.grid(row=3, column=1, sticky=NSEW)
    
    placa = tk.Label(frame_medio, text="placa:", bg=co0)
    placa.grid(row=4, column=1, sticky=NSEW)
    placa_entry = tk.Entry(frame_medio, relief="flat", width=25)
    placa_entry.grid(row=5, column=1, sticky=NSEW)
    
    descricao = tk.Label(frame_medio, text="descrição do pedido:", bg=co0)
    descricao.place(x=180, y=0)
    descricao_entry = tk.Entry(frame_medio, relief="flat", width=25)
    descricao_entry.place(x=180, y=20)

    sair = tk.Button(frame_baixo, text="Voltar", command = voltar, width=13, height=2, fg=co1, bg="#951C1C", relief="flat")
    sair.place(x=20, y=60)
    
    proximo = tk.Button(frame_baixo, text="Próximo", command = avançar, width=13, height=2, fg=co1, bg="#951C1C", relief="flat")
    proximo.place(x=220, y=60)
    
    janela.mainloop()
    
def janela5():
    def voltar():
        janela.destroy()
        janela3()       
    
    def avançar():
        janela.destroy()
        janela2()
        
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)
    
janela3()