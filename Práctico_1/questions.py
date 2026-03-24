import random

words = {
    "programacion": [
        "python",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
        "algoritmo",
    ],
    "animales": [
        "perro",
        "gato",
        "elefante",

    ],
    "paises": [
        "argentina",
        "japon",
        "mexico",
        "francia",
        "italia",
        "canada",
        "egipto",
        "australia",
    ],
}

print("Categorías disponibles:")
for nombre in words.keys():
    print("- " + nombre)

seleccion = input("Elegí una categoría: ").lower().strip()
lista = words.get(seleccion)

while lista is None:
    print("Esa categoría no existe.")
    seleccion = input("Elegí una categoría: ").lower().strip()
    lista = words.get(seleccion)

# Mezcla todas las palabras de la categoría elegida
palabras_mezcladas = random.sample(lista, k=len(lista))
puntaje = 0
i = 0  # Indice, sirve para saber si se terminó la categoría

print("¡Bienvenido al Ahorcado!")
print()

# El bucle for recorrerá la lista mezclada una por una
for word in palabras_mezcladas:
    guessed = []
    attempts = 8 # Se cambió a 8 porque habían palabras con hasta 7 caracteres diferentes como "Algoritmo"
    print(word)  # Para debuggear

    while attempts >= 0: # El comparador >= se debe a que si se acierta la palabra teniendo 1 intento, el jugador pierde igual
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            puntaje += 6
            print("¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ").lower()
        if len(letter) == 1 and ord(letter) > 96 and ord(letter) < 122:
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                puntaje -= 1
                print("Esa letra no está en la palabra.")
            attempts -= 1
        else:
            print("Entrada no válida")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
    # Pregunta si quiere seguir después de cada palabra
    # Solo se pregunta si todavía quedan palabras en la lista mezclada
    i += 1
    if i <= len(palabras_mezcladas) - 1:
        continuar = input("¿Querés jugar otra ronda con una nueva palabra? (s/n): ").lower().strip()
        if continuar != "s":
            print("Saliendo del juego")
            break
    else:
        print("Te quedaste sin palabras en esta categoría")

print("Tu puntaje final fue: ", puntaje)
