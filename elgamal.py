# elgamal.py
import random

def generate_keys():
    p = 467  # bilangan prima
    g = 2    # generator
    x = random.randint(1, p - 2)  # private key
    y = pow(g, x, p)              # public key component
    return (p, g, y), x

def encrypt(public_key, plaintext):
    p, g, y = public_key
    cipher = []
    for char in plaintext:
        m = ord(char)
        k = random.randint(1, p - 2)
        a = pow(g, k, p)
        b = (pow(y, k, p) * m) % p
        cipher.append((a, b))
    return cipher

def decrypt(private_key, public_key, ciphertext):
    p, g, y = public_key
    plaintext = ""
    for a, b in ciphertext:
        s = pow(a, private_key, p)
        m = (b * pow(s, -1, p)) % p
        plaintext += chr(m)
    return plaintext
