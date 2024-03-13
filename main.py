from tkinter import *
import tkinter as tk
from tkinter import messagebox
import csv

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

def novaJanela():
        login_label = tk.Label(frame_cima, anchor=NE, text="BEM-VINDO", font="Ivy 25", bg=co1)
        login_label.place(x=5, y=5)

def verificar():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    # Verificar se o nome de usuário e a senha correspondem aos armazenados no arquivo "users.dat"
    with open('usuarios.dat', 'r', newline='') as file:
                reader = csv.reader(file)
                for linha in reader:
                    if linha[0] == usuario and linha[1] == senha:
                        messagebox.showinfo("Login", "login sucedido")
                        #apaga oque estiver na janela
                        for widget in frame_baixo.winfo_children():
                            widget.destroy()
                        for widget in frame_cima.winfo_children():
                            widget.destroy()    
                        
                        novaJanela()
                        
                        return True
                    else:
                        messagebox.showerror("Login", "invalido")
                        return False
                    
    

# Criar uma janela principal
janela = tk.Tk()
janela.geometry('260x270')
janela.title("Login")

frame_cima = Frame(janela, width=310, height=70, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=1, pady=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=230, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=1, pady=0, sticky=NSEW)

# Criar os widgets
login_label = tk.Label(frame_cima, anchor=NE, text="LOGIN", font="Ivy 25", bg=co1)
login_label.place(x=5, y=5)

linha_label = tk.Label(frame_cima, width=275, text="", font="Ivy 1", bg="green")
linha_label.place(x=-2, y=45)

usuario_label = tk.Label(frame_baixo, text="Usuário:", bg=co1)
usuario_label.place(x=10, y=0)
usuario_entry = tk.Entry(frame_baixo, relief="solid", width=39)
usuario_entry.place(x=10, y=30)

senha_label = tk.Label(frame_baixo, text="Senha:", bg=co1)
senha_label.place(x=10, y=60)
senha_entry = tk.Entry(frame_baixo, show="*", relief="solid", width=39)
senha_entry.place(x=10, y=90)

login_button = tk.Button(frame_baixo, text="Login", command=verificar, width=33, height=3, bg="green", relief="solid")
login_button.place(x=10, y=120)



janela.mainloop()