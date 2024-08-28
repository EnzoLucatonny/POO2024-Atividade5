from data import Data
from autor import Autor
class Livro:
    def __init__(titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anoPublicacao(self):
        return self.__anoPublicacao

    def exibirLivro(self):
        print(f"titulo: {self.__titulo}")
        print(f"autor: {self.__autor}")
        print(self.__anoPublicacao.getData()) 