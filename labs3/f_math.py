from random import randint, choice
from calc import eval

def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice(['+','-','*','/'])
# if op == "+":
#    r = x+y
# elif op == "-":
#     r = x-y
# elif op == "*":
#     r = x*y
# elif op =="/":
#     r = x/y
# else:
#     print("invalid operators")
    error = randint(-1, 1)
    r = eval(x, y, op) + error
    return [x, y, op, r]
quiz = generate_quiz()
# quiz = [x, y, op, r]
x = quiz[0]
y = quiz[1]
op = quiz[2]
r = quiz[3]

output = "{0} {3} {1} = {2}".format(x, y, r, op)
print(output)
user_answer = input("Y/N ?").upper()
if r == eval(x, y, op):
    if user_answer == "Y":
        print("True")
    else:
        print("False")
else:
    if user_answer == "N":
        print("True")
    else:
        print("False")
    
    