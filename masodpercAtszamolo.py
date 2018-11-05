# Irjon egy programot, ami atszamolja a kiindulaskent megadott egeszszamu masodpercet evekke, honapokka, napokka,
# percekke es masodpercekke. (Hasznalja a modulo operatort : % ).

masodperc = int(input("Másodperc: "))

ev = 31556926
honap = 2629744
nap = 86400
ora = 3600
perc = 60

if int(masodperc / ev) > 0:
    print(str(int(masodperc / ev)) + " év")
maradek = masodperc = int(masodperc % ev)

if int(masodperc / honap) > 0:
    print(str(int(masodperc / honap)) + " hónap")
maradek = masodperc = int(masodperc % honap)

if int(masodperc / nap) > 0:
    print(str(int(masodperc / nap)) + " nap")
maradek = masodperc = int(masodperc % nap)

if int(masodperc / ora) > 0:
    print(str(int(masodperc / ora)) + " óra")
maradek = masodperc = int(masodperc % ora)

if int(masodperc / perc) > 0:
    print(str(int(masodperc / perc)) + " perc")
maradek = masodperc = int(masodperc % perc)

print(str(maradek) + " másodperc")
