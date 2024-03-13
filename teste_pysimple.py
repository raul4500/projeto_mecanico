import PySimpleGUI as sg
import csv
layout = [
    [sg.Text('Usuário'), sg.Button('teste')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario = values['usuario']
        senha = values['senha']
        
        file_name = 'usuarios.dat'

        def verificar_login(usuario, senha):
            with open('usuarios.dat', 'r', newline='') as file:
                reader = csv.reader(file)
                for linha in reader:
                    if linha[0] == usuario and linha[1] == senha:
                        return True
                return False
            
        if verificar_login(usuario, senha) == True:
            window['mensagem'].update('login feito com sucesso')
            
        else:
            window['mensagem'].update('houve um erro')
        
        if verificar_login(usuario, senha) == True:
            window.close()
            name = sg.popup_get_text('What is your name?')   
    