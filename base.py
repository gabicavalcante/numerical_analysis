def to_base(number, base):
    restos = []
    while(True):
        restos.append(str(number % base))
        number = number/base
        if number == 0:
            break
    return ''.join(reversed(restos))

convert = lambda n, b, p: n * (b ** p)

def b(number, base):
    b_string = str(number)
    p = len(b_string) - 1
    total = 0
    for n in b_string: 
        total += convert(int(n), base, p)
        p -= 1
    return total


#b(110, 2)
b(4013, 5)
print(to_base(508, 7))