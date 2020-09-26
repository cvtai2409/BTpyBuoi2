a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
if(a<c+b and b<a+c and c<a+b):
    if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
        print("La Tam Giac Vuong")
    else:
        print("Khong La Tam Giac Vuong")
else:
    print("Khong Phai La Tam Giac")