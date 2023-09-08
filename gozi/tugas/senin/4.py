tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    for j in range(tinggi - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()