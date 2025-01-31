import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend")))

from sistema_bancario import SistemaBancario

sistema = SistemaBancario()

def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Conta")
        print("2. Consultar Saldo")
        print("3. Consultar Pontuacao")
        print("4. Realizar Crédito")
        print("5. Realizar Débito")
        print("6. Realizar Transferência")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcaoConta = input('''Informe o tipo de conta:
                1. Conta Simples
                2. Conta Bônus
                3. Conta Poupança
            ''')
            numero = input("Informe o número da conta: ")
<<<<<<< HEAD
            saldoInicial = input("Informe saldo inicial para abrir a conta: ")
            sistema.cadastrar_conta(numero, opcaoConta, saldoInicial)
=======
            if opcaoConta == '3':
                saldo_inicial = float(input("Informe o saldo inicial da conta poupança: "))
                sistema.cadastrar_conta(numero, opcaoConta, saldo_inicial)
            else:
                sistema.cadastrar_conta(numero, opcaoConta)
>>>>>>> 06201050be02cee6c7d37c9aa80211dde869a587
        elif opcao == "2":
            numero = input("Informe o número da conta: ")
            sistema.consultar_saldo(numero)
        elif opcao == "3":
            numero = input("Informe o número da conta: ")
            sistema.consultar_pontuacao(numero)
        elif opcao == "4":
            numero = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do crédito: "))
            sistema.realizar_credito(numero, valor)
        elif opcao == "5":
            numero = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do débito: "))
            sistema.realizar_debito(numero, valor)
        elif opcao == "6":
            origem = input("Informe o número da conta de origem: ")
            destino = input("Informe o número da conta de destino: ")
            valor = float(input("Informe o valor da transferência: "))
            sistema.realizar_transferencia(origem, destino, valor)
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()