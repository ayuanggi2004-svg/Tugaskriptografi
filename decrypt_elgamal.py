# decrypt_elgamal.py
from elgamal import decrypt
import re
import ast
import sys

def load_ciphertext_file(path="ciphertext.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [ln.rstrip("\n") for ln in f.readlines()]
    except FileNotFoundError:
        print("❌ File 'ciphertext.txt' tidak ditemukan. Jalankan dulu program enkripsi.")
        sys.exit(1)

    text = "\n".join(lines)

    # --- Format lama (3 baris raw) ---
    try:
        pk_old = ast.literal_eval(lines[0].strip())
        sk_old = int(lines[1].strip())
        ct_old = ast.literal_eval(lines[2].strip())
        if isinstance(pk_old, tuple) and isinstance(ct_old, (list, tuple)):
            return pk_old, sk_old, ct_old
    except Exception:
        pass

    # --- Format baru (rapi) ---
    m_pub = re.search(
        r"Kunci Publik\s*:\s*\(p=(\d+),\s*g=(\d+),\s*y=(\d+)\)",
        text
    )
    if not m_pub:
        print("❌ Format 'Kunci Publik' tidak ditemukan di ciphertext.txt")
        sys.exit(1)

    p, g, y = map(int, m_pub.groups())
    public_key = (p, g, y)

    m_priv = re.search(r"Kunci Privat\s*:\s*(\d+)", text)
    if not m_priv:
        print("❌ Format 'Kunci Privat' tidak ditemukan di ciphertext.txt")
        sys.exit(1)

    private_key = int(m_priv.group(1))

    ciphertext = []
    try:
        start_idx = next(i for i, ln in enumerate(lines) if "=== HASIL ENKRIPSI ===" in ln)
    except StopIteration:
        print("❌ Bagian '=== HASIL ENKRIPSI ===' tidak ditemukan di ciphertext.txt")
        sys.exit(1)

    for ln in lines[start_idx + 1:]:
        ln = ln.strip()
        if not ln:
            continue

        if re.match(r"^\d{2}\.\s*\(.*\)$", ln):
            pair_str = ln.split(".", 1)[1].strip()
            try:
                pair = ast.literal_eval(pair_str)
                ciphertext.append(pair)
            except Exception:
                pass

    if not ciphertext:
        print("❌ Ciphertext tidak berhasil dibaca dari ciphertext.txt")
        sys.exit(1)

    return public_key, private_key, ciphertext


def main():
    public_key, private_key, ciphertext = load_ciphertext_file()

    decrypted = decrypt(private_key, public_key, ciphertext)

    with open("hasil_dekripsi.txt", "w", encoding="utf-8") as f:
        f.write("=== HASIL DEKRIPSI ELGAMAL ===\n\n")
        f.write(f"Kunci Publik  : {public_key}\n")
        f.write(f"Kunci Privat  : {private_key}\n\n")
        f.write("Ciphertext    :\n")
        for i, pair in enumerate(ciphertext, start=1):
            f.write(f"{i:02d}. {pair}\n")
        f.write("\nPlaintext     : {}\n".format(decrypted))


if __name__ == "__main__":
    main()
