# utils.py
def mod_exp(a, b, m):
    """Menghitung (a^b) mod m"""
    return pow(a, b, m)

def gcd(a, b):
    """Menghitung gcd (Greatest Common Divisor)"""
    if b == 0:
        return a
    return gcd(b, a % b)

def mod_inverse(a, m):
    """Mencari invers modulo dari a (a^-1 mod m)"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None