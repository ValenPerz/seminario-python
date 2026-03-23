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
        "jirafa",
        "tigre",
        "ballena",
        "cebra",
        "hormiga",
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

seleccion = input("Elegí una categoría: ").lower().strip()  # Selección de categoría
lista = words.get(seleccion)

while lista is None:  # En caso de escribirse mal
    print("Esa categoría no existe.")
    seleccion = input("Elegí una categoría: ").lower().strip()
    lista = words.get(seleccion)

word = random.choice(lista)
guessed = []
attempts = 8
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

print(word)  # Para debuggear

while attempts >= 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6  # Gana, +6 puntos
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
            puntaje -= 1  # Falla, -1 punto
            print("Esa letra no está en la palabra.")
        attempts -= 1
    else:
        print("Entrada no válida")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0
print("Tu puntaje fue: ", puntaje)
