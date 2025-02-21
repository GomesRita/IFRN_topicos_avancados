import requests

API_URL = "http://127.0.0.1:5000"

def obter_numero_conta():
    return input("Informe o número da conta: ")

def cadastrar_conta():
    opcaoConta = input('''Informe o tipo de conta:
        1. Conta Simples
        2. Conta Bônus
        3. Conta Poupança
    ''')
    numero = obter_numero_conta()
    saldoInicial = input("Informe saldo inicial para abrir a conta: ")
    response = requests.post(f"{API_URL}/cadastrar_conta", json={
        "numero": numero,
        "tipo_conta": opcaoConta,
        "saldo_inicial": saldoInicial
    })
    print(response.json()['message'])

def consultar_saldo():
    numero = obter_numero_conta()
    response = requests.get(f"{API_URL}/consultar_saldo/{numero}")
    print(response.json()['message'])

def consultar_pontuacao():
    numero = obter_numero_conta()
    response = requests.get(f"{API_URL}/consultar_pontuacao/{numero}")
    print(response.json()['message'])

def realizar_credito():
    numero = obter_numero_conta()
    valor = float(input("Informe o valor do crédito: "))
    response = requests.post(f"{API_URL}/realizar_credito", json={
        "numero": numero,
        "valor": valor
    })
    print(response.json()['message'])

def realizar_debito():
    numero = obter_numero_conta()
    valor = float(input("Informe o valor do débito: "))
    response = requests.post(f"{API_URL}/realizar_debito", json={
        "numero": numero,
        "valor": valor
    })
    print(response.json()['message'])

def realizar_transferencia():
    origem = obter_numero_conta()
    destino = input("Informe o número da conta de destino: ")
    valor = float(input("Informe o valor da transferência: "))
    response = requests.post(f"{API_URL}/realizar_transferencia", json={
        "origem": origem,
        "destino": destino,
        "valor": valor
    })
    print(response.json()['message'])

def render_juros():
    numero = obter_numero_conta()
    taxa = input("Informe a taxa de juros: ")
    response = requests.post(f"{API_URL}/render_juros", json={
        "numero": numero,
        "taxa": taxa
    })
    print(response.json()['message'])

def consultar_dados_conta():
    numero = obter_numero_conta()
    response = requests.get(f"{API_URL}/consultar_dados_conta/{numero}")
    print(response.json()['message'])

def menu():
    opcoes = {
        "1": cadastrar_conta,
        "2": consultar_saldo,
        "3": consultar_pontuacao,
        "4": realizar_credito,
        "5": realizar_debito,
        "6": realizar_transferencia,
        "7": render_juros,
        "8": consultar_dados_conta,
    }

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Conta")
        print("2. Consultar Saldo")
        print("3. Consultar Pontuação")
        print("4. Realizar Crédito")
        print("5. Realizar Débito")
        print("6. Realizar Transferência")
        print("7. Render Juros")
        print("8. Consultar Dados da Conta")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao in opcoes:
            opcoes[opcao]()
        elif opcao == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
