"""
Juego simple de Adivina el Numero
contiene una variable con un numero aleatorio, y el usuario debe adivinarlo
todo esto corre dentro de un bucle infinito que se rompe si el usuario escribe "exit"
"""

import random

def adivinaElNumero():
    while True:
        numero = random.randint(1, 10)
        print("Adivina el numero entre 1 y 10")
        numJugador = input('Ingresa el Numero: ')
        if numJugador == numero:
            print("Adivinaste el numero")
            print('Para salir escribe exit')
        else:
            print("No adivinaste el numero")
            print("El numero era: ", numero)
            print('Para salir escribe exit')
            if numJugador == 'exit':
                break


adivinaElNumero()