from tkinter import *
import tkinter as tk
from tkinter import messagebox
import csv

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

file_name = 'usuarios.dat'
def janela3():
        janela = tk.Tk()
        janela.geometry('260x270')
        janela.maxsize(width=260, height=270)
        janela.minsize(width=260, height=270)
        janela.title("Senha ADM")

        frame_cima = Frame(janela, width=310, height=70, bg=co1, relief='flat')
        frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)
        frame_baixo = Frame(janela, width=310, height=230, bg=co1, relief='flat')
        frame_baixo.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

        # Criar os widgets
        login_label = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Ivy 25", bg=co1)
        login_label.place(x=5, y=5)

        linha_label = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="#660101")
        linha_label.place(x=-2, y=45)

        senha_label = tk.Label(frame_baixo, text="Senha:", bg=co1)
        senha_label.place(x=10, y=30)
        senha_entry = tk.Entry(frame_baixo, show="*", relief="solid", width=25)
        senha_entry.place(x=10, y=60)

        login_button = tk.Button(frame_baixo, text="", command=verificar, width=25, height=2, bg="#660101", relief="solid")
        login_button.place(x=10, y=120)  

def sla():
    janela.destroy()
    janela3()

def novaJanela():
    janela = tk.Tk()
    janela.geometry('350x350')
    janela.title("INFO")

    ccliente_button = tk.Button( text="Criar Pedido", width=33, height=3, bg="orange", relief="solid")
    ccliente_button.place(x=10, y=10)

    cpedido_button = tk.Button( text="Ver Pedidos", command=sla, width=33, height=3, bg="orange", relief="solid")
    cpedido_button.place(x=10, y=100)

    sair_button = tk.Button( text="Sair", width=20, height=2, bg="red", relief="solid")
    sair_button.place(x=60, y=200)
   
def verificar():
    senha = senha_entry.get()
    # Verificar se o nome de usuário e a senha correspondem aos armazenados no arquivo "users.dat"
    with open('usuarios.dat', 'r', newline = '') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == senha:
                janela.destroy()  
                novaJanela()     
                return True
            else:
                messagebox.showerror("Login", "invalido")
                return False
                    
    

# Criar uma janela principal

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
login_label = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Ivy 25", bg=co1)
login_label.place(x=5, y=5)

linha_label = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="#660101")
linha_label.place(x=-2, y=45)

senha_label = tk.Label(frame_baixo, text="Senha:", bg=co1)
senha_label.place(x=10, y=30)
senha_entry = tk.Entry(frame_baixo, show="*", relief="solid", width=25)
senha_entry.place(x=10, y=60)

login_button = tk.Button(frame_baixo, text="enter", command=verificar, width=25, height=2, bg="#660101", relief="solid")
login_button.place(x=10, y=120)

janela.mainloop()
