import random
import sys

if __name__ == '__main__':
    rango = int(sys.argv[1])
    print("Generando un numero aleatorio en un rango de 0 a " + str(rango))
    print(random.choice(range(rango)))
