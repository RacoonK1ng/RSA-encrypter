import random
from funktionen import lese_bestimmte_zeile,encrypt,phi,oeffentlicher_schluessel,wort_in_zahl,eeA,print_schlussel

p1stelle = random.randint(0,3001134)
p1 = lese_bestimmte_zeile(p1stelle)
p2 = lese_bestimmte_zeile(random.randint(0,3001134))  #3001134 ist die tiefste linie in primzahlen.txt

while p1 == p2:
    p2 = lese_bestimmte_zeile(random.randint(0,3001134))

while True:
    nachricht = []
    auswahl = str(input("Schlüssel generieren[1]\nVerschlüsseln mit vorhandenem Schlüssel[2]\nSchlüssel generieren und direkt verschlüsseln [3]\n Was wollen sie machen ?:"))
    N = p1 * p2
    e = oeffentlicher_schluessel(phi(p1, p2))
    d = eeA(e, phi(p1, p2))
    if  auswahl== "1" or auswahl =="3":
        print_schlussel(N,e,d)

    elif auswahl =="2":
        print("Öffentlicher Schlüssel")
        N= int(input("      N:"))
        e= int(input("      e:"))

    else:
        print("Eingabe ist inkorrekt\n\n\n")



    if auswahl =="2" or auswahl=="3":
        auswahl = int(input("\nWollen sie ein Satz[1] oder eine Zahl verschlüsseln[2] ?:"))
        if auswahl ==1:
            nachricht = wort_in_zahl(input("Satz:"))
            print("Satz als Zahlen:", nachricht)
        else:
            nachricht.append(int(input("Zahl:")))
            assert nachricht[0] <N, "Zahl zu gross" #Die Zahl darf nicht grösser sein als N

        print("\n\nVerschlüsselte Nachricht:", encrypt(nachricht, e, N))

    auswahl = str(input("Wollen sie eine weitere Aktion ausführen (y/n)?:")).lower()
    if auswahl =="n":
        break
    if auswahl != "y":
        print("Eingabe ist inkorrekt\n\n\n")
        break