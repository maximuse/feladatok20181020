# Irjon egy programot, ami kiiratja a 7-es szorzotabla elso 20 tagjat, csillaggal jelolve azokat, amelyek 3-nak
# tobbszorosei. Pelda: 7 14 21* 28 35 42* 49

szorzo = 7
db = 20

for i in range(1, db + 1):
    if i * szorzo % 3 == 0:
        print(str(i * szorzo) + "* ", end='')
    else:
        print(str(i * szorzo) + " ", end='')
