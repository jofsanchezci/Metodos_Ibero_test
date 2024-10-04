# test_cuenta_bancaria.py

import pytest
from cuenta_bancaria import CuentaBancaria

# Prueba de creación de cuenta
def test_crear_cuenta():
    cuenta = CuentaBancaria("Juan", 1000)
    assert cuenta.titular == "Juan"
    assert cuenta.obtener_saldo() == 1000

# Prueba de depósito
def test_depositar():
    cuenta = CuentaBancaria("Ana", 500)
    cuenta.depositar(200)
    assert cuenta.obtener_saldo() == 700

# Prueba de excepción en depósito
def test_depositar_monto_negativo():
    cuenta = CuentaBancaria("Ana", 500)
    with pytest.raises(ValueError):
        cuenta.depositar(-100)

# Prueba de retiro
def test_retirar():
    cuenta = CuentaBancaria("Carlos", 800)
    cuenta.retirar(300)
    assert cuenta.obtener_saldo() == 500

# Prueba de excepción por saldo insuficiente
def test_retirar_saldo_insuficiente():
    cuenta = CuentaBancaria("Pedro", 100)
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        cuenta.retirar(150)

# Prueba parametrizada (diferentes casos de depósitos válidos)
@pytest.mark.parametrize("saldo_inicial, deposito, saldo_final_esperado", [
    (100, 50, 150),
    (200, 100, 300),
    (0, 500, 500),
])
def test_depositos_parametrizados(saldo_inicial, deposito, saldo_final_esperado):
    cuenta = CuentaBancaria("Luis", saldo_inicial)
    cuenta.depositar(deposito)
    assert cuenta.obtener_saldo() == saldo_final_esperado
