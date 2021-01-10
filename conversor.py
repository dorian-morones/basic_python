def conversor(type, dolar_price):
    pesos = float(input("Ingresa tus pesos " + type + ": "))
    dolares = pesos / dolar_price
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """

Bienvenido al conversor de monedas 💰

1 - Pesos Mexicanos
2 - Pesos Argentinos
3 - Pesos Colombianos

Elige una opcion:
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("Mexicanos", 20)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Colombianos", 3875)
else:
    print('selecciona una opcion')
