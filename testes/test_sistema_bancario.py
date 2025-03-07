import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Backend.sistema_bancario import SistemaBancario, Conta, ContaBonus, ContaPoupanca

# Testes para Cadastrar Conta
def test_cadastrar_conta_simples():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    assert "123" in sistema.contas
    assert isinstance(sistema.contas["123"], Conta)
    assert sistema.contas["123"].saldo == 100.0

def test_cadastrar_conta_bonus():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("456", "2", 200.0)
    assert "456" in sistema.contas
    assert isinstance(sistema.contas["456"], ContaBonus)
    assert sistema.contas["456"].saldo == 200.0
    assert sistema.contas["456"].pontuacao == 10

def test_cadastrar_conta_poupanca():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("789", "3", 300.0)
    assert "789" in sistema.contas
    assert isinstance(sistema.contas["789"], ContaPoupanca)
    assert sistema.contas["789"].saldo == 300.0

# Testes para Crédito
def test_realizar_credito():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    sistema.realizar_credito("123", 50.0)
    assert sistema.contas["123"].saldo == 150.0

def test_realizar_credito_valor_negativo():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    sistema.realizar_credito("123", -50.0)
    assert sistema.contas["123"].saldo == 100.0  # O saldo não deve mudar

def test_realizar_credito_bonus():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "2", 100.0)  # Conta Bônus
    sistema.realizar_credito("123", 150.0)
    assert sistema.contas["123"].saldo == 250.0
    assert sistema.contas["123"].pontuacao == 11  # 10 pontos iniciais + 1 ponto extra

# Testes para Débito
def test_realizar_debito():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    sistema.realizar_debito("123", 50.0)
    assert sistema.contas["123"].saldo == 50.0

def test_realizar_debito_valor_negativo():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    sistema.realizar_debito("123", -50.0)
    assert sistema.contas["123"].saldo == 100.0  # O saldo não deve mudar

def test_realizar_debito_saldo_insuficiente():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)  
    
    resultado = sistema.realizar_debito("123", 1200.0)
    
    assert resultado == 'Limite de saldo negativo excedido. Operação cancelada.'
    assert sistema.contas["123"].saldo == 100.0

# Testes para Transferência
def test_realizar_transferencia():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)  # Conta de origem
    sistema.cadastrar_conta("456", "2", 50.0)   # Conta de destino (Bônus)
    sistema.realizar_transferencia("123", "456", 30.0)
    assert sistema.contas["123"].saldo == 70.0
    assert sistema.contas["456"].saldo == 80.0

def test_realizar_transferencia_valor_negativo():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)
    sistema.cadastrar_conta("456", "2", 50.0)
    sistema.realizar_transferencia("123", "456", -30.0)
    assert sistema.contas["123"].saldo == 100.0  # O saldo não deve mudar
    assert sistema.contas["456"].saldo == 50.0   # O saldo não deve mudar

def test_realizar_transferencia_bonus():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)  
    sistema.cadastrar_conta("456", "2", 50.0)   
    
    resultado = sistema.realizar_transferencia("123", "456", 1200.0)

    assert resultado == 'Limite de saldo negativo excedido. Operação cancelada.'
    assert sistema.contas["123"].saldo == 100.0
    assert sistema.contas["456"].saldo == 50.0
    assert sistema.contas["456"].pontuacao == 10

# Testes para Render Juros
def test_render_juros():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "3", 100.0)  # Conta Poupança
    sistema.render_juros("123", 10.0)  # 10% de juros
    assert sistema.contas["123"].saldo == 110.0

def test_render_juros_conta_nao_poupanca():
    sistema = SistemaBancario()
    sistema.cadastrar_conta("123", "1", 100.0)  # Conta Simples
    sistema.render_juros("123", 10.0)
    assert sistema.contas["123"].saldo == 100.0  # O saldo não deve mudar