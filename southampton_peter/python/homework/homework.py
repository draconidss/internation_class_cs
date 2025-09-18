print("\n=============演示代码练习3.1  姓名=============")
names = ["a", "b", "c"]
print(names[0])
print(names[1])
print(names[2])

print("\n=============演示代码练习3.2  问候语=============")
names = ["a", "b", "c"]
message = f"Hello,{names[0].title()}!"
print(message)
message = f"Hello,{names[1].title()}!"
print(message)
message = f"Hello,{names[2].title()}!"
print(message)

print("\n=============演示代码练习3.4  嘉宾名单 =============")
guests = ["a", "b", "c"]
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)

print("\n=============演示代码练习3.5  修改嘉宾名单=============")
guests = ["a", "b", "c"]
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
print(f"{guests[0].title()} cannot enjoy the dinner.")
del guests[0]
guests.insert(0, "d")
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"

print("\n=============演示代码练习3.6  添加嘉宾=============")
guests = ["a", "b", "c"]
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
print(f"{guests[0].title()} cannot enjoy the dinner.")
del guests[0]
guests.insert(0, "d")
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print("We find a bigger table!")
guests.insert(1, "e")
guests.insert(2, "f")
guests.append("g")
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[3].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[4].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[5].title()}, I want to enjoy the dinner with you!"
print(message)

print("\n=============演示代码练习3.7  缩短名单=============")
guests = ["a", "b", "c"]
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
print(f"{guests[0].title()} cannot enjoy the dinner.")
del guests[0]
guests.insert(0, "d")
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print("We find a bigger table!")
guests.insert(1, "e")
guests.insert(2, "f")
guests.append("g")
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[3].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[4].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[5].title()}, I want to enjoy the dinner with you!"
print(message)
print("Sorry, we can only invite two people to enjoy the dinner!")
name = guests.pop()
print(f"Sorry {name.title()}, we have no space inviting you to have the dinner.")
name = guests.pop()
print(f"Sorry {name.title()}, we have no space inviting you to have the dinner.")
name = guests.pop()
print(f"Sorry {name.title()}, we have no space inviting you to have the dinner.")
name = guests.pop()
print(f"Sorry {name.title()}, we have no space inviting you to have the dinner.")
name = guests[0].title()
print(f"{name.title()}, I want to have the dinner with you.")
name = guests[1].title()
print(f"{name.title()}, I want to have the dinner with you.")
del guests[0]
del guests[0]
print(guests)

print("\n=============演示代码练习3.8  放眼世界=============")
places = ["d", "a", "t", "h", "y"]

print("Original list:", places)

print("Alphabetical order:", sorted(places))

print("Original list:", places)

print("Reverse alphabetical order:", sorted(places, reverse=True))

print("Original list:", places)

places.reverse()
print("List after reverse():", places)

places.reverse()
print("List after reversing:", places)

places.sort()
print("List after sort():", places)

places.sort(reverse=True)
print("List after sort(reverse=True):", places)

print("\n=============演示代码练习4.6  奇数=============")
odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)

print("\n=============演示代码练习4.7  3的倍数=============")
nums = list(range(3, 31, 3))
for number in nums:
    print(number)

print("\n=============演示代码练习4.8  立方=============")
nums = []
for number in range(1, 11):
    num = number**3
    nums.append(num)
for numbers in nums:
    print(numbers)

print("\n=============演示代码练习4.9  立方推导式=============")
nums = [num**3 for number in range(1, 11)]
for numbers in nums:
    print(numbers)

print("\n=============演示代码练习4.11  你的比萨，我的比萨=============")
pizzas = ["a", "b", "c"]
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append("d")
friend_pizzas.append("e")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print("\n=============演示代码练习4.13  自助餐=============")
foods = ("a", "b", "c", "d", "e")
for food in foods:
    print(food)
foods = ("x", "y", "c", "d", "e")
for food in foods:
    print(food)

print("\n=============演示代码练习5.3  外星人颜色1=============")
alien_color = "green"
if alien_color == "green":
    print("You got 5 points!")

print("\n=============演示代码练习5.4  外星人颜色2=============")
alien_color = "green"
if alien_color == "green":
    print("You got 5 points!")
else:
    print("You got 10 points!")

print("\n=============演示代码练习5.5  外星人颜色3=============")
alien_color = "green"
if alien_color == "green":
    print("You got 5 points!")
elif alien_color == "yellow":
    print("You got 10 points!")
else:
    print("You got 15 points!")

print("\n=============演示代码练习5.6  人生的不同阶段=============")
age = 20
if age < 2:
    print("This is a baby.")
elif age < 4:
    print("This is a preschool.")
elif age < 13:
    print("This is a kid.")
elif age < 18:
    print("This is a teenager.")
elif age < 65:
    print("This is an adult.")
else:
    print("This is an old man.")

print("\n=============演示代码练习5.7  喜欢的水果=============")
favorite_fruits = ["a", "b", "c"]
if "a" in favorite_fruits:
    print("You love a.")
if "b" in favorite_fruits:
    print("You love b.")
if "c" in favorite_fruits:
    print("You love c.")
if "d" in favorite_fruits:
    print("You love d.")
if "e" in favorite_fruits:
    print("You love e.")

print("\n=============演示代码练习5.10  检查用户名=============")
current_users = ["a", "b", "c", "d", "e"]
new_users = ["d", "e", "f", "g", "h"]
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() in current_user.lower():
            print(f"Sorry {new_user}, this name is taken.")
        else:
            print(f"You can take {new_user}.")

print("\n=============演示代码练习5.11  序数=============")
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

print("\n=============演示代码练习6.1  人=============")
person = {"first_name": "Li", "last_name": "Ming", "age": 28, "city": "Beijing"}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")


print("\n=============演示代码练习6.2  喜欢的数1=============")
favorite_nums = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
num = favorite_nums["a"]
print(f"a favorite number is {num}")
num = favorite_nums["b"]
print(f"b favorite number is {num}")
num = favorite_nums["c"]
print(f"c favorite number is {num}")
num = favorite_nums["d"]
print(f"d favorite number is {num}")
num = favorite_nums["e"]
print(f"e favorite number is {num}")

print("\n=============演示代码练习6.3  词汇表1=============")
meaning_dict = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E"}
word = "a"
print(f"\n{word} : {meaning_dict[word]}")
word = "b"
print(f"\n{word} : {meaning_dict[word]}")
word = "c"
print(f"\n{word} : {meaning_dict[word]}")
word = "d"
print(f"\n{word} : {meaning_dict[word]}")
word = "e"
print(f"\n{word} : {meaning_dict[word]}")

print("\n=============演示代码练习6.4  词汇表2=============")
meaning_dict = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E"}
for word, meaning in meaning_dict.items():
    print(f"\n{word.title()}: {meaning}")

print("\n=============演示代码练习6.7  人们=============")
person1 = {"first_name": "Li", "last_name": "Ming", "age": 28, "city": "Beijing"}

person2 = {"first_name": "Wang", "last_name": "Hua", "age": 32, "city": "Shanghai"}

person3 = {"first_name": "Zhao", "last_name": "Lei", "age": 25, "city": "Guangzhou"}

people = [person1, person2, person3]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("-" * 20)

print("\n=============演示代码练习6.9  喜欢的地方=============")
favorite_places = {"a": ["A", "B", "C"], "b": ["D", "E"], "c": ["F"]}

for name, places in favorite_places.items():
    print(f"{name} likes the following places:")
    for place in places:
        print(f" - {place}")

print("\n=============演示代码练习6.10  喜欢的数2 =============")
favorite_nums = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for name, numbers in favorite_nums.items():
    print(f"{name} favorvite number is {numbers}")
