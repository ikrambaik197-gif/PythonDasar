 # LuasBangunData_Polimorfisme.py

import math

# Definisi kelas dasar Shape
class Shape:
    def hitung_luas(self):
        # Method abstract (akan diimplementasikan oleh kelas turunan)
        pass

# Definisi kelas turunan Square yang mewarisi dari Shape
class Square(Shape):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

# Definisi kelas turunan Circle yang mewarisi dari Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2

# Definisi kelas turunan Triangle yang mewarisi dari Shape
class Triangle(Shape):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Program utama
if __name__ == "__main__":
    print("="*50)
    print("     PROGRAM MENGHITUNG LUAS BANGUN DATAR")
    print("="*50)
    
    # Membuat objek dari berbagai bentuk
    bentuk1 = Square(5)          # Persegi dengan sisi 5
    bentuk2 = Circle(3)           # Lingkaran dengan radius 3
    bentuk3 = Triangle(4, 6)      # Segitiga dengan alas 4 dan tinggi 6
    
    # Menambahkan beberapa contoh tambahan
    bentuk4 = Square(7)           # Persegi dengan sisi 7
    bentuk5 = Circle(5)           # Lingkaran dengan radius 5
    bentuk6 = Triangle(8, 3)      # Segitiga dengan alas 8 dan tinggi 3
    
    daftar_bentuk = [bentuk1, bentuk2, bentuk3, bentuk4, bentuk5, bentuk6]
    
    print("\nHasil Perhitungan Luas:")
    print("-"*50)
    
    # Demonstrasi polimorfisme
    for i, bentuk in enumerate(daftar_bentuk, 1):
        luas = bentuk.hitung_luas()
        
        # Menentukan jenis bentuk
        if isinstance(bentuk, Square):
            jenis = "Persegi"
            info = f"sisi = {bentuk.sisi}"
        elif isinstance(bentuk, Circle):
            jenis = "Lingkaran"
            info = f"radius = {bentuk.radius}"
        elif isinstance(bentuk, Triangle):
            jenis = "Segitiga"
            info = f"alas = {bentuk.alas}, tinggi = {bentuk.tinggi}"
        else:
            jenis = "Tidak Diketahui"
            info = ""
        
        print(f"{i}. {jenis:<10} ({info:<15}) : luas = {luas:.2f}")
    
    print("-"*50)
    
    # Demonstrasi konsep polimorfisme
    print("\n" + "="*50)
    print("     DEMONSTRASI POLIMORFISME")
    print("="*50)
    
    print("""
Polimorfisme adalah konsep di mana objek dari kelas yang berbeda
dapat dipanggil dengan method yang sama, tetapi menghasilkan perilaku
yang berbeda sesuai dengan kelasnya masing-masing.

Dalam program ini:
- Semua objek (Square, Circle, Triangle) adalah turunan dari class Shape
- Masing-masing memiliki method hitung_luas() dengan implementasi berbeda
- Method yang sama (hitung_luas()) dipanggil untuk setiap objek
- Hasilnya berbeda-beda sesuai dengan rumus luas masing-masing bangun
    """)
    
    # Menampilkan hubungan inheritance
    print("\nHubungan Inheritance:")
    print(f"Square merupakan turunan dari Shape: {issubclass(Square, Shape)}")
    print(f"Circle merupakan turunan dari Shape: {issubclass(Circle, Shape)}")
    print(f"Triangle merupakan turunan dari Shape: {issubclass(Triangle, Shape)}")