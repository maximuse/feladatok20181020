# Kérj be egy egész óra értéket. Ha a szám nem 0 és 24 óra között van, akkor adjon hibaüzenetet, egyébként köszönjön el
# a program a napszaknak megfelelően!
# 4-9: Jó reggelt!, 10-17: Jó napot!, 18-21: Jó estét!, 22-3: Jó éjszakát!

o = int(input("Óra: "))

if (o >= 0) and (o < 24):
    if (o >= 4) and (o <= 9):
        print("Jó reggelt!")
    elif (o >= 10) and (o <= 17):
        print("Jó napot!")
    elif (o >= 18) and (o <= 21):
        print("Jó estét!")
    else:
        print("Jó éjszakát!")
else:
    print("Nem megfelelő számot írt be!")
