# 1. Variables
nombre = "Abelardo"
edad = 25
es_estudiante = True

# 2. Imprimir en pantalla (F-strings)

print(f"Hola mi nombre es {nombre} y tengo {edad} años.")

# 3. Condicionales
if es_estudiante:
    print("Soy estudiante, ¡A seguir aprendiendo !")
else: 
    print("Soy profesional, ¡A trabajar!")

# 4. Buckles
# imprimir los numero del 1 al 15
for i in range(1,6):
    print(f"Numero: {i}")

# 5. Interaccion con el usuario
nombre_usuario = input("Escribe tu nombre: ")
print(f"¡hola, {nombre_usuario}! Bienvenido a python. ")