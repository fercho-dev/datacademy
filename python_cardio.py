import math


# Reto 1 Area de un triangulo
def area_triangulo():
    base = int(input("cual es la base del triangulo"))
    altura = int(input("cual es la altura del triangulo"))
    print((base * altura) / 2)

# Reto 2 Piedra, papel o tijera


def piedra_papel_tijera(jugador_1, jugador_2):
    if jugador_1 == "piedra":
        if jugador_2 == "piedra":
            print("Esto es un empate")
        elif jugador_2 == "papel":
            print("El ganador es el jugador 2")
        elif jugador_2 == "tijera":
            print("El ganador es el jugador 1")
    elif jugador_1 == "papel":
        if jugador_2 == "piedra":
            print("El ganador es el jugador 1")
        elif jugador_2 == "papel":
            print("Esto es un empate")
        elif jugador_2 == "tijera":
            print("El ganador es el jugador 2")
    elif jugador_1 == "tijera":
        if jugador_2 == "piedra":
            print("El ganador es el jugador 2")
        elif jugador_2 == "papel":
            print("El ganador es el jugador 1")
        elif jugador_2 == "tijera":
            print("Esto es un empate")

# Reto 3 conversor de millas a km


def from_mil_to_km()):
    millas=int(input("inserta el numero de millas"))
    print(millas * 1.609344)

# Reto 4 calculadora de volumenes
def volume(altura, radio):
    return math.pi * (radio**2) * altura

# Reto 5 rangos cambiantes
def rangos_cambiantes():
    limit_sup=int(input("ingresa el limite superior"))
    limit_inf=int(input("ingresa el limite inferior"))
    comp_num=int(input("ingresa el numero de comparacion"))

    if comp_num > limit_inf and comp_num < limit_sup:
        print(comp_num)
    elif comp_num < limit_inf:
        print("el numero es muy pequeño")
    elif comp_num > limit_sup:
        print("el numero es muy grande")

if __name__ == "__main__":
    pass
