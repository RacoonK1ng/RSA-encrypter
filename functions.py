import math
import random

def print_key(N, e, d):
    print("Public key:")
    print("     N:", N)
    print("     e:", e, "\n")
    print("Private key:")
    print("     N:", N)
    print("     d:", d, "\n")


def decrypt(c, d, n):

    i = 0
    pointer = 0
    list = []
    for x in c:
        if x == "-":
            list.append(pow(int(c[pointer:i]),d,n))
            pointer = i+1
        i += 1
    if i != pointer:
        list.append(pow(int(c[pointer:i]),d,n))

    return list

def num_to_text(number):

    text = ""
    for a in number:
        num=a
        word = ""
        while num > 0:
            rest = (num - 1) % 28
            if rest == 26:  # Treating " " as 27
                word = ' ' + word
            else:
                word = chr(rest + ord('A')) + word
            num = (num - 1) // 28
        text += word.lower()
    return text

assert num_to_text([443512])
assert num_to_text([4948959])
assert num_to_text([3879984635, 4439818116, 21327])

def read_line(line_number):

    with open("primes.txt", 'r') as file:
        for current_line, line in enumerate(file, start=1):
            if current_line == line_number:
                return int(line.strip())
    return "error"


def encrypt(m, e, n):

    product=""
    for x in m:
        product += str(pow(int(x), e, n))
        product += "-"
    return product[:-1]

assert encrypt([65], 17, 3233) == "2790"
assert encrypt([89], 23, 3233) == "2554"

def phi(p1, p2):
    return (p1 -1)*(p2 -1)
assert phi(7,29) == 168
assert phi(8,7) == 42
assert phi(0,1) ==0


def generate_public_key(n):

    e = read_line(random.randint(0, 3001134))
    if n % e == 0:
        generate_public_key(n)
    if n <= e:
        generate_public_key(n)
    return e

def eeA(e,n):#extended euclidean algorithm

    b = [n]
    a=[e]
    q=[]
    r=[]
    x=0
    y_old= 0
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
        y_old = y
        y = x - (q[i-1]*y)
        x = y_old
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


def text_to_num(text):

    symbols = []
    numbers = []
    point = 0
    i = 0
    for a in text:
        if i % 7== 0:
            symbols.append(text[point:i])
            point = i
        i+=1
    if point != i:
        symbols.append(text[point:i])

    for obj in symbols:
        obj = obj.upper()
        num = 0
        for letter in obj:
            if letter == ' ':
                num = num * 28 + 27  # Treating " " as 27
            else:
                num = num * 28 + (ord(letter) - ord('A') + 1)
        numbers.append(num)
    numbers.remove(0)
    return numbers


assert text_to_num("test") == [443512]
assert text_to_num("hallo") == [4948959]
assert text_to_num("hallo wie geht es") == [3879984635, 4439818116, 21327]
