def add(x,y): # khai bao cua funtion
    r = x+y
    return r # cho r thoat ra khoi def

def eval(x, y, op):
    # x = int(input("x = "))
    # y = int(input("y = "))
    if op == "+":
        r = x+y # return x+y
    elif op == "-":
        r = x-y
    elif op == "*":
        r = x*y
    elif op == "/":
        r = x/y

    return r # tra ve ket qua hoac dung chuong trinh
print(eval(9, 10, "-"))

    

# a = int(input("a = "))
# b = int(input("b = "))
# t = add(a, b)
# print(t)