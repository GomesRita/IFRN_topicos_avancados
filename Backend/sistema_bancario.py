class Conta:
   def __init__(self, numero):
       self.numero = numero;
       self.saldo = 0.0;


class SistemaBancario:
   def __init__(self):
       self.contas = {}


   def cadastrar_conta(self, numero):
       if numero in self.contas:
           print("Conta já cadastrada.")
       else:
           self.contas[numero] = Conta(numero)
           print(f"Conta {numero} cadastrada com sucesso.")
          
   #Simule a correção do bug abaixo e estabeleça um nova baseline (rc-1.3) após sua
   #correção, que será novamente validada.
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


   #As operações de débito e transferência não podem ser realizadas caso a conta
   #origem não tenha saldo suficiente (Não deve permitir saldo negativo);
   def realizar_debito(self, numero, valor):
       conta = self.contas.get(numero)


       if conta:
           if valor > 0:
               if conta.saldo < valor:
                   print('Saldo insuficiente, operação cancelada');
               else:
                   conta.saldo -= valor
                   print(f"Débito de R${valor:.2f} realizado na conta {numero}.");
           else:
               print('Informe um valor válido, operação não realizada')
       else:
           print("Conta não encontrada.")
          
   def realizar_transferencia(self, origem, destino, valor):
       conta_origem = self.contas.get(origem)
       conta_destino = self.contas.get(destino)


       if conta_origem and conta_destino:
           if valor > 0:
               if conta_origem.saldo < valor:
                   print('Saldo insuficiente, operação cancelada');
               else:
                   conta_origem.saldo -= valor
                   conta_destino.saldo += valor
                   print(f"Transferência de R${valor:.2f} realizada da conta {origem} para a conta {destino}.")
           else:
               print('Informe um valor válido, operação não realizada')
       else:
           print("Conta de origem ou destino não encontrada.")


   def consultar_saldo(self, numero):
       conta = self.contas.get(numero)
       if conta:
           print(f"Saldo da conta {numero}: R${conta.saldo:.2f}")
       else:
           print("Conta não encontrada.")
