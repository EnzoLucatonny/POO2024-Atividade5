from Conta_Bancaria import Conta_Bancaria

class Conta_Corrente(Conta_Bancaria):
    def __init__(self, titular, cpf, saldo, numerocc):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f"{self.titular}, CPF {self.cpf}, saldo {self.saldo:.2f}, numero da conta {self.numerocc}"
    