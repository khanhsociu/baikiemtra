print("Nhap so nguyen duong: ")
while True:
    a = int(input())
    if a<0:
        print("vu long nhap so nguyen duong:")
    else:
        break
giaiThua = 1
for i in range(1, a+1):
    giaiThua = giaiThua * i;
print(a, "! =", giaiThua)