# Tárold konstansokban a krumpli, a hagyma és a padlizsán egységárát! Írj olyan programot, amely bekéri, hogy miből
# mennyit óhajt a vásárló, majd készítsen egy számlát

KRUMPLI = 70
HAGYMA = 98
PADLIZSAN = 200

krumpli = float(input("Krumpli: "))
hagyma = float(input("Hagyma: "))
padlizsan = float(input("Padlizsán: "))

print("Krumpli: " + str(krumpli) + " kg * " + str(KRUMPLI) + " Ft/kg = " + str(round(krumpli * KRUMPLI)) + " Ft")
print("Hagyma: " + str(hagyma) + " kg * " + str(HAGYMA) + " Ft/kg = " + str(round(hagyma * HAGYMA)) + " Ft")
print("Padlizsán: " + str(padlizsan) + " kg * " + str(PADLIZSAN) + " Ft/kg = " + str(round(padlizsan * PADLIZSAN)) + " Ft")
print("----------------------------------------------------------------------------------Összesen: {0} Ft".format(
    str(round((krumpli * KRUMPLI) + (hagyma * HAGYMA) + (padlizsan * PADLIZSAN)))))
