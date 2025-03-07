from flask import Flask, jsonify, request

from sistema_bancario import SistemaBancario

app = Flask(__name__)

sistema = SistemaBancario()

@app.route('/', methods=['GET'])
def hello_world():
        return jsonify('Sistema bancário')

@app.route('/cadastrarConta', methods=['POST'])
def cadastrar_conta():
    data = request.get_json()

    if not data or 'numero' not in data or 'opcaoConta' not in data or 'saldoInicial' not in data:
        return jsonify({"erro": "Dados inválidos ou faltando."}), 400

    else: 
        numero = data['numero']
        opcaoConta = data['opcaoConta']
        saldoInicial = data['saldoInicial']
        
        conta = sistema.cadastrar_conta(numero, opcaoConta, saldoInicial)
        return jsonify(conta)

@app.route('/realizarCredito', methods=['PUT'])
def realizar_credito():
    data = request.get_json()

    if not data or 'numero' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados inválidos ou faltando."}), 400
    else:
        numero = data['numero']
        valor = data['valor']

        conta = sistema.realizar_credito(numero, valor)
        return jsonify(conta)

@app.route('/renderJuros', methods=['GET'])
def render_juros():
    data = request.get_json()

    if not data or 'numero' not in data or 'taxa' not in data:
        return jsonify({"erro": "Dados inválidos ou faltando."}), 400

    else:
        numero = data['numero']
        taxa = data['taxa']

        conta = sistema.render_juros(numero, taxa)
        return jsonify(conta)

@app.route('/realizarDebito', methods=['PUT'])
def realizar_debito():
    data = request.get_json()

    if not data or 'numero' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados inválidos ou faltando."}), 400

    else:
        numero = data['numero']
        valor = data['valor']

        conta = sistema.realizar_debito(numero, valor)
        return jsonify(conta)

@app.route('/realizarTransferencia', methods = ['PUT'])
def realizar_transferencia():
    data = request.get_json()

    if not data or 'origem' not in data or 'destino' not in data or 'valor' not in data:
        return jsonify({"erro": "Dados inválidos ou faltando."}), 400

    else:
        origem = data['origem']
        destino = data['destino']
        valor = data['valor']

        conta = sistema.realizar_transferencia(origem, destino, valor)
        return jsonify(conta)


@app.route('/saldo/<int:numero>', methods=['GET'])
def consultar_saldo(numero):
    conta = sistema.consultar_saldo(numero)
    return jsonify(conta)

@app.route('/consultarPontuacao/<int:numero>', methods = ['GET'])
def consultar_pontuacao(numero):
    conta = sistema.consultar_pontuacao(numero)
    return jsonify(conta)

@app.route('/consultarConta/<int:numero>')
def consultar_dados_conta(numero):
    conta = sistema.consultar_dados_conta(numero)
    return jsonify(conta)

app.run(port=8080, host='0.0.0.0', debug=True)
