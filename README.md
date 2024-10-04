
# Ejemplo de Pruebas con PyTest

Este repositorio contiene un ejemplo básico y avanzado de cómo utilizar PyTest para realizar pruebas en Python. El ejemplo incluye una simulación de una clase `CuentaBancaria` con funcionalidades para manejar cuentas, realizar depósitos y retiros, y manejar excepciones.

## Requisitos

Para ejecutar estas pruebas, debes tener Python instalado en tu máquina, así como PyTest.

Puedes instalar PyTest usando:

```bash
pip install pytest
```

## Archivos

1. `cuenta_bancaria.py`: Contiene la clase `CuentaBancaria` con las siguientes funcionalidades:
   - Crear una cuenta con un saldo inicial.
   - Depositar una cantidad en la cuenta.
   - Retirar una cantidad, asegurando que haya suficiente saldo.
   - Obtener el saldo actual de la cuenta.

2. `test_cuenta_bancaria.py`: Contiene las pruebas para verificar el funcionamiento de `CuentaBancaria` utilizando PyTest:
   - Pruebas para crear cuentas, depositar y retirar dinero.
   - Manejo de excepciones cuando se intenta depositar un monto negativo o retirar más de lo disponible.
   - Pruebas parametrizadas para validar varios casos de depósitos.

## Ejecución de Pruebas

Para ejecutar las pruebas, simplemente corre el siguiente comando en la terminal desde el directorio donde están ubicados los archivos:

```bash
pytest
```

## Ejemplo de Salida

```bash
============================= test session starts ==============================
collected 6 items

test_cuenta_bancaria.py ......                                          [100%]

============================== 6 passed in 0.05s ===============================
```

Esto indica que todas las pruebas han pasado correctamente.

## Funcionalidades Cubiertas

- **Pruebas básicas**: Se verifican las funcionalidades principales como creación de cuenta, depósitos y retiros.
- **Manejo de excepciones**: Se asegura que el código maneja correctamente las situaciones en las que los montos no son válidos.
- **Pruebas parametrizadas**: Se ejecutan pruebas para múltiples casos de depósitos con diferentes saldos iniciales y montos.

Este ejemplo proporciona una base sólida para empezar a trabajar con PyTest y aplicar pruebas unitarias en proyectos de Python.
