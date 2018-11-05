# Kérj be egy egyjegyű, nem negatív számot! Írd ki a szám szöveges formáját.

n = int(input("Szám: "))

if (n >= 0) and (n < 10):
    if n == 0:
        print("nulla")
    elif n == 1:
        print("egy")
    elif n == 2:
        print("kettő")
    elif n == 3:
        print("három")
    elif n == 4:
        print("négy")
    elif n == 5:
        print("öt")
    elif n == 6:
        print("hat")
    elif n == 7:
        print("hét")
    elif n == 8:
        print("nyolc")
    elif n == 9:
        print("kilenc")
else:
    print("Nem megfelelő számot írt be!")
