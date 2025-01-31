import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend")));

from sistema_bancario import SistemaBancario

sistema = SistemaBancario()

def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Conta")
        print("2. Consultar Saldo")
        print("3. Realizar Crédito")
        print("4. Realizar Débito")
        print("5. Realizar Transferência")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Informe o número da conta: ")
            sistema.cadastrar_conta(numero)
        elif opcao == "2":
            numero = input("Informe o número da conta: ")
            sistema.consultar_saldo(numero)
        elif opcao == "3":
            numero = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do crédito: "))
            sistema.realizar_credito(numero, valor)
        elif opcao == "4":
            numero = input("Informe o número da conta: ")
            valor = float(input("Informe o valor do débito: "))
            sistema.realizar_debito(numero, valor)
        elif opcao == "5":
            origem = input("Informe o número da conta de origem: ")
            destino = input("Informe o número da conta de destino: ")
            valor = float(input("Informe o valor da transferência: "))
            sistema.realizar_transferencia(origem, destino, valor)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
