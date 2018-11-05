# Kérjünk be a konzolról egy valós számot! A szám akkor jó, ha 1000 és 2000 közötti páros egész (a határokat is
# beleértve). Írjuk ki, hogy a szám jó, vagy nem jó!

n = float(input("Szám: "))

if (n >= 1000) and (n <= 2000) and (n % 2 == 0):
    print("jó szám")
else:
    print("nem jó szám")
