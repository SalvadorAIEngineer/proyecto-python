# Día 5: Funciones y módulos (Sistemas e IA)

# Funciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

# Función de saludo
def saludo(nombre):
    print("Hola", nombre)

# Usando las funciones
print("Suma:", suma(10, 5))
print("Resta:", resta(10, 5))
print("Multiplicación:", multiplica(10, 5))
saludo("Salvador")

# Librerías del sistema
import os
print("Directorio actual:", os.getcwd())



import calculadora

print("Suma:", calculadora.suma(5, 7))
print("Resta:", calculadora.resta(10, 3))
print("Multiplicación:", calculadora.multiplica(4, 6))