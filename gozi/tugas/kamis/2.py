import tkinter as tk
from datetime import datetime

def cari_nopol():
    nopol_dicari = entry_nopol.get()
    hasil_pencarian.config(text=f"Hasil Pencarian untuk {nopol_dicari}: Informasi Parkir")

def hitung_biaya():
    waktu_masuk = entry_masuk.get()
    waktu_keluar = entry_keluar.get()

    try:
        waktu_masuk = datetime.strptime(waktu_masuk, "%H:%M")
        waktu_keluar = datetime.strptime(waktu_keluar, "%H:%M")

        selisih = waktu_keluar - waktu_masuk

        tarif_per_jam = 5000
        biaya_parkir = (selisih.total_seconds() / 3600) * tarif_per_jam

        label_biaya.config(text=f"Biaya Parkir: Rp {biaya_parkir:.2f}")

        nopol = entry_nopol.get()
        informasi_parkir = f"Nomor Plat: {nopol}, Masuk: {waktu_masuk.strftime('%H:%M')}, Keluar: {waktu_keluar.strftime('%H:%M')}, Biaya: Rp {biaya_parkir:.2f}"
        tambah_pelanggan(informasi_parkir)
    except ValueError:
        label_biaya.config(text="Format waktu salah")

def tambah_pelanggan(info_parkir):
    daftar_pelanggan.insert(tk.END, info_parkir)

root = tk.Tk()
root.title("Program Parkir")


label_judul = tk.Label(root, text="GOZI PARKIR", font=("Arial", 18, "bold", ))
label_judul.pack()


label_nopol = tk.Label(root, text="Cari Nomor Plat Polisi:")
label_nopol.pack()
entry_nopol = tk.Entry(root)
entry_nopol.pack()


button_cari = tk.Button(root, text="Cari Nopol", command=cari_nopol)
button_cari.pack()


hasil_pencarian = tk.Label(root, text="")
hasil_pencarian.pack()


label_masuk = tk.Label(root, text="Waktu Masuk (HH:MM):")
label_masuk.pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

label_keluar = tk.Label(root, text="Waktu Keluar (HH:MM):")
label_keluar.pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

button_hitung = tk.Button(root, text="Hitung Biaya Parkir", command=hitung_biaya)
button_hitung.pack()

label_biaya = tk.Label(root, text="Biaya Parkir: Rp 0.00")
label_biaya.pack()

daftar_pelanggan = tk.Listbox(root, height=10, width=100)
daftar_pelanggan.pack()

button_tambah_pelanggan = tk.Button(root, text="Tambah Pelanggan", command=tambah_pelanggan)
button_tambah_pelanggan.pack()

# Menjalankan aplikasi
root.mainloop()