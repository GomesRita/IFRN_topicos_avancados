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
        print("3. Consultar Pontuacao")
        print("4. Realizar Crédito")
        print("5. Realizar Débito")
        print("6. Realizar Transferência")
        print("7. Render Juros")
        print("8. Sair")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            opcaoConta = input('''Informe o tipo de conta:
                1. Conta Simples
                2. Conta Bônus
                3. Conta Poupança
            ''');
            numero = input("Informe o número da conta: ")
            saldoInicial = input("Informe saldo inicial para abrir a conta: ")
            sistema.cadastrar_conta(numero, opcaoConta, saldoInicial)
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
            numero = input("Informe o número da conta: ")
            taxa = input("Informe a taxa de juros: ")
            sistema.render_juros(numero, taxa)
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
