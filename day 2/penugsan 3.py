 # Definisi kelas dasar Vehicle
class Vehicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Warna: {self.warna}")

# Definisi kelas turunan Car yang mewarisi dari Vehicle
class Car(Vehicle):
    def __init__(self, merk, tahun, warna, model):
        # Panggil konstruktor kelas dasar
        super().__init__(merk, tahun, warna)
        self.model = model

    def tampilkan_info(self):
        # Panggil metode kelas dasar untuk menampilkan info kendaraan
        super().tampilkan_info()
        print(f"Model: {self.model}")

# Program utama
if __name__ == "__main__":
    print("="*40)
    print("     PROGRAM INFORMASI KENDARAAN")
    print("="*40)
    
    # Membuat objek Car dengan data spesifik
    car = Car("Toyota", 2022, "Merah", "Camry")
    
    print("\nInfo Kendaraan:")
    print("-"*20)
    car.tampilkan_info()
    
    # Contoh tambahan untuk mendemonstrasikan inheritance
    print("\n" + "="*40)
    print("     CONTOH TAMBAHAN")
    print("="*40)
    
    # Membuat beberapa objek Car lainnya
    car2 = Car("Honda", 2023, "Hitam", "Civic")
    car3 = Car("Suzuki", 2021, "Putih", "Ertiga")
    
    print("\nInfo Kendaraan 2:")
    print("-"*20)
    car2.tampilkan_info()
    
    print("\nInfo Kendaraan 3:")
    print("-"*20)
    car3.tampilkan_info()
    
    # Demonstrasi polimorfisme
    print("\n" + "="*40)
    print("     DEMONSTRASI INHERITANCE")
    print("="*40)
    
    # Membuat list kendaraan
    kendaraan = [car, car2, car3]
    
    print("\nDaftar Semua Kendaraan:")
    print("-"*30)
    for i, k in enumerate(kendaraan, 1):
        print(f"\nKendaraan ke-{i}:")
        k.tampilkan_info()
    
    # Menampilkan informasi tentang inheritance
    print("\n" + "="*40)
    print("     INFORMASI INHERITANCE")
    print("="*40)
    print(f"Class Car merupakan turunan dari class Vehicle: {issubclass(Car, Vehicle)}")
    print(f"Objek car adalah instance dari class Car: {isinstance(car, Car)}")
    print(f"Objek car juga merupakan instance dari class Vehicle: {isinstance(car, Vehicle)}")