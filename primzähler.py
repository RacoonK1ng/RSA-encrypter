import os
max = 100000 # höhste primzahl
allNs = list(range(2, max))

for i in allNs:
    for x in range(i+i,max, i):
        print("Eliminiert  ", x, "   vielfaches von  ",i)
        try:
            allNs.remove(x)
        except:
            pass

file = open("primzahlen.txt", "w")
for x in allNs:
    file.write(str(x)+"\n")
file.close()
