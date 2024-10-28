import random

def wuerfel_zaehlen(anzahl_wuerfel):
    zaehler = [0] * 6
    i = 0
    while i < anzahl_wuerfel:
        wurf = random.randint(1, 6)
        zaehler[wurf - 1] += 1
        i += 1
    zahl = 0
    while zahl < 6:
        print(f"{zahl + 1}: {zaehler[zahl]} mal")
        zahl += 1
anzahl = int(input("Giben Sie die Anzahl der Würfel ein: "))
wuerfel_zaehlen(anzahl)
