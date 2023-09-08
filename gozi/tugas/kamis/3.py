import PySimpleGUI as sg

layout = [
    [sg.Text("DATA SISWA BARU")],
    [sg.Text("Nama Lengkap"), sg.InputText(key="Nama")],
    [sg.Text("Tanggal Lahir"), sg.InputText(key="Tanggal Lahir")],
    [sg.Text("Asal Sekolah"), sg.InputText(key="Asal Sekolah")],
    [sg.Text("NISN"), sg.InputText(key="NISN")],
    [sg.Text("Nama Ayah"), sg.InputText(key="Nama Ayah")],
    [sg.Text("Nama Ibu"), sg.InputText(key="Nama Ibu")],
    [sg.Text("Nomor Telepon"), sg.InputText(key="Nomor Telepon")],
    [sg.Text("Alamat"), sg.InputText(key="Alamat")],
    [sg.Button("Hapus"), sg.Button("Simpan")],
]

window = sg.Window("Program Data Siswa Baru", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Hapus":
        for key in values.keys():
            window[key].update('')
    elif event == "Simpan":
        with open("data_siswa.txt", "a") as file:
            file.write(f"Nama: {values['Nama']}\n")
            file.write(f"Tanggal Lahir: {values['Tanggal Lahir']}\n")
            file.write(f"Asal Sekolah: {values['Asal Sekolah']}\n")
            file.write(f"NISN: {values['NISN']}\n")
            file.write(f"Nama Ayah: {values['Nama Ayah']}\n")
            file.write(f"Nama Ibu: {values['Nama Ibu']}\n")
            file.write(f"Nomor Telepon: {values['Nomor Telepon']}\n")
            file.write(f"Alamat: {values['Alamat']}\n\n")
        sg.popup("Data Siswa tersimpan!")

window.close()