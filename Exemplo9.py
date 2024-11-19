from tkinter import *
janela = Tk()

info2 = """Assim também 
é possivel 
ter várias linhas."""

rotulo2 = Label(janela, text= info2, justify= "right")
rotulo2.grid(row=2, column=0)

logo = PhotoImage(file="")
rotulo2 = Label(janela, image= logo)
rotulo2.grid(row=0, column=1)

botao_sair = Button(janela)
botao_sair.grid(row=1, column=0)
botao_sair["text"] = "sair"
botao_sair["width"] = 10
botao_sair["command"] = quit

janela.mainloop()
