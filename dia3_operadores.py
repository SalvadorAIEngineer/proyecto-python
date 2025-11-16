print("=== Día 3: Operadores y entradas ===")

#Ejercicio 1
print("\n--- Operaciones aritméticas ---")
a= float(input("ingresa el primer número: "))
b= float(input("Ingresa el segundo número: "))


print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicación:", a*b)
print("Divisíon:", a/b)

#Ejercicio 2
print("\n--- Edad del usuario ---")
edad= int(input("Ingresa tu edad: "))


if edad < 18:
    print("Eres menor de edad")
elif edad < 60:
    print("Eres adulto")
else:
    print("Eres adulto mayor")


#Ejercicio 3
print("\n--- Número positivo, negativo o cero ---")
numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El número es cero")
    