while True:
    nilai_siswa = int(input("Masukkan nilai siswa: "))

    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        mengulang = input("Nilai kurang dari 75. Apakah ingin mengulang? (Ya/Tidak): ")

        if mengulang.lower() == "ya":
            continue
        else:
            print("Tidak Tuntas")
            break

print("Program selesai")