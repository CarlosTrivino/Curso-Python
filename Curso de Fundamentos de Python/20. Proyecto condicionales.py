# Proyecto: condicionales
'''
Vamos a empezar a crear el proyecto del curso que consiste en el juego de piedra papel o tijera,
a medida que se avanza en las clases, se irá mejorando el juego
'''
# Apartir de aquí inicia el juego:
import random # Se usa esta librería para que el computador seleccione aleatoriamente una opción

user_score = 0
computer_score = 0

while True:
    print("\n\n",30*"*")
    user_option = input("Piedra, Papel o Tijera=>")
    computer_option = random.choice(['Piedra', 'Papel', 'Tijera']) # Con este módulo, el computador seleccione aleatoriamente una opción
    


    print("\n\nJugador: ",user_option)
    print("\nComputador: ",computer_option)


    if user_option == computer_option:
        print("\nEmpate!")
        print("\nPuntuación Jugador: ",user_score,"\nPuntuación Computador: ",computer_score)
    elif user_option == "Piedra" and computer_option == "Papel":
        print("\nPunto para el Computador!")
        computer_score +=1
        print("\nPuntuación Jugador: ",user_score,"\nPuntuación Computador: ",computer_score)
    elif user_option == "Piedra" and computer_option == "Tijera":
        print("Punto para el Jugador!")
        user_score +=1
        print("Puntuación Jugador: ",user_score,"\nPuntuación Computador: ",computer_score)
    elif user_option == "Papel" and computer_option == "Piedra":
        print("Punto para el Jugador!")
        user_score +=1
        print("Puntuación Jugador: ",user_score,"\nPuntuación Computador: ",computer_score)
    elif user_option == "Papel" and computer_option == "Tijera":
        print("Punto para el Computador!")
        computer_score +=1
        print("Puntuación Jugador: ",user_score,"\nPuntuación Computador: ",computer_score)
    else:
        print("Debe elegir una opción válida")

    if user_score ==3 or computer_score == 3:
        break
    else:
        continue