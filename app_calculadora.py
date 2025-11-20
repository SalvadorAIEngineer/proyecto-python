# app_calculadora.py
# Este archivo importa operaciones.py y realiza cálculos

import operaciones

# Pedir al usuario dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Usar las funciones del módulo operaciones
print("Suma:", operaciones.suma(num1, num2))
print("Resta:", operaciones.resta(num1, num2))
print("Multiplicación:", operaciones.multiplica(num1, num2))
print("División:", operaciones.divide(num1, num2))
