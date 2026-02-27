nama = input("Masukkan Nama: ")
gaji_pokok = float(input("Masukkan Gaji Pokok: "))

# Proses perhitungan
tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print("\n=== HASIL PERHITUNGAN GAJI ===")
print("Nama        :", nama)
print("Gaji Pokok  :", gaji_pokok)
print("Gaji Bersih :", gaji_bersih)