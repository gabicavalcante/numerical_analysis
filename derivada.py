from math import cos

def f(x):
    return x * cos(x)

lim = lambda x, h: (f(x + h) - f(x))/h

for h in [0.1, 0.05, 0.01, 0.005, 0.0001, 0.00005]:
    print(f"h: {h} -> {lim(1, h)}")