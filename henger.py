# Kérjük be a konzolról egy henger sugarát és magasságát cm-ben, majd - írjuk ki a henger térfogatát! - Írjuk ki a
# henger súlyát, ha ez tömör vashenger, és ha fahenger! A kiírásokban a számokat kerekítsük 2 tizedesre!

import math

r = int(input("Sugár: "))
m = int(input("Magasság: "))
v = pow(r, 2) * math.pi * m

print("Térfogat: " + str(round(v, 2)) + " cm3")
print("Vas fajsúlya: " + str(round(v * 7.2, 2)) + " g")
print("Fa fajsúlya: " + str(round(v * 1.5, 2)) + " g")
