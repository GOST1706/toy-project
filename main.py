import random
import sys

if __name__ == '__main__':
    rango = int(input('Ingresa un valor'))
    if not rango: rango = 0
    print("Generando un numero aleatorio en un rango de 0 a " + str(rango))
    print(random.randint(0,rango))
