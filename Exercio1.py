from distutils.cmd import Command
from select import select
from tkinter import *
from tracemalloc import start
from Biblioteca import *

janela = Tk()

rotulo = Label(janela, text="BLACK MESA BLUE SHIFT")
rotulo.grid(row=0, column=0)

botao_continuar = Button(janela)
botao_continuar.grid(row=1, column=0)
botao_continuar["text"] = "Continuar"
botao_continuar["width"] = 10
botao_continuar["command"] = start

botao_capitulos = Button(janela)
botao_capitulos.grid(row=2, column=0)
botao_capitulos["text"] = "Capitulos"
botao_capitulos["width"] = 10
botao_capitulos["command"] = select

botao_opcao = Button(janela)
botao_opcao.grid(row=3, column=0)
botao_opcao["text"] = "Opções"
botao_opcao["width"] = 10
botao_opcao["command"] = select

botao_sair = Button(janela)
botao_sair.grid(row=4, column=0)
botao_sair["text"] = "Sair"
botao_sair["width"] = 10
botao_sair["command"] = quit

janela.mainloop()