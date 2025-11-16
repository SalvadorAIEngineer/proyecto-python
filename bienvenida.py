#Requisitos:
#Pedir nombre al usuario.
#Mostrar un saludo personalizado.
#Si el nombre es "Salvador", mostrar:
#"Acceso autorizado: Ingeniero Principal"
#Si NO es Salvador, mostrar:
#"Acceso autorizado"

# Pedimos el nombre al usuario
nombre = input("Ingresa tu nombre: ")

# Saludo
print(f"Hola {nombre}, bienvenido al sistema")

# Condicional para roles
if nombre.lower() == "salvador":   # .lower() para evitar problemas con mayúsculas
    print("Acceso autorizado: Ingeniero Principal")
else:
    print("Acceso autorizado")
