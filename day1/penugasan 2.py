import math

# Menghitung volume tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari**2 * tinggi

# Menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Input untuk tabung
r = float(input("Masukkan jari-jari tabung: "))
t_tabung = float(input("Masukkan tinggi tabung: "))

# Input untuk balok
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t_balok = float(input("Masukkan tinggi balok: "))

# Menghitung volume
hasil_tabung = volume_tabung(r, t_tabung)
hasil_balok = volume_balok(p, l, t_balok)

# Output hasil
print("\n=== Hasil Perhitungan ===")
print(f"Volume Tabung = {hasil_tabung:.2f}")
print(f"Volume Balok  = {hasil_balok:.2f}")