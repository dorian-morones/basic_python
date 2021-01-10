def run():
    LIMITE = 100000
    contador = 0
    potencia = 2**contador
    while potencia < LIMITE:
        if potencia >= 255:
            break
        print('2 elevando a ' + str(contador) +
              ' es igual a: ' + str(potencia))
        contador = contador + 1
        potencia = 2**contador


if __name__ == "__main__":
    run()
