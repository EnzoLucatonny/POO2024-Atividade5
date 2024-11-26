from tkinter import *

janela = Tk()
janela.geometry("400x300")
janela.title("POO - 2V")
#janela.resizable(FALSE, FALSE)
janela.minsize(300, 200)
janela.maxsize(800,600)

rotulo = Label(janela, text="Olá Mundo")
rotulo.grid(row=0, column=0)

nome = Label(janela, text="Enzo")
nome.grid(row=1, column=0)

botão_sair = Button(janela)
botão_sair.grid(row=2, column=0)
