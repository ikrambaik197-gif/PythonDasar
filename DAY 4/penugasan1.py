import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = float(entry_kuantitas.get())
        total = harga * kuantitas
        label_total.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

tk.Label(root, text="Harga:").pack(pady=5)
entry_harga = tk.Entry(root)
entry_harga.pack()

tk.Label(root, text="Kuantitas:").pack(pady=5)
entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack()

tk.Button(root, text="Hitung Total", command=hitung_total).pack(pady=15)

label_total = tk.Label(root, text="Total: Rp.0.00", font=("Arial", 12, "bold"))
label_total.pack()

root.mainloop()