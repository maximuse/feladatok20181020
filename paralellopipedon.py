# Irjon egy programot, ami kiszamolja egy derekszogű parallelepipedon terfogatat, aminek meg van adva a szelessege, a
# magassaga es a hosszusaga.

szelesseg = int(input("Szélesség: "))
magassag = int(input("Magasság: "))
hosszusag = int(input("Hosszúság: "))

volume = szelesseg * magassag * hosszusag

print("Térfogat: " + str(volume))
