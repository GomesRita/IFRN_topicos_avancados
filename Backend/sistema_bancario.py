class Conta:  # Conta Simples
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.limite_negativo = -1000.0  # Limite de saldo negativo

    def verificar_limite(self, valor):
        return self.saldo - valor >= self.limite_negativo


class ContaBonus:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.pontuacao = 0.0
        self.somadorDeposito = 0.0
        self.somadorTransferencia = 0.0
        self.limite_negativo = -1000.0  # Limite de saldo negativo

    def verificar_limite(self, valor):
        return self.saldo - valor >= self.limite_negativo


class ContaPoupanca:  # Nova classe: Conta Poupança
    def __init__(self, numero, saldo_inicial):
        self.numero = numero
        self.saldo = saldo_inicial  # Saldo inicial obrigatório


class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, numero, opcaoConta, saldoInicial):
        if opcaoConta == '1':
            if numero in self.contas:
                print("Conta já cadastrada.")
            else:
                self.contas[numero] = Conta(numero)
                conta = self.contas.get(numero)
                conta.saldo += float(saldoInicial)
                print(f"Conta {numero} cadastrada com sucesso.")
        elif opcaoConta == '2':
            if numero in self.contas:
                print("Conta já cadastrada.")
            else:
                self.contas[numero] = ContaBonus(numero)
                contaBonus = self.contas.get(numero)
                contaBonus.pontuacao += 10
                contaBonus.saldo += float(saldoInicial)
                print(f"Conta {numero} cadastrada com sucesso.")
        
        if opcaoConta == '3':  # Conta Poupança
            if numero in self.contas:
                print("Conta já cadastrada.")
            else:
                self.contas[numero] = ContaPoupanca(numero)
                contaPoupanca = self.contas.get(numero)
                contaPoupanca.saldo += float(saldoInicial)
                print(f"Conta {numero} cadastrada com sucesso.")

    def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
           if valor > 0:
               conta.saldo += valor
               print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
           else:
               print('Informe um valor válido, operação não realizada')
        else:
           print("Conta não encontrada.")

    def render_juros(self, numero, taxa):
        conta = self.contas.get(numero)
        if conta:
            if isinstance(conta, ContaPoupanca):
                if float(taxa) > 0:
                    juros = conta.saldo * (float(taxa) / 100)
                    conta.saldo += juros
                    print(f"Juros de R${juros:.2f} aplicados na conta {numero}. Novo saldo: R${conta.saldo:.2f}")
                else:
                    print("Taxa de juros inválida. Informe um valor positivo.")
            else:
                print("Esta operação é permitida apenas para contas poupança.")
        else:
            print("Conta não encontrada.")

    def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            if valor > 0:
                if isinstance(conta, ContaBonus):
                    conta.somadorDeposito += valor
                    if conta.somadorDeposito >= 100:
                        conta.pontuacao += valor // 100
                        conta.saldo += valor
                        print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
                        conta.somadorDeposito = 0
                else:
                    conta.saldo += valor
                    print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
            else:
                print('Informe um valor válido, operação não realizada')
        else:
            print("Conta não encontrada.")

    def realizar_debito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            if isinstance(conta, (Conta, ContaBonus)):
                if not conta.verificar_limite(valor):
                    print('Limite de saldo negativo excedido, operação cancelada')
                else:
                    conta.saldo -= valor
                    print(f"Débito de R${valor:.2f} realizado na conta {numero}.")
            else:
                if conta.saldo < valor:
                    print('Saldo insuficiente, operação cancelada')
                else:
                    conta.saldo -= valor
                    print(f"Débito de R${valor:.2f} realizado na conta {numero}.")
        else:
            print("Conta não encontrada.")

    def realizar_transferencia(self, origem, destino, valor):
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)

        if conta_origem and conta_destino:
            if conta_origem.saldo < valor:
                print('Saldo insuficiente, operação cancelada');
            else:
                if isinstance(conta_destino, ContaBonus):
                    conta_destino.somadorTransferencia += valor
                    if conta_destino.somadorTransferencia >= 150:
                        conta_destino.pontuacao +=valor // 150;
                        conta_origem.saldo -= valor
                        conta_destino.saldo += valor
                        print(f"Transferência de R${valor:.2f} realizada da conta {origem} para a conta {destino}.")
            else:
                if conta_origem.saldo < valor:
                    print('Saldo insuficiente, operação cancelada')
                else:
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

    def consultar_pontuacao(self, numero):
        contaBonus = self.contas.get(numero)
        if contaBonus:
            if isinstance(contaBonus, ContaBonus):
                print(f"Pontuacao da conta {numero}: R${contaBonus.pontuacao:.2f}")
            else:
                print("Sua conta não é do tipo conta bônus")
        else:
            print("Conta não encontrada.")