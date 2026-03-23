import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 8
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

print(word)

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
print("Tu puntaje fue: ", puntaje)
