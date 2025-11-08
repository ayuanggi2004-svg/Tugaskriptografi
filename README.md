🔐 ElGamal Cryptosystem — Implementasi Algoritma Kriptografi Kunci Publik

Proyek ini merupakan implementasi **algoritma kriptografi kunci publik ElGamal** menggunakan bahasa pemrograman **Python**.
ElGamal adalah algoritma kriptografi asimetris yang menggunakan **dua kunci berbeda**, yaitu *kunci publik* untuk enkripsi dan *kunci privat* untuk dekripsi. 
Algoritma ini didasarkan pada konsep **logaritma diskrit** dalam aritmetika modulo bilangan prima. 
Proyek ini dibuat sebagai bagian dari tugas mata kuliah *Kriptografi*, dengan tujuan memahami proses pembangkitan kunci, enkripsi, dan dekripsi pada algoritma kunci publik

⚙️ Fitur Program
- 🔑 **Pembuatan Kunci Otomatis** — menghasilkan kunci publik & privat secara acak  
- 🧩 **Enkripsi Pesan** — mengenkripsi teks menggunakan kunci publik  
- 🔓 **Dekripsi Pesan** — mendekripsi ciphertext menggunakan kunci privat  
- 💾 **Penyimpanan Otomatis** — hasil enkripsi dan dekripsi disimpan dalam file `.txt`  
- 🧠 **Struktur Modular** — fungsi utama dipisahkan menjadi beberapa file (modular)  
- ⏱️ *(Opsional)* Pengukuran waktu proses enkripsi dan dekripsi

📁 Struktur Folder
ElGamal_Project/
│
├── elgamal.py → Implementasi algoritma ElGamal (inti)
├── encrypt_elgamal.py → Program untuk enkripsi teks
├── decrypt_elgamal.py → Program untuk dekripsi ciphertext
├── utils.py → Fungsi bantu (opsional)
├── ciphertext.txt → Hasil enkripsi (otomatis disimpan)
├── hasil_dekripsi.txt → Hasil dekripsi (otomatis disimpan)
└── README.md → Dokumentasi proyek

🧠 Cara Menjalankan Program
1. Pastikan **Python 3.10+** sudah terinstal di komputer.  
2. Buka terminal (CMD / PowerShell / VSCode Terminal) pada folder proyek.  
3. Untuk melakukan **enkripsi**, jalankan perintah berikut:

   ```bash
   python encrypt_elgamal.py
4. Masukkan teks yang ingin dienkripsi.
5. Program akan menghasilkan pasangan (a, b) ciphertext dan menyimpannya di ciphertext.txt.
6. Untuk melakukan dekripsi, jalankan:
     python decrypt_elgamal.py

Pastikan file ciphertext.txt ada di folder yang sama.
Program akan membaca ciphertext dan menampilkan hasil plaintext di terminal serta menyimpannya ke hasil_dekripsi.txt.
