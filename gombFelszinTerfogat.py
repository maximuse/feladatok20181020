# Kérje be a gömb sugarát, majd írja ki a gömb felszínét és térfogatát!

import math

r = int(input("Sugár: "))

print("felszín:\t" + str(4 * math.pow(r, 2) * math.pi) + "\ntérfogat:\t" + str(4 * math.pow(r, 3) * math.pi / 3))
