from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os

co0 = "#D9D9D9" 
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

senhas = 'senhas.dat'
admin = 'admin.dat'
pedidos = 'pedidos.dat'
temp = 'temp.dat'

def janela1():
    with open(temp, 'w'):
        pass
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
    login = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Arial 25", bg=co0)
    login.place(x=80, y=5)

    senha = tk.Label(frame_baixo, text="senha:", bg=co0)
    senha.place(x=110, y=20)
    senha_entry = tk.Entry(frame_baixo, show="*", relief="flat", width=25)
    senha_entry.place(x=53, y=50)

    login = tk.Button(frame_baixo, text="enter",fg=co1, command=verificar, width=25, height=2, bg="#660101", relief="flat")
    login.place(x=37, y=140)

    janela.mainloop()
    
def janela2():
    with open(temp, 'w'):
        pass
    def sair():
        janela.destroy()
    def criarPedido():
        janela.destroy()
        janela3()
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("HOME")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)
    
    def verPedidos():
        janela.destroy()
        janela6()
    
    frame = Frame(janela, width=350, height=350, bg=co0, relief='flat')
    frame.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)

    ccliente = tk.Button(frame, text="Criar Pedido", width=33, fg=co1, command=criarPedido, height=3, bg="#951C1C", relief="flat")
    ccliente.place(x=50, y=50)

    cpedido = tk.Button(frame, text="Ver Pedidos", width=33,fg=co1, command=verPedidos, height=3, bg="#951C1C", relief="flat")
    cpedido.place(x=50, y=140)

    sair1 = tk.Button(frame, text="Sair",command = sair,fg=co1, width=20, height=2, bg="#660101", relief="flat")
    sair1.place(x=93, y=240)
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
        
        with open(temp, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([n,c,e,t])
                
        janela.destroy()
        janela4()
        return [n,c,e,t]

    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)

    
    frame_cima = Frame(janela, width=350, height=60, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_medio = Frame(janela, width=350, height=220, bg=co0, relief='flat')
    frame_medio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=350, height=200, bg=co0, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)
    
    titulo = tk.Label(frame_cima, text="Cadastrar Cliente", font="Arial 18", bg=co0)
    titulo.place(x=70, y=10)
       
    
    nome = tk.Label(frame_medio, text="nome:", bg=co0)
    nome.place(x=20,y=0)
    nome_entry = tk.Entry(frame_medio, relief="flat", width=50)
    nome_entry.place(x=20,y=20)
    
    
    cpf = tk.Label(frame_medio, text="cpf:", bg=co0)
    cpf.place(x=20,y=50)
    cpf_entry = tk.Entry(frame_medio, relief="flat", width=50)
    cpf_entry.place(x=20,y=70)
    
    endereço = tk.Label(frame_medio, text="endereço:", bg=co0)
    endereço.place(x=20,y=100)
    endereço_entry = tk.Entry(frame_medio, relief="flat", width=50)
    endereço_entry.place(x=20,y=120)
    
    telefone = tk.Label(frame_medio, text="telefone:", bg=co0)
    telefone.place(x=20,y=150)
    telefone_entry = tk.Entry(frame_medio, relief="flat", width=50)
    telefone_entry.place(x=20,y=170)

    sair = tk.Button(frame_baixo, text="Cancelar",fg=co1, command = voltar, width=13, height=2, bg="#951C1C", relief="flat")
    sair.place(x=20, y=0)
    
    proximo = tk.Button(frame_baixo, text="Próximo",fg=co1, command = verificar, width=13, height=2, bg="#951C1C", relief="flat")
    proximo.place(x=220, y=0)
    
    janela.mainloop()

def janela4():
    def voltar():
        janela.destroy()
        janela2()       
                   
    def verificar():
        m = marca_entry.get()
        a = ano_entry.get()
        p = placa_entry.get()
        d = descricao_entry.get()
        d1 = descricao1_entry.get()
        d2 = descricao2_entry.get()
        
        with open(temp, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([m,a,p,d,d1,d2])
            writer.writerow(['----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'])
        with open(temp, 'r', newline = '') as file:
            reader = csv.reader(file)
            for linha in reader:
                print(linha)
        
        janela.destroy()
        janela5()
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("")
    janela.maxsize(width=350, height=350)
    janela.minsize(width=350, height=350)

    
    frame_cima = Frame(janela, width=350, height=60, bg=co0, relief='flat')
    frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
    frame_medio = Frame(janela, width=350, height=220, bg=co0, relief='flat')
    frame_medio.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=350, height=200, bg=co0, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)
    
    titulo = tk.Label(frame_cima, text="Cadastrar Pedido", font="Arial 18", bg=co0)
    titulo.place(x=70, y=10)
       
    marca = tk.Label(frame_medio, text="marca:", bg=co0)
    marca.place(x=15,y=0)
    marca_entry = tk.Entry(frame_medio, relief="flat", width=25)
    marca_entry.place(x=15,y=20)
    
    
    ano = tk.Label(frame_medio, text="ano:", bg=co0)
    ano.place(x=15,y=50)
    ano_entry = tk.Entry(frame_medio, relief="flat", width=25)
    ano_entry.place(x=15,y=70)
    
    placa = tk.Label(frame_medio, text="placa:", bg=co0)
    placa.place(x=15,y=100)
    placa_entry = tk.Entry(frame_medio, relief="flat", width=25)
    placa_entry.place(x=15,y=120)
    
    descricao = tk.Label(frame_medio, text="tipo(s) de serviço(s):", bg=co0)
    descricao.place(x=180, y=0)
    descricao_entry = tk.Entry(frame_medio, relief="flat", width=25)
    descricao_entry.place(x=180, y=20)
    descricao1_entry = tk.Entry(frame_medio, relief="flat", width=25)
    descricao1_entry.place(x=180, y=40)
    descricao2_entry = tk.Entry(frame_medio, relief="flat", width=25)
    descricao2_entry.place(x=180, y=60)

    sair = tk.Button(frame_baixo, text="Cancelar", command = voltar, width=13, height=2, fg=co1, bg="#951C1C", relief="flat")
    sair.place(x=20, y=0)
    
    proximo = tk.Button(frame_baixo, text="Próximo", command = verificar, width=13, height=2, fg=co1, bg="#951C1C", relief="flat")
    proximo.place(x=220, y=0)
    
    janela.mainloop()
    
def janela5():
    def voltar():
        janela.destroy()
        janela4()    
        
    def verificar():
        s = senha_entry.get()
        u = usuario_entry.get()
        
        with open(admin, 'r', newline = '') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[1] == s and linha[0] == u:
                    with open(temp, 'r', newline='') as file:
                        reader = csv.reader(file)
                        for linha in reader:
                            with open(pedidos, 'a', newline = '') as file:
                                writer = csv.writer(file)
                                writer.writerow(linha)
                    
                            
                            
                    messagebox.showinfo("permissao", "Pedido cadastrado!")
                    janela.destroy()
                    janela2()
                else:
                    messagebox.showerror("permissao", "invalido")
                    
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
    login = tk.Label(frame_cima, anchor=NE, text="PERMISSÃO DO ADMIN", font="Ivy 15", bg=co0)
    login.place(x=15, y=10)

    linha = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="#660101")
    linha.place(x=-2, y=45)
    
    usuario = tk.Label(frame_baixo, text="usuario:", bg=co0)
    usuario.place(x=110, y=0)
    usuario_entry = tk.Entry(frame_baixo, relief="flat", width=25)
    usuario_entry.place(x=50, y=30)

    senha = tk.Label(frame_baixo, text="senha:", bg=co0)
    senha.place(x=110, y=60)
    senha_entry = tk.Entry(frame_baixo, show="*", relief="flat", width=25)
    senha_entry.place(x=50, y=90)

    login = tk.Button(frame_baixo, text="Finalizar",fg=co1, command=verificar, width=13, height=2, bg="#660101", relief="flat")
    login.place(x=130, y=140)
    
    sair = tk.Button(frame_baixo, text="Cancelar", command = voltar, width=13, height=2, fg=co1, bg="#951C1C", relief="flat")
    sair.place(x=20, y=140)

    janela.mainloop()
   
def janela6(): 
    def recarregar():
        janela.destroy()
        janela6()    
    def voltar():
        janela.destroy()
        janela2()    
        
    def imprimir_lista_em_linhas():
        with open(pedidos, 'r', newline='') as file:
            reader = csv.reader(file)
            text = tk.Text(frame_medio, wrap="none", bg="#660101", fg=co1)
            text.pack(fill="both", expand=True)
            scrollbar = tk.Scrollbar(frame_medio, orient="vertical", command=text.yview)
            scrollbar.pack(side="right", fill="y")
            text.configure(yscrollcommand=scrollbar.set)
            for linha in reader:
                linha_formatada = ','.join(linha)
                text.insert("end", f"{linha_formatada}\n")

    janela = tk.Tk()
    janela.geometry('650x350')
    janela.title("")
    janela.maxsize(width=650, height=350)
    janela.minsize(width=650, height=350)

    frame_medio = Frame(janela, width=280, height=300, bg="#660101", relief='flat')
    frame_medio.place(x=0,y=0)
    frame_medio.pack(fill='both', expand=True)
    frame_baixo = Frame(janela, width=650, height=200, bg=co0, relief='flat')
    frame_baixo.place(x=0,y=270)
        
    titulo = tk.Label(frame_baixo, text="PEDIDOS", font="Arial 18", bg=co0)
    titulo.place(x=250, y=20)
       
    sair = tk.Button(frame_baixo, text="Voltar",fg=co1, command = voltar, width=13, height=2, bg="#951C1C", relief="flat")
    sair.place(x=30, y=15)
    
    recarregar = tk.Button(frame_baixo, text="Recarregar",fg=co1, command = recarregar, width=13, height=2, bg="#951C1C", relief="flat")
    recarregar.place(x=520, y=15)
    
    imprimir_lista_em_linhas()
    
    janela.mainloop()
    
janela1()