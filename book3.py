N = int(input("Nhap N: "))
TongL = 0
for i in range (1, N+1):
    if (i % 2 != 0):
        TongL = TongL + i
print(f"Tong le la: {TongL}")