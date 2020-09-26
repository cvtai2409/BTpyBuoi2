N = int(input("Nhap N: "))
TongC = 0
for i in range (1, N+1):
    if (i % 2 == 0):
        TongC = TongC + i
print(f"Tong chan la: {TongC}")