# Kérd be a konzolról egy téglatest három élének hosszúságát, majd írd ki a hasáb felszínét és térfogatát!

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print("felszín:\t" + str(a * b * c) + "\ntérfogat:\t" + str((a * b * 2) + (a * c * 2) + (b * c * 2)))
