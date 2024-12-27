def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.saldo += valor
            print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
        else:
            print("Conta não encontrada.")