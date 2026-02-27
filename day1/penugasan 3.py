ganjil = 0
genap = 0

for i in range(1, 101):
    if i % 2 == 0:
        genap += 1
        print(f"{i} adalah bilangan genap")
    else:
        ganjil += 1
        print(f"{i} adalah bilangan ganjil")

print("\nTotal bilangan genap:", genap)
print("Total bilangan ganjil:", ganjil)