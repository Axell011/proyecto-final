import random
import time

print("  -- T R A G A M O N E D A S  VERSUS --\n")
print("Definan la cantidad de pozo para los jugadores(El pozo minimo es 10)")
print("La apuesta minima sera la mitad del pozo menos su decima parte")
pozo = int(input("Pozo: "))
if pozo < 10:
    while pozo < 10:
        print("La minima cantidad de dinero es 10. Vuelve a poner")
        pozo = int(input(""))
p = pozo//2 - pozo//10
print("La apuesta minima sera", p)
print("\nJUGADORES")
j1 = input("Jugador 1: ")
j2 = input("Jugador 2: ")
print("\nComienza jugando "+str(j1)+"...")
D1=[]
D2=[]
def juego(pozo,p,D):
    Ap = int(input("¿Cuántos soles quieres apostar?\n"))
    if Ap < 4 or Ap > pozo or Ap < p:
        while Ap < p:
            print("Es menor que la minima apuesta para tu cantidad"+"("+str(p)+")"+". Vuelve a poner")
            Ap = int(input(""))
        while Ap < 4:
            print("La minima apuesta es 4 soles. Vuelve a poner")
            Ap = int(input(""))
        while Ap > pozo:
            print("No tienes esa cantidad. Vuelve a poner")
            Ap = int(input(""))

    print()
    i = 0
    while i >= 0:
        i = i + 1
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        print("Jalando palanca")
        time.sleep(1.5)
        print("\n    | " + str(a) + " | " + str(b) + " | " + str(c) + " | ")

        if (a == b and b != c) or (a == c and b != a) or (b == c and a != c):
            ga = Ap
            print("\n¡Enhorabuena! Ha ganado " + str(ga) + " soles. Tiene ahora " + str(ga + pozo) + " soles.")

        elif a == b and a == c and b == c:
            ga = Ap * 4
            print("¡\nEnhorabuena! Ha ganado " + str(ga) + " soles. Tiene ahora " + str(ga + pozo) + " soles.")

        else:
            ga = -(Ap)
            print("\n¡Lo siento! Ha perdido " + str(-ga) + " soles. Tiene ahora " + str(pozo + ga) + " soles.")

        pozo = pozo + ga

        if pozo < Ap:
            print("Ya no puede apostar mas")
            print("\nSe retira con", pozo, "soles")
            break

        if pozo < 4:
            print("Ya no puede apostar mas")
            print("\nSe retira con", pozo, "soles")
            break
        rpta = input("Pulse X para terminar, otra tecla para seguir: ")
        if rpta in ["x", "X"]:
            print("\nSe retira con", pozo, "soles")
            break
        print()

    D.append(pozo)
    return

juego(pozo,p,D1)

print("\nTurno del jugador "+str(j2)+"...")

juego(pozo,p,D2)

for i in D1:
    DinJ1=i
for i in D2:
    DinJ2=i

print("\nRESULTADO")
time.sleep(1)
if DinJ1 > DinJ2:
    print("\nEl GANADOR es -->", end="  ");time.sleep(1);print(j1.upper())
elif DinJ1 < DinJ2:
    print("\nEl GANADOR es -->", end="  ");time.sleep(1);print(j2.upper())
elif DinJ1 == DinJ2:
    print("\nEMPATE")
print("\nGracias por jugar")
