from tkinter import *
from tkinter import messagebox
janela = Tk()
janela.title("Boas vindas")
janela.geometry("300x200+100+100")

rotulo = Label(janela, text="Qual o seu nome? ")
rotulo.grid(row=0, column=0)

campo = Entry(janela)
campo.grid(row=0, column=1)

def boasvindas():
    nome = campo.get()
    msg = f"Seja bem vindas(a), {nome}!"
    messagebox.showinfo(message=nome)

botao = Button(janela)
botao.grid(row=1, column=0)
botao["text"] = "Enviar"
botao["command"] = boasvindas

janela.mainloop()
