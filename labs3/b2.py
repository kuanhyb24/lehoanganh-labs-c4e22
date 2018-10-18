from calc import eval, add

x = int(input("nhap x: "))
y = int(input("nhap y: "))
op = str(input("nhap phep toan (+, -, /, *): "))

r = eval(x, y, op)

print(x, op, y, "=", r)