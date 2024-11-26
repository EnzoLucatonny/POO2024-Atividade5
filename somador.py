from tkinter import *
janela = Tk()
janela.title("somador")
janela.geometry("200x100+100+100")

rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo3 = Label(janela, text="RESULTADO = ")
rotulo3.grid(row=3, column=0)

campo3 = Entry(janela)
campo3.grid(row=3, column=1)

def somar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    soma = v1+v2
    campo3.delete(0,END)
    campo3.insert(0, soma)
    campo3["state"] = "disabled"

botao = Button(janela)
botao.grid(row=2, column=1)
botao["width"] = 15
botao["text"] = "Somar"
botao["command"] = somar

def subtrair():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    subtracao = v1-v2
    campo3.delete(0,END)
    campo3.insert(0, subtracao)
    campo3["state"] = "disabled"

botao = Button(janela)
botao.grid(row=2, column=2)
botao["width"] = 25
botao["text"] = "Subtrair"
botao["command"] = subtrair

def multiplicar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    multiplicacao = v1*v2
    campo3.delete(0,END)
    campo3.insert(0, multiplicacao)
    campo3["state"] = "disabled"

botao = Button(janela)
botao.grid(row=2, column=3)
botao["width"] = 25
botao["text"] = "Multiplicar"
botao["command"] = multiplicar

def dividir():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    divisao = v1/v2
    campo3.delete(0,END)
    campo3.insert(0, divisao)
    campo3["state"] = "disabled"

botao = Button(janela)
botao.grid(row=2, column=4)
botao["width"] = 25
botao["text"] = "Dividir"
botao["command"] = dividir

janela.mainloop()