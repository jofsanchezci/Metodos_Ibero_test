# cuenta_bancaria.py

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        self.saldo += monto
    
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto
    
    def obtener_saldo(self):
        return self.saldo
