import tkinter as tk
from tkinter import ttk

def hitung_total():
    harga = float(harga_entry.get())
    kuantitas = int(kuantitas_entry.get())
    total = harga * kuantitas
    total_label.config(text=f"Total: Rp {total:,.2f}")

window = tk.Tk()
window.title("Program Kasir")


input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

harga_label = ttk.Label(input_frame, text="Harga:")
harga_label.grid(row=0, column=0, sticky="W")
harga_entry = ttk.Entry(input_frame)
harga_entry.grid(row=0, column=1)

kuantitas_label = ttk.Label(input_frame, text="Kuantitas:")
kuantitas_label.grid(row=1, column=0, sticky="W")
kuantitas_entry = ttk.Entry(input_frame)
kuantitas_entry.grid(row=1, column=1)

hitung_button = ttk.Button(window, text="Hitung Total", command=hitung_total)
hitung_button.pack(pady=10)

total_label = ttk.Label(window, text="")
total_label.pack()

window.mainloop()