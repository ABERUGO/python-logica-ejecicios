# Pedir la palabra al usuario y convertirla a minusculas
palabra = input("Escribe una palabra: ").lower()

# Crear un diccionario con las vocales inicializadas en 0
# Esto se llama "Inicializar el diccionario"
contador_vocales = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

# Recorrer la palabra letra por letra
for letra in palabra:
    # Si la letra esta en el diccionario (es una vocal)
    if letra in contador_vocales:
        # Sumamos 1 añ valor de esa vocal
        contador_vocales[letra] += 1

# Mostrar el resultado final
print(f"La palabra '{palabra}' tiene las siguiente vocales: ")
for vocal, cantidad in contador_vocales.items():
    if cantidad > 0: # Solo mostramos las vocales que aparecen al menos una vez
        print(f" {vocal}: {cantidad}")

#Inicializar el contador de vocales
contador_vocales = 0
contador_consonantes = 0
# Recorrer la palabra letra por letra
for letra in palabra:
    # Verificar si la letra actual es una vocal
    if letra in "aeiou":
        contador_vocales += 1
    elif letra.isalpha():
        contador_consonantes += 1

# Mostrar el resultado final
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales y {contador_consonantes} consonantes. ")