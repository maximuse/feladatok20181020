# Ha beteszünk a bankba egy adott összeget, adott éves kamatszázalékra, adott hónapra, mennyi pénzt vehetünk majd fel az
# idő lejártakor?
import math

osszeg = int(input("Összeg: "))
szazalek = int(input("Éves kamatszázalék: "))
honap = int(input("Hónapok száma: "))

eredmeny = round(osszeg * math.pow(((100 + szazalek) / 100), honap / 12))

print(str(eredmeny))
