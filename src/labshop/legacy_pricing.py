import math

T = [(0, 1.0), (10, 0.97), (50, 0.94), (100, 0.9), (500, 0.85)]


def f(q, p, c=None):
    r = 1.0
    for a, b in T:
        if q > a:
            r = b
    if c is not None and c in ("gov", "edu"):
        r = r * 0.95
    v = q * p * r
    return math.floor(v * 100) / 100


def g(q, p, c=None):
    return round(q * p - f(q, p, c), 2)
