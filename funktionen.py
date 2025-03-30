import math
import random

def print_schlussel(N,e,d):
    print("Öffentlicher schlüssel:")
    print("     N:", N)
    print("     e:", e, "\n")
    print("Privater schlüssel:")
    print("     N:", N)
    print("     d:", d, "\n")


def decrypt(c, d, n):
    """
    Entschlüsselt eine Nachricht mithilfe des RSA-Verschlüsselungsalgorithmus.

    Args:
        c (str): Die verschlüsselte Nachricht, bestehend aus durch Bindestriche getrennten Zahlen.
        d (int): Der private Schlüssel.
        n (int): Der Modulus.

    Returns:
        list: Die entschlüsselte Nachricht als Liste von Zahlen.
    """
    i = 0
    punkt = 0
    list = []
    for x in c:
        if x == "-":
            list.append(pow(int(c[punkt:i]),d,n))
            punkt = i+1
        i += 1
    if i != punkt:
        list.append(pow(int(c[punkt:i]),d,n))

    return list

def zahl_in_wort(zahl):
    """
    Wandelt eine Zahl in ein Wort um, indem die Positionen der Buchstaben im Alphabet zurückgerechnet werden.
    Leerstellen werden als 27 behandelt.

    Args:
        zahl (list): Die Zahl, die umgewandelt werden soll.

    Returns:
        str: Das rekonstruierte Wort.
    """
    satz = ""
    for a in zahl:
        num=a
        wort = ""
        while num > 0:
            rest = (num - 1) % 28
            if rest == 26:  # Leerstellen als 27 behandeln
                wort = ' ' + wort
            else:
                wort = chr(rest + ord('A')) + wort
            num = (num - 1) // 28
        satz += wort.lower()
    return satz

assert zahl_in_wort([443512])
assert zahl_in_wort([4948959])
assert zahl_in_wort([3879984635, 4439818116, 21327])

def lese_bestimmte_zeile(zeilennummer):
    """
    Liest eine bestimmte Zeile aus einer Datei und gibt deren Inhalt als Ganzzahl zurück.

    Diese Funktion öffnet die Datei "primzahlen.txt" im Lesemodus und durchsucht sie nach der angegebenen Zeilennummer.
    Wenn die Zeilennummer gefunden wird, wird der Inhalt der Zeile als Ganzzahl zurückgegeben.
    Wenn die Zeilennummer nicht gefunden wird, gibt die Funktion "error" zurück.

    Args:
        zeilennummer (int): Die Zeilennummer, die gelesen werden soll.

    Returns:
        int: Der Inhalt der angegebenen Zeile als Ganzzahl.
        str: "error", wenn die Zeilennummer nicht gefunden wird.
    """
    with open("primzahlen.txt", 'r') as file:
        for aktuelle_zeilennummer, zeile in enumerate(file, start=1):
            if aktuelle_zeilennummer == zeilennummer:
                return int(zeile.strip())
    return "error"


def encrypt(m, e, n):
    """Verschlüsselt mehrere Zahlen mithilfe des RSA-Verschlüsselungsalgorithmus.
    Args:
        m (List): Die zu verschlüsselnde Nachricht, bestehend aus Ziffern.
        e (int): Der öffentliche Schlüssel.
        n (int): Der Modulus.

    Returns:
        str: Die verschlüsselte Nachricht, wobei die verschlüsselten Zahlen durch Bindestriche getrennt sind."""
    produkt=""
    for x in m:
        produkt += str(pow(int(x), e, n))
        produkt += "-"
    return produkt[:-1]

assert encrypt([65], 17, 3233) == "2790"
assert encrypt([89], 23, 3233) == "2554"

def phi(p1, p2):
    """Berechnet die Eulersche Phi-Funktion für zwei Primzahlen.

    Diese Funktion berechnet das Produkt der Werte (p1 - 1) und (p2 - 1),
    was der Anzahl der positiven ganzen Zahlen entspricht, die kleiner als
    das Produkt der beiden Primzahlen p1 und p2 sind und zu diesem teilerfremd sind.

    Args:
        p1 (int): Die erste Primzahl.
        p2 (int): Die zweite Primzahl.

    Returns:
        int: Das Produkt von (p1 - 1) und (p2 - 1), das die Anzahl der teilerfremden
             Zahlen zum Produkt der beiden Primzahlen darstellt."""
    return (p1 -1)*(p2 -1)
assert phi(7,29) == 168
assert phi(8,7) == 42
assert phi(0,1) ==0


def oeffentlicher_schluessel(n):
    """Wählt eine teilerfremde Primzahl von n aus, die kleiner N ist.

    Diese Funktion wählt zufällig eine Primzahl aus einer Liste von Primzahlen aus,
    die zu n teilerfremd ist und kleiner N ist. Die Auswahl erfolgt

    Args:
        N (int): Die Zahl, zu der eine teilerfremde Primzahl gefunden werden soll.

    Returns:
        int: Eine zufällig ausgewählte Primzahl, die zu n teilerfremd ist und kleiner
        als N ist.

    Hinweis:
        Die Funktion ruft sich rekursiv auf, wenn die ausgewählte Primzahl nicht
        teilerfremd zu n ist.
"""
    e = lese_bestimmte_zeile(random.randint(0, 3001134))
    if n % e == 0:
        oeffentlicher_schluessel(n)
    if n <= e:
        oeffentlicher_schluessel(n)
    return e

def eeA(e,n):#erweiterter Euklidischer algoritmus
    """Berechnet den modularen inversen Wert von e modulo n unter Verwendung des erweiterten euklidischen Algorithmus.

    Diese Funktion verwendet den erweiterten euklidischen Algorithmus, um den modularen inversen Wert von e
    modulo n zu berechnen. Der modulare Inverse ist eine Zahl y, die die Gleichung (e * y) % n = 1 erfüllt.

    Args:
        e (int): Die Zahl, deren modularer Inverser berechnet werden soll.
        n (int): Der Modulus.

    Returns:
        int: Der modulare Inverse von e modulo n. Wenn der berechnete Wert negativ ist, wird n hinzugefügt,
             um einen positiven Wert zu erhalten."""
    b = [n]
    a=[e]
    q=[]
    r=[]
    x=0
    yalt= 0
    y=0
    i=0
    while r==[] or r[i-1]>0:
        if a[i] > b[i]:
            q.append(math.floor(a[i] / b[i]))
            r.append(a[i] % b[i])
            if r[i] >0:
                a.append(r[i])
                b.append(b[i])
            i+= 1
        elif a[i]<b[i]:
            q.append(math.floor(b[i]/a[i]))
            r.append(b[i]%a[i])
            if r[i]>0:
                b.append(r[i])
                a.append(a[i])
            i+=1
    y = 1
    while i > 1:
        i -= 1
        yalt = y
        y = x - (q[i-1]*y)
        x = yalt
    if y <= 0 :
        return y+n
    else:
        return y

assert eeA(17,168)==89
assert eeA(23,220)==67
assert eeA(10, 17) == 12
assert eeA(7, 26) == 15
assert eeA(17, 3120) == 2753
assert eeA(25, 37) == 3


def wort_in_zahl(wort):
    """
    Wandelt ein Wort in eine einzelne Zahl um, indem die Positionen der Buchstaben im Alphabet summiert werden.
    Leerstellen werden als 27 behandelt.

    Args:
        wort (str): Das Wort, das umgewandelt werden soll.

    Returns:
        list: Die Summe der Positionen der Buchstaben im Alphabet.
    """
    zeichenliste = []
    zahlenliste = []
    punkt = 0
    i = 0
    for a in wort:
        if i % 7== 0:
            zeichenliste.append(wort[punkt:i])
            punkt = i
        i+=1
    if punkt != i:
        zeichenliste.append(wort[punkt:i])

    for obj in zeichenliste:
        obj = obj.upper()
        zahl = 0
        for buchstabe in obj:
            if buchstabe == ' ':
                zahl = zahl * 28 + 27  # Behandle Leerstellen als 27
            else:
                zahl = zahl * 28 + (ord(buchstabe) - ord('A') + 1)
        zahlenliste.append(zahl)
    zahlenliste.remove(0)
    return zahlenliste


assert wort_in_zahl("test") == [443512]
assert wort_in_zahl("hallo") == [4948959]
assert wort_in_zahl("hallo wie geht es") == [3879984635, 4439818116, 21327]
