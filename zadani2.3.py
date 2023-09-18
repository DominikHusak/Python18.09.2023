from math import sqrt

while True:
    try:
        L = int(input("Zadej indukcnost [H]:"))
        if L <= 0:
            raise ValueError("Indukcnost musi byt kladne cislo")
        break
    except ValueError as e:
        print(e)
        print("Zadej platnou hodnotu")

while True:
    try:
        C = int(input("Zadej indukcnost [F]:"))
        if C <= 0:
            raise ValueError("Indukcnost musi byt kladne cislo")
        break
    except ValueError as e:
        print(e)
        print("Zadej platnou hodnotu")

F = 1 / (2 * 3.14 * sqrt(L * C))

print("Frekvence je: " + str(F) + "Hz")

