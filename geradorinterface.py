import segno # biblioteca de gerar qr 
import tkinter as tk #biblioteca de interface 
from tkinter import filedialog #biblioteca de salvar arquivos 
 
def gerar_qr():
    url = entry.get() #captura a url digitada
    if url: #verifiac se tem algo escrito 
        qr = segno.make(url) ##gera o qr de acordo com a url
        arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])  #abre uma guia para o usuario esccolher onde sera salvo o qr no formato png
        if arquivo: #verifica se o usuario escoheu um local para ssalvar 
            qr.save(arquivo, scale=15) #salva o arqivo vom o tamnho definido 
            label_status.config(text="QR Code salvo com sucesso!")
    else: #caso o url seja invalido ou nao tenha nada desccrito elw exibe um aviso 
        label_status.config(text="Digite um URL válido.")

# interface do bagulho 
janela = tk.Tk() #cria a janela 
janela.title("Gerador de QR Code") #define o titulo

tk.Label(janela, text="Digite o URL:").pack(pady=10)
entry = tk.Entry(janela, width=100)
entry.pack(pady=5) #add um espaçamento vertical

btn_gerar = tk.Button(janela, text="Gerar QR Code", command=gerar_qr)
btn_gerar.pack(pady=10)

label_status = tk.Label(janela, text="")
label_status.pack(pady=5)

janela.mainloop() #cria um loop da janela para permanecer aberta ate que o usuario a feche
