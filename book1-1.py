a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
import math
if a == 0:
    if b == 0:
        if c == 0:
            print("Phu9ong trinh vo so nghiem!")
        else:
            print("phuong trinh vo nghiem!")
    else:
        if c == 0:
            print("Phuong trinh co 1 nghiem x = 0")
        else:
            print("Phuong trinh co 1 nghiem x = ", -c / b)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("phuong trinh vo nghiem!")
    elif delta == 0:
        print("Phuong trinh co 1 nghiem x = ", -b / (2 * a))
    else:
        print("Phuong trinh co 2 nghiem phan biet!")
        print("x1 = ", float((-b - math.sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + math.sqrt(delta)) / (2 * a)))