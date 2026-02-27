from PIL import Image

# Nama file gambar asli
input_file = "logo.jpg"   # ganti sesuai nama file kamu
output_file = "logo_edit.jpg"

try:
    # Membuka gambar
    img = Image.open(input_file)
    print("Gambar berhasil dibuka.")

    # Menampilkan ukuran asli
    print("Ukuran asli:", img.size)

    # Resize gambar (misal jadi 300x300)
    img_resize = img.resize((300, 300))

    # Ubah ke grayscale
    img_gray = img_resize.convert("L")

    # Simpan hasil
    img_gray.save(output_file)

    print("Gambar berhasil diubah dan disimpan sebagai", output_file)