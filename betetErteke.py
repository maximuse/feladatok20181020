# Írj programot, amely meghatározza, mennyi lesz egy betét értéke a futamidő végén, ha 10.000 Ft-ot helyezünk betétbe
# 8%-os névleges kamatláb mellett. Az évközi kamatozások száma 12. Az évek számát a felhasználótól kérje be a program.
# A futamidő végén nézett értéket az alábbi képlet alapján számold: FV = C * ((1 + (r / m)) ^ m * t)

import math

t = int(input("Évek száma: "))
c = 10000
r = 8
m = 12

fv = c * math.pow(1 + ((r / 100) / m), m * t)

print("a betét értéke a futamidő végén: " + str(round(fv)))
