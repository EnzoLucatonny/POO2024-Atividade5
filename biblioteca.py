from livro import Livro
from autor import Autor

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def inserir_livro(self, livro):
        self.__livros.append(livro)


    def buscar_livro(self, nome):
        for livro in self.__livros:
            if livro.get_nome().lower() == nome.lower():
                return livro
        return None

    def remover_livro(self, nome):
        livro = self.buscar_livro(nome)
        if livro:
            self.__livros.remove(livro)
            return True
        return False

    def listar_livro(self):
        if not self.__livros:
            print("Biblioteca vazia.")
        else:
            for livro in self.__livros:
                livro.exibirLivro()