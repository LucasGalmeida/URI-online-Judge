NAME = input()
SALARY = float(input())
SOLD = float(input())
SOLD = SOLD * 15 / 100
print("TOTAL = R$ {:.2f}".format(SALARY + SOLD))
