# dictionary

# create dic
dic_1 = {"a": "b", 10: 1}
dic_2 = dict(a="b", b="a")
print(f"dict_1: {dic_1}")

# insert key-value
alien_0 = {"color": "green", "points": 10}
alien_0["points"] = 5
print(alien_0)

# del key-value
del alien_0["color"]
print(f'del alien_0["color"]: {alien_0}')

# del non-exist key
# del alien_0["non_exist"] # KeyError: 'non_exist'
# print(f"del alien_0[\"non_exist\"]: {alien_0}")

if "points" in alien_0:
    print(f'alien_0 contains key "points"')

if "non_exist_key" in alien_0:
    print(f'alien_0 contains key "non_exist_key"')
else:
    print(f'alien_0 not contains key "non_exist_key"')

fruits = ["apple", "banana", "orange", "blueberry"]
prices = [1.20, 0.50, 0.80, 2.50]
fruits_dict = {}
for index, item in enumerate(fruits):
    fruits_dict[item] = prices[index]
print(f"fruits_dict:", fruits_dict)

fruits_dict = {fruits[index]: prices[index] for index, item in enumerate(fruits)}

a = input("Number: ") # input value is always string
# type compression
inta = int(a) + 1 # notice: the variable a must be a numeric value
print(inta)

MyNumber = 3+2.0
MyName = 'Dusty'
print(MyName, MyNumber)
print('MyName', 'MyNumber')

print((1 + 2) + 1.5)
