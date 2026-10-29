# 1. La forma "pythonica" (Slicing)
palabra = input("Escribe una palabra: ")
palabra_invertida = palabra[::-1]
print(f"La palabra invertida es: {palabra_invertida}")

# 2. La forma "Logica" (Para la entrevista)
palabra = input("Escribe una palabra: ")

# 1. Creamos la variable vacia
invertida = ""

# Recorremos la palabra
for letra in palabra:
    # 3. Aqui esta el truco: ¿Como concatenamos la letra para que quede al prinicipio?
    # Pista: Es similar a invertida = invertida + letra, pero al reves.
    invertida = letra + invertida # <--- ¡Esta es la linea magica!

print(f"La palabra original es: {palabra}")
print(f"La palabra invertida es: {invertida}")