import random


def run():
    numero_random = random.randint(0, 100)
    user_num = int(input('Ingresa un numero entre 1 y 100: '))

    while user_num != numero_random:
        if user_num < numero_random:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        user_num = int(input('Elige otro número: '))

    if numero_random == user_num:
          print('El numero es correcto')

if __name__ == "__main__":
    run()
