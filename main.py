import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def abrir_arquivo():
    global linhas_contendo_kijo
    numero = entrada_numero_label.get()
    
    if not numero:
        messagebox.showerror("Erro", "Insira o número de frota antes de impoortar o arquivo.")
        return

    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if arquivo:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()

        linhas_contendo_kijo = [linha for linha in linhas if f"KIJO120,02,{numero}" in linha]

        if linhas_contendo_kijo:
            texto_caixa.delete(1.0, tk.END)
            for linha in linhas_contendo_kijo:
                # Remover a parte "Rx  2023-09-28 09:05:35 [177.26.206.56:63874 100002]" da linha
                linha_limpa = linha.split("] ", 1)[-1]
                texto_caixa.insert(tk.END, linha_limpa)

def salvar_arquivo():
    global linhas_contendo_kijo
    if linhas_contendo_kijo:
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])

        if arquivo:
            linhas_limpas = [linha.split("] ", 1)[-1] for linha in linhas_contendo_kijo]
            with open(arquivo, 'w') as file:
                file.writelines(linhas_limpas)
                messagebox.showinfo(f"Sucesso", "Os KIJOS do HoverBee {entrada_numero_label} foram filtrados com sucesso!")

janela = tk.Tk()
janela.title("HoverBee Converter V1.0.0.0'")
janela.geometry("800x600")
janela.resizable(False, False)

logo = Image.open("quitoDev.png")  # Substitua "logo.png" pelo caminho do seu arquivo de imagem
q = Label(janela, text="A quitoDev Development", width=40,height=0, font=('Times New Roman', 15, 'bold'))
d = Label(janela, text="Grãos - P&D - Soluções Radical", width=40,height=0, font=('Times New Roman', 10))
largura, altura = 120, 120  # Dimensões desejadas
logo = logo.resize((largura, altura))  # Redimensiona com suavização
q.pack()

# Carrega a imagem redimensionada em tk.PhotoImage
logo = ImageTk.PhotoImage(logo)
d.pack()

# Adiciona o logotipo à janela
logo_label = tk.Label(janela, image=logo)
logo_label.pack(pady=10)

entrada_numero_label = tk.Label(janela, text="Numero de Frota:")
entrada_numero_label.pack()
entrada_numero_label = tk.Entry(janela)
entrada_numero_label.pack()

botao_abrir = tk.Button(janela, text="Importar KIJO LOG", command=abrir_arquivo)
botao_abrir.pack(pady=10)

botao_salvar = tk.Button(janela, text="Salvar", command=salvar_arquivo)
botao_salvar.pack(pady=10)

texto_caixa = tk.Text(janela, wrap=tk.WORD, width=80, height=15)
texto_caixa.pack()

janela.mainloop()
