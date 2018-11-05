# Írjon egy programot, ami kiszámolja a 13-as szorzótábla első 50 tagját, de csak azokat irja ki,
# melyek a 7-nek is többszörosei.

szorzo = 13
db = 50

for i in range(1, db + 1):
    if i * szorzo % 7 == 0:
        print(str(i * szorzo) + " ", end='')
