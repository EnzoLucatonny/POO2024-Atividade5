from tkinter import *
janela = Tk()

info = "Esse texto será\nexibido \nem várias linhas."

rotulo = Label(janela, text= info, justify= "left")
rotulo.grid(row=0, column=0)

info2 = """Assim também 
é possivel 
ter várias linhas."""

rotulo2 = Label(janela, text= info, justify= "right")
rotulo2.grid(row=2, column=0)


botao_sair = Button(janela)
botao_sair.grid(row=1, column=0)
botao_sair["text"] = "sair"
botao_sair["width"] = 10
botao_sair["command"] = quit

janela.mainloop()
