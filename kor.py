# Olvassunk be egy nem negatív egész számot, valakinek az életkorát! Kortól függően írjuk ki a megfelelő szöveget:
# 0 – 13 évig: Gyermek 14 – 17 évig: Fiatalkorú 18 – 23 évig: Ifjú 24 – 59 évig: Felnőtt 60 évtől Idős

a = int(input("Kor: "))

if (a >= 0) and (a <= 13):
    print("Gyermek")
elif (a >= 14) and (a <= 17):
    print("Fiatalkorú")
elif (a >= 18) and (a <= 23):
    print("Ifjú")
elif (a >= 24) and (a <= 59):
    print("Felnőtt")
elif a <= 60:
    print("Idős")
