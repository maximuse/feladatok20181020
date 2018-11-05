# Egy dolgozatra annak pontszámától függően a következő osztályzatot adják:
# elégtelen (1): 0 – 29 elégséges (2): 30 – 37 közepes (3): 38 – 43 jó (4): 44 – 49 jeles (5): 50 – 55
# Kérje be a dolgozat pontszámát, majd írja ki az osztályzatot számmal és betűvel!

p = int(input("Pontszám: "))

if (p == 0) or (p <= 29):
    print("1 (elégtelen)")
elif (p == 30) or (p <= 37):
    print("2 (elégséges)")
elif (p == 38) or (p <= 43):
    print("3 (közepes)")
elif (p == 44) or (p <= 49):
    print("4 (jó)")
elif (p == 50) or (p <= 55):
    print("5 (jeles)")
else:
    print("Hiba!")
