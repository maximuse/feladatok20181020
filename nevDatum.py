# Írjon programot, ami bekéri a teljes nevet, a születési dátumot, majd kiírja a „Szia <keresztnév>! Te <x> éves vagy.”

import datetime

teljesNev = input("Teljes név: ")
ev = int(input("Születési év: "))

keresztNev = teljesNev.split(" ")[1]
kor = int(datetime.datetime.now().year - ev)

print("Szia " + keresztNev + "! Te " + str(kor) + " éves vagy.")
