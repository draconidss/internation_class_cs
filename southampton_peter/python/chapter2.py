# mod
print(5.5 // 2)

PI = 3.1415
PI = 1
print("PI:" + str(PI))

# int str bool float
print(f"2 ** 3：{2 ** 3}")

# bool
flag_a = True
flag_b = False
print(f"flag_a and flag_b: {flag_a and flag_b}")  # False
print(f"flag_a and flag_b: {flag_a or flag_b}")  # True
print(f"not flag_b: {not flag_b}")  # True

# use 'is' and 'is not'
x = 25
y = 25
z = 24
a = 500
b = 500
print(f"x is y :{x is y}")  # True
print(f"x is z :{x is z}")  # False
print(f"x is not z :{x is not z}")  # True
print(f"a is b :{a is b}")  # True

# Conversion
print(int("10"))
print(bool(10))

# print
print(0.1 + 0.1)
print(f"type(x): {type(x)}")

# type declare variables
x: int = 4.1
print(x)

balance = 0


def deposit():
    # global balances
    balance = 1
    print(f"inside balance: {balance}")


deposit()
print(f"outer balance: {balance}")
