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

