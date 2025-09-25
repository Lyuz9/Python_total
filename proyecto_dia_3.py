def analizar_texto():
    texto = input("Ingresa un texto: ")
    letras = input("Ingresa tres letras (separadas por espacios): ").lower().split()

    frecuencia_letras = {}
    texto_lower = texto.lower()  
    
    for letra in letras:
        frecuencia_letras[letra] = texto_lower.count(letra)

    print("\nFrecuencia de letras:")
    for letra, frecuencia in frecuencia_letras.items():
        print(f"La letra '{letra}' aparece {frecuencia} veces.")

    palabras = texto.split()
    cantidad_palabras = len(palabras)
    print(f"\nCantidad de palabras: {cantidad_palabras}")

    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"\nPrimera letra: {primera_letra}")
    print(f"Última letra: {ultima_letra}")

    palabras_invertidas = palabras[::-1]  
    texto_invertido = " ".join(palabras_invertidas) 
    print(f"\nTexto con palabras invertidas: {texto_invertido}")

    python_encontrado = "python" in texto_lower  
    resultados = {
        True: "La palabra 'Python' está presente en el texto.",
        False: "La palabra 'Python' no está presente en el texto."
    }
    print(f"\n{resultados[python_encontrado]}")

analizar_texto()