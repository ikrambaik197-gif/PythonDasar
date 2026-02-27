 # dataSiswa_ClassObjek.py
# Definisi kelas Contact
class Contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Telepon: {self.nomor_telepon}")
        print(f"Email: {self.email}")
        print()

# Definisi kelas AddressBook untuk mengelola daftar kontak
class AddressBook:
    def __init__(self):
        # Perbaikan: menggunakan list, bukan dictionary karena method append() digunakan
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)
        print(f"Kontak '{kontak.nama}' berhasil ditambahkan!")

    def tampilkan_semua_kontak(self):
        if not self.daftar_kontak:
            print("Belum ada kontak yang tersimpan.")
            return
        
        print("\n" + "="*40)
        print("           DAFTAR KONTAK")
        print("="*40)
        for i, kontak in enumerate(self.daftar_kontak, 1):
            print(f"Kontak ke-{i}:")
            kontak.tampilkan_info()

# Program utama
if __name__ == "__main__":
    address_book = AddressBook()
    
    print("=== PROGRAM MANAJEMEN KONTAK ===")
    print("Selamat datang di Aplikasi Address Book")
    
    while True:
        print("\n" + "-"*30)
        print("Menu Utama:")
        print("1. Tambah Kontak")
        print("2. Tampilkan Semua Kontak")
        print("3. Keluar")
        print("-"*30)
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\n--- TAMBAH KONTAK BARU ---")
            nama = input("Nama: ")
            nomor_telepon = input("Nomor Telepon: ")
            email = input("Email: ")
            
            # Validasi input sederhana
            if nama and nomor_telepon and email:
                kontak_baru = Contact(nama, nomor_telepon, email)
                address_book.tambah_kontak(kontak_baru)
            else:
                print("Semua field harus diisi!")

        elif pilihan == "2":
            address_book.tampilkan_semua_kontak()

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar (1/2/3).")