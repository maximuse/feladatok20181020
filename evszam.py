# Kérj be egy évszámot! Ha a beütött szám negatív, akkor adj hibajelzést, ha nem, akkor állapítsd meg, hogy az évszám
# osztható-e 17-tel, vagy nem!


def loop(i):
    if i < 0:
        print("Hibás számot adott meg!")
        return True
    else:
        return False


n = int(input("Évszám: "))
while loop(n):
    n = int(input("Évszám: "))

if n % 17 == 0:
    print("A(z) " + str(n) + " osztható 17-tel.")
else:
    print("A(z) " + str(n) + " nem osztható 17-tel.")
