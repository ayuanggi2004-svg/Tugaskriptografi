# decrypt_elgamal.py
from elgamal import decrypt

print("=== PROGRAM DEKRIPSI ELGAMAL ===\n")

# 1. Baca hasil enkripsi dari file
try:
    with open("ciphertext.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        public_key = eval(lines[0].strip())
        private_key = int(lines[1].strip())
        ciphertext = eval(lines[2].strip())
except FileNotFoundError:
    print("❌ File 'ciphertext.txt' tidak ditemukan. Jalankan dulu program enkripsi.")
    exit()

# 2. Proses dekripsi
decrypted = decrypt(private_key, public_key, ciphertext)
print("\n=== HASIL DEKRIPSI ===")
print("Plaintext : ", decrypted)

# 3. Simpan hasil dekripsi ke file
with open("hasil_dekripsi.txt", "w", encoding="utf-8") as f:
    f.write("=== HASIL DEKRIPSI ELGAMAL ===\n\n")
    f.write(f"Kunci Publik  : {public_key}\n")
    f.write(f"Kunci Privat  : {private_key}\n\n")
    f.write("Ciphertext    : {}\n\n".format(ciphertext))
    f.write("Plaintext     : {}\n".format(decrypted))

print("\n✅ Hasil dekripsi disimpan di file 'hasil_dekripsi.txt'")
