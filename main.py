# main.py
from elgamal import generate_keys, encrypt, decrypt

def main():
    print("=== Algoritma Kriptografi ElGamal ===")

    # 1. Generate key
    public_key, private_key = generate_keys()
    print("\nKunci Publik :", public_key)
    print("Kunci Privat:", private_key)

    # 2. Input pesan
    message = input("\nMasukkan pesan yang akan dienkripsi: ")

    # 3. Enkripsi
    cipher = encrypt(public_key, message)
    print("\nCiphertext :", cipher)

    # 4. Dekripsi
    decrypted = decrypt(private_key, public_key, cipher)
    print("\nHasil Dekripsi :", decrypted)


if __name__ == "__main__":
    main()
