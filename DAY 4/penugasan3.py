import tkinter as tk
from tkinter import messagebox

# Membuat window utama
root = tk.Tk()
root.title("Data Siswa Baru")
root.geometry("600x650")
root.configure(bg="#d9d9d9")

# ====== HEADER ======
header = tk.Label(root, text="DATA SISWA BARU",
                  font=("Arial", 20, "bold"),
                  bg="#8fd3d4", fg="black",
                  pady=15)
header.pack(fill="x")

# ====== FRAME FORM ======
frame = tk.Frame(root, bg="#d9d9d9", padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Fungsi membuat label + entry
def create_field(label_text, row):
    label = tk.Label(frame, text=label_text, font=("Arial", 11),
                     bg="#d9d9d9", anchor="w")
    label.grid(row=row, column=0, sticky="w", pady=8)

    entry = tk.Entry(frame, font=("Arial", 11), width=50)
    entry.grid(row=row, column=1, pady=8)
    return entry

# Membuat field input
nama = create_field("Nama Lengkap", 0)
tanggal = create_field("Tanggal Lahir", 1)
asal = create_field("Asal Sekolah", 2)
nisn = create_field("NISN", 3)
ayah = create_field("Nama Ayah", 4)
ibu = create_field("Nama Ibu", 5)
telepon = create_field("Nomor Telepon / HP", 6)

# ====== ALAMAT (TEXT AREA) ======
label_alamat = tk.Label(frame, text="Alamat",
                        font=("Arial", 11),
                        bg="#d9d9d9", anchor="w")
label_alamat.grid(row=7, column=0, sticky="nw", pady=8)

alamat = tk.Text(frame, width=38, height=6, font=("Arial", 11))
alamat.grid(row=7, column=1, pady=8)

# ====== FUNGSI TOMBOL ======
def simpan_data():
    data = f"""
    Nama: {nama.get()}
    Tanggal Lahir: {tanggal.get()}
    Asal Sekolah: {asal.get()}
    NISN: {nisn.get()}
    Nama Ayah: {ayah.get()}
    Nama Ibu: {ibu.get()}
    Telepon: {telepon.get()}
    Alamat: {alamat.get("1.0", tk.END)}
    """

    messagebox.showinfo("Data Tersimpan", "Data siswa berhasil disimpan!")

def hapus_data():
    nama.delete(0, tk.END)
    tanggal.delete(0, tk.END)
    asal.delete(0, tk.END)
    nisn.delete(0, tk.END)
    ayah.delete(0, tk.END)
    ibu.delete(0, tk.END)
    telepon.delete(0, tk.END)
    alamat.delete("1.0", tk.END)

# ====== FRAME TOMBOL ======
frame_tombol = tk.Frame(root, bg="#8fd3d4", pady=15)
frame_tombol.pack(fill="x")

btn_hapus = tk.Button(frame_tombol, text="Hapus",
                      width=12, bg="#c76d4a", fg="white",
                      font=("Arial", 11, "bold"),
                      command=hapus_data)
btn_hapus.pack(side="right", padx=10)

btn_simpan = tk.Button(frame_tombol, text="Simpan",
                       width=12, bg="#c76d4a", fg="white",
                       font=("Arial", 11, "bold"),
                       command=simpan_data)
btn_simpan.pack(side="right")

# Menjalankan program
root.mainloop()