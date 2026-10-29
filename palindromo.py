def es_palindromo(palabra):
    # 1. Convertir a minúsculas
    palabra = palabra.lower()
    
    # 2. Invertir la palabra
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
        
    # 3. Comparar y retornar True o False
    if palabra == invertida:
        return True
    else:
        return False

# Este bloque hace que el código se ejecute SOLO si lo corres directamente
# No se ejecutará cuando lo importemos para las pruebas unitarias
if __name__ == "__main__":
    palabra = input("Escribe una palabra: ").lower()
    
    if es_palindromo(palabra):
        print(f"'{palabra}' es un palindromo!")
    else:
        print(f"'{palabra}' no es un palindromo.")
