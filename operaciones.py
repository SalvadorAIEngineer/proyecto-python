# operaciones.py
# Este módulo define funciones matemáticas básicas para la calculadora

# Suma
def suma(a, b):
    # Tu código aquí
    return a + b

# Resta
def resta(a, b):
    # Tu código aquí
    return a - b

# Multiplicación
def multiplica(a, b):
    # Tu código aquí
    return a * b

# División
def divide(a, b):
    # Tu código aquí
    # Debe manejar la división entre cero
    if b == 0:
        return "Error: División entre cero"
    return a / b
