# Kérd be egy telek oldalait méterben! Írd ki a telek területét négyszögölben! (1 négyszögöl = 3,6 m2). Ha a telek 100
# négyszögölnél kisebb, akkor írja ki, hogy túl kicsi!

a = int(input("A: "))
b = int(input("B: "))

t = (a * b) / 3.6

print(str(t) + " négyszögöl")

if t <= 100:
    print("túl kicsi")
