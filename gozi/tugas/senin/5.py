tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end="")
    
    print()