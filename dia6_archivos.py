#crear un archivo
with open("empleados.txt","w") as archivo:
    archivo.write("Salvador\n")
    archivo.write("Mateo\n")
    archivo.write("Juana\n")
    archivo.write("Mario\n")

#Leer un archivo
with open("empleados.txt","r") as archivo:
    contenido= archivo.read()
    print(contenido)
    
#Agregar informacíon
with open("empleados.txt","a") as archivo:
    archivo.write("Ottoniel\n")

# Leer archivo actualizado
with open("empleados.txt","r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("Contenido final:")
    print(contenido)
