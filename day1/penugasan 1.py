print("=== PERSEGI ===")
sisi = float(input("Masukkan panjang sisi: "))

keliling_persegi = 4 * sisi
luas_persegi = sisi * sisi

print("Keliling Persegi =", keliling_persegi)
print("Luas Persegi =", luas_persegi)


print("\n=== PERSEGI PANJANG ===")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

keliling_pp = 2 * (panjang + lebar)
luas_pp = panjang * lebar

print("Keliling Persegi Panjang =", keliling_pp)
print("Luas Persegi Panjang =", luas_pp)


print("\n=== TRAPESIUM ===")
a = float(input("Masukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
c = float(input("Masukkan sisi miring kiri: "))
d = float(input("Masukkan sisi miring kanan: "))
tinggi = float(input("Masukkan tinggi: "))

keliling_trapesium = a + b + c + d
luas_trapesium = 0.5 * (a + b) * tinggi

print("Keliling Trapesium =", keliling_trapesium)
print("Luas Trapesium =", luas_trapesium)