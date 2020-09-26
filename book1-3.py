n = int(input("Nhap N la so nguyen duong [1->1000]: "))
while(n>999 or n < 0):
    n = int(input("Nhap lai N la so nguyen duong [1->1000]: "))
total = 0
while(n>0):
    total += n%10
    n = int(n/10)

print(total)
