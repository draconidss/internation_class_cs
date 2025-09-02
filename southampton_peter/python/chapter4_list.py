# len
nums = [9, 6, 1, 4, 2]
print(len(nums))

# slices
shopping_list = ["Apple", "Banana", "Milk", "Bread"]
print(shopping_list[0:3])  # ["Apple", "Banana", "Milk"]
print(shopping_list[3:3])  # []
print(shopping_list[-3:-1])  # ["Banana", "Milk"]
print(shopping_list[:3])  # ["Apple", "Banana", "Milk"]
print(shopping_list[-2:])  # ["Milk", "Bread"]

shopping_list_1 = ["Apple", "Banana", "Milk", "Bread", "Choc", "Eggs"]
print(shopping_list_1[1:5:2])  # ["Banana", "Bread"]
# step is -1
print(shopping_list_1[5:2:-1])  # ["Bread", "Choc", "Eggs"]
print(shopping_list_1[5:2:-2])  # ['Eggs', 'Choc', 'Bread']
print(shopping_list_1[5::-2])  # ['Eggs', 'Bread', 'Banana']
# reverse
print(shopping_list_1[::-1])  # reverse

# list unpacked
a, b, c, d = shopping_list
# wrong
# a,b,c = shopping_list
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
# print(f"d: {d}")

# enumerate
for index, item in enumerate(shopping_list):
    print(f"Index: {index}, Item: {item}")

# range
for index in range(len(shopping_list)):
    print(f"Index: {index}, Upper Item: {shopping_list[index].upper()}")

nums = [num for num in range(1, 100)]
print(nums)

# del
arr = [1, 2, 3]
for index, item in enumerate(arr):
    print(f"index: {index}")
    print(f"arr before del: {arr}")
    del arr[index]
    print(f"arr after del: {arr}")
# No.1，index  = 0, del arr[0] -> arr = [2, 3]
# No.2，index  = 1, del arr[1] -> arr = [2]
# No.3，index  = 2, del arr[2] -> arr = [2]

# arr_1 = [1, 2, 3]
# del arr_1[3]
# print(arr_1)

usernames = ["aaa", "bbb"]
if usernames:
    print("not empty")
else:
    print("not empty")

letter = "h"
if "":
    print("vowel")
else:
    print("consonant")