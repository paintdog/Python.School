import random

# Einstellungen
untere_grenze = 1
obere_grenze = 20

# Variablen
richtige_antworten = 0
falsche_antworten = 0

# Wir informieren den Benutzer über das Programm
print("Kopfrechenaufgaben")
print() # Leerzeile
print("Eingabe e zum Beenden!")
print() # Leerzeile

# Hauptschleife
while True:

    zahl_1 = random.randint(untere_grenze, obere_grenze)
    zahl_2 = 6 # Auch hier eine Zufallszahl generieren!

    print("Was ergibt: " + str(zahl_1) + " * " + str(zahl_2) + "?")

    eingabe = input("Ihre Eingabe: ")

    if eingabe == "e":
        break
    else:
        benutzer_ergebnis = int(eingabe)

    if benutzer_ergebnis == zahl_1 * zahl_2:
        print("Das ist richtig!")
        # Die Zählvariable für korrekte Antworten muss erhöht werden
    else:
        print("Falsch! Richtig: " + str(zahl_1 * zahl_2) + "!")
        # Die Zählvariable für falsche Antworten muss erhöht werden
    print()

# Ausgabe der Statistik
print("Richtige Antwort(en): " + str(richtige_antworten))
print("Falsche Antwort(en): " + str(falsche_antworten))
