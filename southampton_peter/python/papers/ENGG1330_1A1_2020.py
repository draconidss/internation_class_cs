a = "The University of Hong Kong"
print(a[:-13:-2].upper())

i = 4.0
print(17 // i, 17.0 / 4, 18 // 7, 18.0 // 7)

i = 42
b = i <= 44 and i * 2 > 100 or i * 3 > 100
print(b)

a = []
a = a + [1, 2]
a = [1, 2] + a
a = a + [2, 2] + a
del a[0]
a.insert(3, 3)
for e in reversed(a):
    print(e * 2)


def r(p):
    print(p, end="")
    if p < 8:
        r(p + 1)
        p = p + 1
        print(p, end="")


r(5)
print("my height is %.2f, my weight is %d" % (180, 100))
heig = input
print(f"my height is {input("height: ")}, my weight is {input("weight: ")}")

import math

print(
    "**********************************************\n**** WELCOME TO ENGG1330 AREA OF TRIANGLE ****\n**********************************************"
)
choice = 0
while choice != 1:
    print("1. Exit")
    print("2. Area of Triangle 1")
    print("3. Area of Triangle 2")
    print("4. Area of Triangle 3")
    choice = int(input("Your choice: "))
    if choice == 2:
        base = int(input("Base: "))
        height = int(input("Height: "))
        area = base * height / 2
        print(f"The area is {area}.")
    elif choice == 3:
        A = int(input("A: "))
        B = int(input("B: "))
        Gamma = int(input("Gamma: "))
        area = 0.5 * A * B * math.sin(Gamma)
        print(f"The area is {area}.")
    elif choice == 4:
        A = int(input("A: "))
        B = int(input("B: "))
        C = int(input("C: "))
        p = (A + B + C) / 2
        area = math.sqrt(p * (p - A) * (p - B) * (p - C))
        print(f"The area is {area}.")
print("Bye Bye!")
