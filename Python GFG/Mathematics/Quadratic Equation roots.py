import math


def quadraticroots(a, b, c):
    d = math.floor((b * b) - (4 * a * c))
    e = math.sqrt(abs(d))
    r1 = math.floor((-b + e) / (2 * a))
    r2 = math.floor((-b - e) / (2 * a))

    if d < 0:
        print("Imaginary")
    elif r1 > r2:
        print(r1, r2)
    else:
        print(r2, r1)
