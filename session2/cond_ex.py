# Giai phuong trinh bac hai

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

delta = b ** 2 - 4 * a * c
delta_sqrt = delta**0.5

if delta > 0:
    print("Phuong trinh co 2 nghiem")
    x1 = (-b + delta_sqrt) / (2 * a)
    print("x1 =", x1)
    x2 = (-b - delta_sqrt) / (2 * a)
    print("x2 =", x2)
elif delta == 0:
    print("Phuong trinh co mot nghiem duy nhat")
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Phuong trinh vo nghiem")
