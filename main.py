import random

print("Selamat datang di permainan Tebak Angka!")
print("Saya telah memilih sebuah angka antara 1 dan 100.")
print("Bisakah kamu menebaknya?")

# Pilih angka acak antara 1 dan 100
angka_rahasia = random.randint(1, 100)
tebakan = 0
percobaan = 0

# Loop utama permainan
while tebakan != angka_rahasia:
    try:
        tebakan = int(input("Masukkan tebakanmu (1-100): "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan!")
    except ValueError:
        print("Mohon masukkan angka yang valid.")

print("Terima kasih telah bermain!")
