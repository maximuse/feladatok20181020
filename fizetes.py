# Kérjük be a konzolról egy alkalmazott fizetését! Ha ez a fizetés 100 000 forintnál nem nagyobb, akkor emeljük meg
# 25%-kal! Végül írjuk ki az alkalmazott fizetését!

fizetes = int(input("Fizetés: "))

if fizetes <= 100000:
    print(fizetes * 1.25)
else:
    print(fizetes)
