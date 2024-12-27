class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, numero):
        if numero in self.contas:
            print("Conta já cadastrada.")
        else:
            self.contas[numero] = Conta(numero)
            print(f"Conta {numero} cadastrada com sucesso.")

   def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.saldo += valor
            print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
        else:
            print("Conta não encontrada.")
