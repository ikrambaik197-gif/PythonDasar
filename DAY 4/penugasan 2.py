import tkinter as tk
from tkinter import ttk
from datetime import datetime

BIAYA_PER_JAM = 2000

data_parkir = []

def hitung_biaya():
    try:
        jam_masuk = datetime.strptime(entry_masuk.get(), "%H:%M")
        jam_keluar = datetime.strptime(entry_keluar.get(), "%H:%M")

        selisih = jam_keluar - jam_masuk
        jam = selisih.seconds // 3600
        if selisih.seconds % 3600 != 0:
            jam += 1

        total = jam * BIAYA_PER_JAM
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(total))

        simpan_data(total)

    except:
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, "Format HH:MM")

def simpan_data(total):
    plat = entry_plat.get()
    masuk = entry_masuk.get()
    keluar = entry_keluar.get()

    data = (plat, masuk, keluar, total)
    data_parkir.append(data)

    tree_terakhir.insert("", "end", values=data)

    # Urutkan berdasarkan biaya terbesar
    sorted_data = sorted(data_parkir, key=lambda x: x[3], reverse=True)
    tree_terbanyak.delete(*tree_terbanyak.get_children())
    for item in sorted_data:
        tree_terbanyak.insert("", "end", values=item)

def cari_data():
    keyword = entry_cari.get()
    for item in tree_terakhir.get_children():
        values = tree_terakhir.item(item)["values"]
        if keyword in values[0]:
            tree_terakhir.selection_set(item)
            break

# ================= GUI =================
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("900x500")

# Frame kiri
frame_kiri = tk.Frame(root)
frame_kiri.pack(side="left", padx=10, pady=10)

tk.Label(frame_kiri, text="Cari NoPol").grid(row=0, column=0, sticky="w")
entry_cari = tk.Entry(frame_kiri)
entry_cari.grid(row=0, column=1)
tk.Button(frame_kiri, text="Cari", command=cari_data).grid(row=0, column=2)

tk.Label(frame_kiri, text="No Plat Polisi").grid(row=1, column=0, sticky="w")
entry_plat = tk.Entry(frame_kiri)
entry_plat.grid(row=1, column=1)

tk.Label(frame_kiri, text="Waktu Masuk (HH:MM)").grid(row=2, column=0, sticky="w")
entry_masuk = tk.Entry(frame_kiri)
entry_masuk.grid(row=2, column=1)

tk.Label(frame_kiri, text="Waktu Keluar (HH:MM)").grid(row=3, column=0, sticky="w")
entry_keluar = tk.Entry(frame_kiri)
entry_keluar.grid(row=3, column=1)

tk.Label(frame_kiri, text="Biaya").grid(row=4, column=0, sticky="w")
entry_biaya = tk.Entry(frame_kiri)
entry_biaya.grid(row=4, column=1)

tk.Button(frame_kiri, text="Hitung", command=hitung_biaya).grid(row=4, column=2)

# Frame kanan (Biaya besar)
frame_kanan = tk.Frame(root)
frame_kanan.pack(side="right", padx=20)

tk.Label(frame_kanan, text="Biaya Per Jam", fg="red", font=("Arial", 20)).pack()
tk.Label(frame_kanan, text="Rp. 2.000", fg="red", font=("Arial", 32, "bold")).pack()

# ================= TABEL =================
frame_bawah = tk.Frame(root)
frame_bawah.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("plat", "masuk", "keluar", "biaya")

# List Terakhir Keluar
tk.Label(frame_bawah, text="List Pelanggan Urut Terakhir Keluar", fg="blue").grid(row=0, column=0)

tree_terakhir = ttk.Treeview(frame_bawah, columns=columns, show="headings", height=8)
for col in columns:
    tree_terakhir.heading(col, text=col.capitalize())
tree_terakhir.grid(row=1, column=0, padx=10)

# List Banyak Bayar
tk.Label(frame_bawah, text="List Pelanggan Banyak Bayar", fg="blue").grid(row=0, column=1)

tree_terbanyak = ttk.Treeview(frame_bawah, columns=columns, show="headings", height=8)
for col in columns:
    tree_terbanyak.heading(col, text=col.capitalize())
tree_terbanyak.grid(row=1, column=1, padx=10)

root.mainloop()