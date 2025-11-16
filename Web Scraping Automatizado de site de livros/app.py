# //Raspagem da web
# //Vou extrair dados de sites automaticamente

# Passos:
""" 1.Rastreamento - Acesso do site via link
    2.Extração - Extração dos dados desejados do codigo html da pág.
    3.Armazenamento - Os dados são armazenados uma planilha, banco de dados ou arquivo CSV
"""
# Bibliotecas necessarias
import requests as rs  # Rquisição
from bs4 import BeautifulSoup as bs  # Rapasgem simples
import pandas as pd  # planilha e salvamento
import os  # gerenciamento de arquivo
import sys  # determina se o .exe ou .py esta rodando
import tkinter as tk  # interface
from tkinter import messagebox  # avisa que tudo ocorreu bem (caixa de aviso)

# Função para descobrir a pasta correta (mesma do .exe ou .py)


def get_base_path():
    if getattr(sys, 'frozen', False):
        # Quando empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Quando rodando como script Python
        return os.path.dirname(os.path.abspath(__file__))

# Função principal de scraping


def rodar_scraping():
    livros = []

    for pag in range(1, 51):
        if pag == 1:
            url = "https://books.toscrape.com/"
        else:
            url = f"https://books.toscrape.com/catalogue/page-{pag}.html"

        # Requisição
        response = rs.get(url)
        site = bs(response.text, 'html.parser')

        # Extração
        titulos = site.find_all('h3')
        precos = site.find_all(class_="price_color")
        disp = site.find_all(class_="instock availability")

        # Estrutura
        for t, p, d in zip(titulos, precos, disp):
            nome = t.a['title']
            preco = p.text
            disponibilidade = d.text.strip()
            livros.append([nome, preco, disponibilidade])

    # Criando DataFrame
    df = pd.DataFrame(livros, columns=['Titulo', 'Preço', 'Disponibilidade'])

    # Caminho de saída (mesma pasta do executável/script)
    pasta = get_base_path()
    arquivo_csv = os.path.join(pasta, "Tabela_de_livros.csv")

    # Salvando CSV
    df.to_csv(arquivo_csv, index=False, encoding="utf-8-sig")

    # Mensagem de sucesso
    messagebox.showinfo("Concluído", f"Arquivo salvo em:\n{arquivo_csv}")


# Interface Tkinter
janela = tk.Tk()
janela.title("Raspador de Livros")
janela.geometry("300x150")

botao = tk.Button(janela, text="Rodar Scraping", command=rodar_scraping,
                  font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
botao.pack(expand=True)

janela.mainloop()
