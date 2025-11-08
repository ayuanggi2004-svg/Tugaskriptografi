# encrypt_elgamal.py
from elgamal import generate_keys, encrypt

print("=== PROGRAM ENKRIPSI ELGAMAL ===\n")

# 1. Generate key
public_key, private_key = generate_keys()
print("Kunci Publik : (p={}, g={}, y={})".format(*public_key))
print("Kunci Privat : {}\n".format(private_key))

# 2. Input pesan
message = input("Masukkan pesan yang akan dienkripsi: ").strip()

# 3. Proses enkripsi
cipher = encrypt(public_key, message)
print("\n=== HASIL ENKRIPSI ===")
for index, pair in enumerate(cipher, start=1):
    print(f"{index:02d}. {pair}")

# 4. Simpan hasil ke file
with open("ciphertext.txt", "w", encoding="utf-8") as f:
    f.write(f"{public_key}\n")
    f.write(f"{private_key}\n")
    f.write(str(cipher))

print("\n✅ Ciphertext dan kunci berhasil disimpan di 'ciphertext.txt'")
