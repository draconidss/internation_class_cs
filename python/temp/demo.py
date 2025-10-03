for i in range(5):  # i is in range [0,4]
    print(f"No {i} iteration：{i}")

print("====")

for i in range(1, 5):  # 1 is start, 5 is end, i is in range [1,4]
    print(f"No {i} iteration：{i}")

print("====")

# 1 is start
# 5 is end, exclusive
# 2 is step
# i is 1, 3
for i in range(1, 5, 2):
    print(f"No {i} iteration：{i}")

for i in range(1):  # i
    for j in range(1):  # i.xx
        for k in range(3):  # i.j.xx
            # 2 * 2 * 2 times
            print(f"Draco i: {i}, j:{j}, k:{k}")

print("11111\r")  # 11111

a = "123"
b = 456
c = a + str(b)
d = int(c)
print("d + 1:", d + 1)

a = 0.1
b = 0.1
print(a + b == 0.2)  # True
print("a * b = ", a * b == 0.01)  # False
print(0.2 + 0.1 == 0.3)
print(abs(1e-10 + 1e-10 - 2e-10 + 1e-20) < 1e-20)
print("=======")

print("01 \n 02 \t\r\t\n 03\t 04 \t\n 05 \n")
print("=======")
print("01 \t 02 \t\t\n 03 \t 04 \t\n 05 \n")
print("=======")
print("01 \t 02 \n 03 \t 04 \t\t\n 05 \n")
print("=======")
print("01\t 02 \t\t\n 03 \t\t 04 \t\n 05")

s_1 = "stringri"
print(f"s_1.find(): {s_1.find("ri")}")

# print(abs(a + b - 2e-10) < 1e-15)

flag = True
flag_2 = False
num_1 = 10
num_2 = 20
print(num_1 < num_2)
print(f"True and False: {True and False}")  # False
print(f"True and True: {True and True}")  # True
print(f"False and True: {False and True}")  # False
print(f"False and False: {False and False}")  # False

# and or not
# True and False

print(f"not False: {not False}") # True
print(f"not True: {not True}") # False
