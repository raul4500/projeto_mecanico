import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Criar um widget Text
text = tk.Text(root, wrap="none")
text.pack(fill="both", expand=True)

# Adicionar uma scrollbar vertical
scrollbar = tk.Scrollbar(root, orient="vertical", command=text.yview)
scrollbar.pack(side="right", fill="y")

# Configurar a scrollbar para rolar o Text
text.configure(yscrollcommand=scrollbar.set)

# Adicionar conteúdo ao Text
for i in range(50):
    text.insert("end", f"Label {i}\n")

root.mainloop()