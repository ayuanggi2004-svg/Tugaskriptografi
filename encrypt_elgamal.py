# encrypt_elgamal.py
from elgamal import generate_keys, encrypt

def main():
    # 1. Generate key (tanpa print ke terminal)
    public_key, private_key = generate_keys()

    # 2. Input pesan (ini satu-satunya yang tampil di terminal)
    message = input("Masukkan pesan yang akan dienkripsi: ").strip()

    # 3. Proses enkripsi
    cipher = encrypt(public_key, message)

    # 4. Simpan semua output ke file
    with open("ciphertext.txt", "w", encoding="utf-8") as f:
        # tulis kunci dengan format yang rapi
        p, g, y = public_key
        f.write("=== PROGRAM ENKRIPSI ELGAMAL ===\n\n")
        f.write(f"Kunci Publik : (p={p}, g={g}, y={y})\n")
        f.write(f"Kunci Privat : {private_key}\n\n")

        f.write("=== HASIL ENKRIPSI ===\n")
        for index, pair in enumerate(cipher, start=1):
            f.write(f"{index:02d}. {pair}\n")

if __name__ == "__main__":
    main()
