from funktionen import decrypt,zahl_in_wort


print("Fürs entschlüsseln müssen sie ihren privaten Schlüssel eingeben:")
auswahl = "n"
while True:
    if auswahl == "n":
        print("Privater Schlüssel")
        N = int(input("     N:"))
        d = int(input("     d:"))
    elif auswahl != "y":
        print("Error")
    auswahl = str(input("Wollen sie ein Satz[1] oder eine Zahl entschlüsseln[2] ?:"))
    if auswahl != "1" and auswahl != "2":
        print("Eingabe ist inkorrekt\n\n\n")
        break
    nachricht = str(input("\nVerschlüsselte Nachricht:"))

    if auswahl == "1":
        nachrichtliste = decrypt(nachricht, d, N)
        print("Entschlüsselte Zahlen:", nachrichtliste)
        print("\n\nEntschlüsselter Satz:", zahl_in_wort(nachrichtliste))
    elif auswahl =="2":
        print("Entschlüsselte Nachricht:", decrypt(nachricht, d, N))
    else:
        print("Eingabe ist inkorrekt\n\n\n")
        break

    auswahl = str(input("Wollen sie noch etwas entschlüsseln (y/n) ?:")).lower()
    if auswahl == "n":
        break
    elif auswahl =="y":
        auswahl = str(input("Wollen sie den gleichen Schlüssel verwenden (y/n) ?:"))
    else:
        print("Eingabe ist inkorrekt\n\n\n")
        break