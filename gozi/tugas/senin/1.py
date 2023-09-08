def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling


def hitung_trapesium(panjang_atas, panjang_bawah, tinggi, sisi_miring):
    luas = 0.5 * (panjang_atas + panjang_bawah) * tinggi
    keliling = panjang_atas + panjang_bawah + (2 * sisi_miring)
    return luas, keliling


jenis_bangun_datar = input("Masukkan jenis bangun datar (persegi, persegi panjang, trapesium): ")

if jenis_bangun_datar == "persegi":
    sisi = float(input("Masukkan panjang sisi: "))
    luas, keliling = hitung_persegi(sisi)
elif jenis_bangun_datar == "persegi panjang":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas, keliling = hitung_persegi_panjang(panjang, lebar)
elif jenis_bangun_datar == "trapesium":
    panjang_atas = float(input("Masukkan panjang sisi atas: "))
    panjang_bawah = float(input("Masukkan panjang sisi bawah: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi_miring = float(input("Masukkan panjang sisi miring: "))
    luas, keliling = hitung_trapesium(panjang_atas, panjang_bawah, tinggi, sisi_miring)
else:
    print("Jenis bangun datar tidak valid")

print(f"Luas {jenis_bangun_datar} adalah: {luas}")
print(f"Keliling {jenis_bangun_datar} adalah: {keliling}")