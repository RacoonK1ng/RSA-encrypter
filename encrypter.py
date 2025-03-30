import random
from functions import read_line,encrypt,phi,generate_public_key,text_to_num,eeA,print_key

p1_pointer = random.randint(0, 3001134)
p1 = read_line(p1_pointer)
p2 = read_line(random.randint(0, 3001134))  #3001134 is the lowest line in primes.txt

while p1 == p2:
    p2 = read_line(random.randint(0, 3001134))

while True:
    message = []
    choice = str(input("Generate key[1]\nEncrypt with key[2]\nGenerate key and encrypt[3]\n What do you want to do ?:"))
    N = p1 * p2
    e = generate_public_key(phi(p1, p2))
    d = eeA(e, phi(p1, p2))
    if  choice== "1" or choice == "3":
        print_key(N, e, d)

    elif choice == "2":
        print("Public key")
        N= int(input("      N:"))
        e= int(input("      e:"))

    else:
        print("Entry is incorrect\n\n\n")



    if choice == "2" or choice== "3":
        choice = int(input("\nEncrypt text[1] or encrypt number[2] ?:"))
        if choice ==1:
            message = text_to_num(input("Text:"))
            print("Text as number:", message)
        else:
            message.append(int(input("Number:")))
            assert message[0] < N, "number to big" # number cant be bigger than N

        print("\n\nEncrypted message:", encrypt(message, e, N))

    choice = str(input("Encrypt a another message (y/n) ?: (y/n)?:")).lower()
    if choice == "n":
        break
    if choice != "y":
        print("Entry is incorrect\n\n\n")
        break