import random


def run():
    texto = '''
            ***************************************
                Bienvenido al juego del aleatorio
                Adivina que número del 1 al 100
                     eligió la computadora.
            ***************************************
Ingresa tu número: '''
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input(texto))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige un número mayor')
        else:
            print('Elige un número menor')
        numero_elegido = int(input('Ingresa otro número: '))
    print('Ganaste!!')


if __name__ == '__main__':
    run()20