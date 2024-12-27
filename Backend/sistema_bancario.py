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

    def realizar_debito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.saldo -= valor
            print(f"Débito de R${valor:.2f} realizado na conta {numero}.")
        else:
            print("Conta não encontrada.")
            
    def realizar_transferencia(self, origem, destino, valor):
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)

        if conta_origem and conta_destino:
            conta_origem.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada da conta {origem} para a conta {destino}.")
        else:
            print("Conta de origem ou destino não encontrada.")

    def consultar_saldo(self, numero):
        conta = self.contas.get(numero)
        if conta:
            print(f"Saldo da conta {numero}: R${conta.saldo:.2f}")
        else:
            print("Conta não encontrada.")