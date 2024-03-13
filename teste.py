import tkinter as tk
from tkinter import messagebox
import csv

def verificar():
    usuario = username_entry.get()
    senha = password_entry.get()
    # Verificar se o nome de usuário e a senha correspondem aos armazenados no arquivo "users.dat"
    with open('usuarios.dat', 'r', newline='') as file:
                reader = csv.reader(file)
                for linha in reader:
                    if linha[0] == usuario and linha[1] == senha:
                        messagebox.showinfo("Login", "login sucedido")
                        return True
                    else:
                        messagebox.showerror("Login", "invalido")
                        return False

# Criar uma janela principal
janela = tk.Tk()
janela.geometry('300x300')
janela.title("Login")

# Criar os widgets
username_label = tk.Label(janela, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
username_entry = tk.Entry(janela)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(janela, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
password_entry = tk.Entry(janela, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(janela, text="Login", command=verificar)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)



janela.mainloop()