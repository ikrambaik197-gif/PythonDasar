tinggi = int(input("Masukkan tinggi piramida: "))

for i in range(tinggi):
    # Spasi
    for j in range(tinggi - i - 1):
        print(" ", end="")
    
    # Bintang
    for k in range(2 * i + 1):
        print("*", end="")
    
    print()