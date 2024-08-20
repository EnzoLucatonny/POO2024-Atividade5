from Conta_Bancaria import Conta_Bancaria

class Conta_Poupança(Conta_Bancaria):
    def __init__(self, rendimento, titular, cpf, saldo):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_redinmento(self):
        print (self.rendimento * self.saldo)

    def render(self):
        return self.saldo + self.saldo * self.rendimento