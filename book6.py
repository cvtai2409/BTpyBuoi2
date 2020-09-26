N = int(input("Nhap N: "))
Tong = 0
for i in range (1, N+1):
    if(i == 17):
        continue
    Tong = Tong + i
print(f"Tong la: {Tong}")