# Ha a számla ÁFA összege a számla nettó értékének egy adott százaléka, akkor hány százalék ÁFÁ-t tartalmaz a számla
# bruttó összege? Készíts a problémára egy kisegítő programot! Páldául 25%-os ÁFA esetén a számla 20% ÁFÁ-t tartalmaz,
# 12%-os ÁFA esetén a számla ÁFA tartalma 10,71%.

netto = int(input("Nettó: "))
afa = int(input("Áfa: "))

brutto = netto * ((100 + afa) / 100)
brottoAfa = brutto - netto
nettoAfa = (brottoAfa / brutto) * 100
print("bruttó: " + str(round(brutto)))
print("nettó áfa: " + str(round(nettoAfa)))
