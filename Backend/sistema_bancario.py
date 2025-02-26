class Conta: #Conta Simples
    def __init__(self, numero):
        self.numero = numero;
        self.saldo = 0.0;

class ContaBonus:
    def __init__(self, numero):
        self.numero = numero;
        self.saldo = 0.0;
        self.pontuacao = 0.0;
        self.somadorDeposito = 0.0;
        self.somadorTransferencia = 0.0;

class ContaPoupanca:  # Nova classe: Conta Poupança
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0


class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, numero, opcaoConta, saldoInicial):
        if opcaoConta == '1':
            if numero in self.contas:
                return "Conta já cadastrada."
            else:
                self.contas[numero] = Conta(numero)
                conta = self.contas.get(numero)
                conta.saldo += float(saldoInicial)
                return f"Conta {numero} cadastrada com sucesso."
        if opcaoConta == '2':
            if numero in self.contas:
                return "Conta já cadastrada."
            else:
                self.contas[numero] = ContaBonus(numero)
                contaBonus = self.contas.get(numero)
                contaBonus.pontuacao += 10
                contaBonus.saldo += float(saldoInicial)
                return f"Conta {numero} cadastrada com sucesso."
        
        if opcaoConta == '3':  # Conta Poupança
            if numero in self.contas:
                return "Conta já cadastrada."
            else:
                self.contas[numero] = ContaPoupanca(numero)
                contaPoupanca = self.contas.get(numero)
                contaPoupanca.saldo += float(saldoInicial)
                return f"Conta {numero} cadastrada com sucesso."

    def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
           if valor > 0:
               conta.saldo += valor
               return f"Crédito de R${valor:.2f} realizado na conta {numero}."
           else:
               return 'Informe um valor válido, operação não realizada'
        else:
           return "Conta não encontrada."

    # Nova operação: Render Juros
    def render_juros(self, numero, taxa):
        conta = self.contas.get(numero)
        if conta:
            if isinstance(conta, ContaPoupanca):
                if float(taxa) > 0:
                    juros = conta.saldo * (float(taxa) / 100)
                    conta.saldo += juros
                    return f"Juros de R${juros:.2f} aplicados na conta {numero}. Novo saldo: R${conta.saldo:.2f}"
                else:
                    return "Taxa de juros inválida. Informe um valor positivo."
            else:
                return "Esta operação é permitida apenas para contas poupança."
        else:
            return "Conta não encontrada."

        
    def realizar_credito(self, numero, valor):
        conta = self.contas.get(numero);
        if conta:
            if valor > 0:
                if isinstance(conta, ContaBonus):
                    conta.somadorDeposito += valor;
                    if conta.somadorDeposito >= 100:
                        conta.pontuacao +=valor // 100;
                        conta.saldo += valor;
                        return f"Crédito de R${valor:.2f} realizado na conta {numero}."
                        conta.somadorDeposito == 0;
                else:
                    conta.saldo += valor
                    return f"Crédito de R${valor:.2f} realizado na conta {numero}."
            else:
                return 'Informe um valor válido, operação não realizada'

        else:
            return "Conta não encontrada."


    def realizar_debito(self, numero, valor):
        conta = self.contas.get(numero)

        if conta:
            if valor <= 0:  
                return 'Valor inválido para débito. Operação cancelada.'
            
            if conta.saldo - valor < -1000:
                return 'Limite de saldo negativo excedido. Operação cancelada.'
        
            conta.saldo -= valor
            return f"Débito de R${valor:.2f} realizado na conta {numero}."
        else:
            return "Conta não encontrada."
        
    def realizar_transferencia(self, origem, destino, valor):
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)

        if conta_origem and conta_destino:
            if valor <= 0:  # Valida se o valor é positivo
                return 'Valor inválido para transferência. Operação cancelada.'
            
            # Verifica se o saldo da conta de origem ficará abaixo do limite de -1000 após a transferência
            if conta_origem.saldo - valor < -1000:
                return 'Limite de saldo negativo excedido. Operação cancelada.'
            
            # Realiza a transferência
            conta_origem.saldo -= valor  # Subtrai o valor da conta de origem
            conta_destino.saldo += valor  # Adiciona o valor à conta de destino

            # Atualiza a pontuação da conta de destino (se for ContaBonus)
            if isinstance(conta_destino, ContaBonus):
                conta_destino.somadorTransferencia += valor
                if conta_destino.somadorTransferencia >= 150:
                    conta_destino.pontuacao += 1  # Adiciona 1 ponto a cada 150 reais transferidos
                    conta_destino.somadorTransferencia = 0  # Reinicia o somador

            return f"Transferência de R${valor:.2f} realizada da conta {origem} para a conta {destino}."
        else:
            return "Conta de origem ou destino não encontrada."
            


    def consultar_saldo(self, numero):
        conta = self.contas.get(numero)
        if conta:
            return f"Saldo da conta {numero}: R${conta.saldo:.2f}"
        else:
            return "Conta não encontrada."

    def consultar_pontuacao(self, numero):
        contaBonus = self.contas.get(numero)
        if contaBonus:
            if isinstance(contaBonus, ContaBonus):
                return f"Pontuacao da conta {numero}: R${contaBonus.pontuacao:.2f}"
            else:
                return "Sua conta não é do tipo conta bônus"
        else:
            return "Conta não encontrada."

    def consultar_dados_conta(self, numero):
        conta = self.contas.get(numero)
        if conta:
            tipo_conta = 'Conta Simples'
            if isinstance(conta, ContaBonus):
                tipo_conta = 'Conta Bonus'
            elif isinstance(conta, ContaPoupanca):
                tipo_conta = 'Conta Poupança'

            dados_conta = f"""
            Tipo de Conta: {tipo_conta}
            Número da Conta: {conta.numero}
            Saldo: R${conta.saldo:.2f}
            """
            if isinstance(conta, ContaBonus):
                dados_conta += f"Pontuação: {conta.pontuacao:.2f}"

            return dados_conta
        else:
            return "Conta não encontrada."