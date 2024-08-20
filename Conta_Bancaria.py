class Conta_Bancaria:
    def __init__(self, titular, cpf, saldo):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
    
    def mostrar_conta(self):
        return f"{self.titular}, CPF {self.cpf}, saldo {self.saldo:.2f}"
    
    def depositar(self, saldo):
        return self.saldo + saldo

    def sacar(self, saldo):
        return self.saldo - saldo

    def verificar_saldo(self):
        return self.saldo