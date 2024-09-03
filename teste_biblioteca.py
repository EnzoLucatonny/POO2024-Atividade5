from livro import Livro
from autor import Autor
from biblioteca import Biblioteca

def adicionar_livro():
    titulo = input("Digite o titulo do livro: ")
    anoPublicacao = input("Digite o ano de publicação do livro: ")
    nome = input("Digite o nome do autor(a) do livro: ")
    nacionalidade = input("Digite a nacionalidade do autor(a) do livro: ")
    dataNascimento = input("Digite a data de nascimento do autor(a) do livro: ")
    autor = Autor(nome, nacionalidade, dataNascimento)
    livro = Livro(titulo, autor, anoPublicacao)
    return livro

def exibir_menu():
    print("\nMenu:")
    print("1) Adicionar Livro")
    print("2) Remover Livro")
    print("3) Busca Livro")
    print("4) Listar de Livros")
    print("5) SAIR ")

biblioteca = Biblioteca()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        livro = adicionar_livro()
        biblioteca.inserir_livro(livro)
        print("Livro adicionado com sucesso!")

    elif opcao == '2':
        nome = input("Digite o nome do livro que deseja buscar: ")
        livro = biblioteca.buscar_livro(nome)
        if livro:
            livro.exibirLivro()
        else:
            print("Livro não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do livro que deseja remover: ")
        if livro.remover_livro(nome):
            print("Livro removido com sucesso!")
        else:
            print("Livro não encontrado.")

    elif opcao == '4':
        biblioteca.listar_livro()

    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")




