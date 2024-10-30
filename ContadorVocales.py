# Función para contar y almacenar las vocales
def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']  # Incluyendo vocales con tilde
    arreglo_vocales = []
    # Recorrer la frase letra por letra
    for letra in frase.lower():
        if letra in vocales:
            arreglo_vocales.append(letra)  # Almacenar la vocal en el arreglo

    # Mostrar los resultados
    print(f"Cantidad de vocales encontradas: {len(arreglo_vocales)}")
    print(f"Vocales encontradas: {arreglo_vocales}")
# Solicitar la frase al usuario
frase_usuario = input("Ingresa una frase: ")
contar_vocales(frase_usuario)