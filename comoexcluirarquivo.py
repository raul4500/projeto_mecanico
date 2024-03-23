import os

with open(pedidos, 'r', newline='') as arquivo_leitura, open(caminho_arquivo_temp, 'w', newline='') as arquivo_escrita:
            leitor = csv.reader(arquivo_leitura)
            escritor = csv.writer(arquivo_escrita)  
            for indice_linha, linha in enumerate(leitor):
                if indice_linha != linha_para_excluir:
                    escritor.writerow(linha)
        os.replace(caminho_arquivo_temp, pedidos)