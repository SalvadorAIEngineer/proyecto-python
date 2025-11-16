# Día 4: Listas, ciclos y operadores lógicos
print("=== Día 4 ===")

#Ejercicio 1
numeros = [50,60,70,80,90]
suma = 0
for num in numeros:
    suma += num
print("Suma ", suma)
print("Promedio: ", suma / len(numeros))


#Ejercicio 2
nombres = ["Salvador", "Sara", "Lesley", "Efrein"]
for nombre in nombres:
    print("Hola", nombre)



#Ejercicio 3
total = 0
while True:
    n= int(input("Ingresa un numero (0 para salir): "))
    if n == 0:
        break
    total += n
print("Suma total:", total)
