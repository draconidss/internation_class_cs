# 2.1简单消息
name = "hello"
print(name)

# 2.2多条简单消息
name1 = "wwz"
print(name1)
name1 = "wwz1"
print(name1)

# 2.3/2.4 个性化消息
name2 = "Eric wwz dawn"
msg = f"Hello {name2.title()},whould you like to learn some Python today?"
print(msg)
name2 = "Eric"
msg = f"Hello {name2.upper()},whould you like to learn some Python today?"
print(msg)
name2 = "Eric"
msg = f"Hello {name2.lower()},whould you like to learn some Python today?"
print(msg)

# 2.5名言1
print('Albrt Einstein once said,"A person who never made a mistake never tried anything new"')

# 2.6名言2
famous_person = "Albert Einstein"
msg1 = f'{famous_person} once said,"A person who never made a mistake never tried anything new."'
print(msg1)

#2.7删除人名中空白
name4 = "\tEric Matthes\n"
print("Unmmodified:")
print(name4)
print("\nUsing lstrip():")
print(name4.lstrip())
print("\nUsing rstrip():")
print(name4.rstrip())
print("\nUsing strip():")
print(name4.strip())


# 2.8文件拓展名
filename = "python_notes.txt"
filename1 = filename.removesuffix(".txt")
print(filename1)

# 2.9数字8
print(4 + 4) # 8
print(2 * 4) # 8
print(2.0 * 4) # 8.0
print(16 / 2) # 8.0
print(16.0 / 2) # 8.0
print(16 // 2) # 8
print(16.0 // 2) # 8.0
print(10 - 2) # 8

#2.10最喜欢的数字
print("\n=============2.10 喜欢的数字 =============")
favoritenumber = 17
msg2 = f"my favorite number is {favoritenumber}."


print("a\nb")

#3.1姓名
print("\n=============3.1姓名 =============")
names = ['wwz', 'apple', 'wwl']
print(names[0]) # wwz
print(names[1]) # apple
print(names[2]) # wwl

#3.2问候
print("\n=============3.2 问候=============")
names = ['wwz', 'apple', 'wwl']
msg3 = f"Hello, {names[0].title()}!"
print(msg3) # Hello,Wwz
msg3 = f"Hello, {names[1].title()}!"
print(msg3) # Hello,Apple
msg3 = f"Hello, {names[2].title()}!"
print(msg3) # Hello,Wwl

#3.3自己的列表
print("\n=============3.3自己的列表=============")
name5 = ['bus', 'bike', 'motorcycle']
msg4 = f"I would like to own a Honda name5[2]"

#3.4嘉宾名单
print("\n=============3.4嘉宾名单=============")
names1 = ['wwz', 'apple', 'wwl']
print(names1[0])
print(names1[1])
print(names1[2])

#3.5修改嘉宾名单





#3.6添加嘉宾
print("\n=============3.6添加嘉宾=============")
names2 = ["a","b","c"]
names2.insert(0,"e")
print("names2.insert(0, 'e') :",names2) # [e,a,b,c,]
names2.insert(2,"f")
print("names2.insert(2, 'f') :",names2) # [e,a,f,b,c,]
names2.append("g")
print("names2.append('g')) :",names2) # [e,a,f,b,c,g]

#3.7缩短名单
print("\n=============3.7缩短名单=============")
names2 = ["a","b","c"]
names2.insert(0,"e")
print("names2.insert(0, 'e') :",names2) # [e,a,b,c,]
names2.insert(2,"f")
print("names2.insert(2, 'f') :",names2) # [e,a,f,b,c,]
names2.append("g")
print("names2.append('g')) :",names2) # [e,a,f,b,c,g]
person1 = names2.pop(0)
msg5 = f"sorry", {person1}
print(msg5)
person2 = names2.pop(0)
msg6 = f"sorry", {person2}
print(msg6)
person3 = names2.pop(0)
msg7 = f"sorry", {person3}
print(msg7)
person4 = names2.pop(0)
msg8 = f"sorry", {person4}
print(msg8)
del names2[0]
del names2[0]

#3.8放眼看世界
print("\n=============3.8放眼看世界=============")
names3 = ["g","e","q","v","y"]
print(names3) # ["g","e","q","v","y"]
print(sorted(names3)) # ["e","g","q","v","y"]
print(sorted(names3,reverse=True)) # ["y","v","q","g","e"]
print(names3) # ["g","e","q","v","y"]
names3.reverse()
print(names3) # ["y","v","q","g","e"]
names3.reverse()
print(names3) # ["g","e","q","v","y"]
names3.sort()
print(names3) # ["e","g","q","v","y"]
names3.sort(reverse=True)
print(names3) # ["y","v","q","g","e"]

#4.1比萨
print("\n=============4.1比萨=============")
pizzas = ["a","b","c"]
for pizza in pizzas:
    print(pizza)
    print(f"{pizza},I like it")
print("I like pizza")

#4.2动物
print("\n=============4.2动物=============")
animals = ["a","b","c"]
for animal in animals:
    print(animal)
    print(f"{animal},it is")
print("They are animals")

#4.3数到20
print("\n=============数到20=============")
numbers = list(range(1, 21))
for number in numbers: 
    print(number)
nums1 = [num1 for num1 in range(1,21)]
print(nums1)

#4.4 100万求和
print("\n=============4.4 100万求和=============")
nums3 = [num3 for num3 in range (1,1000000)]
print(sum(nums3))

sum = 0
for number in nums3:
    sum = sum + number
print(sum)

#4.6奇数
print("\n=============4.6奇数=============")
nums4 = [number for number in range(1,21,2)]
print(nums4)

#4.7被3整除
print("\n=============4.7被3整除=============")
nums5 = [number for number in range(3,31,3)]
print(nums5)

#4.8立方
print("\n=============4.8立方=============")
nums = [num**3 for num in range(1,11)]
print(nums)

#4.11你的比萨，我的比萨
print("\n=============4.11你的比萨，我的比萨=============")
fp = ["a","b","c"]
mp = fp[:]
fp.append("d")
mp.append("e")
for pizza1 in fp:    
    print(f"my favourite pizza are,{fp}")
for pizza2 in mp:    
    print(f"my favourite pizza are,{mp}")

#4.12使用多个循环
print("\n=============4.12 使用多个循环=============")
ff = ["a","b","c"]
mf = ff[:]
ff.append("d")
mf.append("e")
for pizza1 in ff:    
    print(f"my favourite pizza are,{ff}")
for pizza2 in mf:    
    print(f"my favourite pizza are,{mf}")

#4.13自助餐
print("\n=============4.13自助餐=============")
dimensions = ("a","b","c","d","e")
for food in dimensions:
    print(food)
#dimensions[0] = "f" # TypeError: 'tuple' object does not support item assignment
dimensions = ("a","b","c","f","g")
for food in dimensions:
    print(dimensions)

#5.3 外星人颜色 1
print("\n=============5.3 外星人颜色 1=============")
alien_color = "green"
if alien_color == "green":
    print("you get 5 points")
alien_color = "yellow"
if alien_color == "green":
    print("you get 5 points")

#5.4 外星人颜色 2
print("\n=============5.4 外星人颜色 2=============")
alien_color = "green" #5 points
if alien_color == "green":
    print("you get 5 points")
else:
    print("you get 10 points")
alien_color = "red" #10 points
if alien_color == "green":
    print("you get 5 points")
else:
    print("you get 10 points")

#5.5 外星人颜色 3
print("\n=============5.5 外星人颜色 3=============")
if alien_color == "green":
    print("you get 5 points")
elif alien_color == "yellow":
    print("you get 10 points")
else:
    print("you get 15 points")

#5.6 人生的不同阶段
print("\n=============5.6 人生的不同阶段=============")
age = 18
if age < 2:
    print("You're a baby!")
elif age >= 2 and age < 4: 
    print("You're a toddler!")
elif age >= 4 and age < 13: 
    print("You're a kid!")
elif age >= 13 and age < 18: 
    print("You're a teenager!")
elif age >= 18 and age < 65: 
    print("You're an adult!")
else: 
    print("You're an elder!")

#5.7 喜欢的水果
print("\n=============5.7 喜欢的水果=============")
favorite_fruits = ["a","b","c"]
if "a" in favorite_fruits:
    print("you really like a")
if "b" in favorite_fruits:
    print("you really like b")
if "c" in favorite_fruits:
    print("you really like c")
if "d" in favorite_fruits:
    print("you really like d")
if "e" in favorite_fruits:
    print("you really like e")

#5.8 以特殊方式跟管理员打招呼
print("\n=============5.8 以特殊方式跟管理员打招呼=============")
names = ["wwz","wwl","zsl","wwf","admin"]
for name in names:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

#5.9 处理没有用户的情形
print("\n=============5.9 处理没有用户的情形=============")
names = []
if names:
    for name in names:
        if name == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")




#5.10 检查用户名
print("\n=============5.10 检查用户名=============")
current_users = ["Wwz","wwl","Zsl","Rcw","rcy"]
for index, current_user in enumerate(current_users):
    current_users[index] = current_user.lower()
print(current_users)
current_users = [current_user.lower() for current_user in current_users]
new_users = ["wwf","wwx","wwz","wwl","dyc"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("sorry,you can't use this name")
    else:
        print("you can use this name")

#5.11 序数
print("\n=============5.11 序数=============")
numbs = [number for number in range(1,10)]
for numb in numbs:
    if numb == 1:
        print("1st")
    elif numb == 2:
        print("2nd")
    elif numb == 3:
        print("3rd")
    else:
        print(f"{numb}th")

#6.1 人
print("\n=============6.1 人=============")
people = {
    "first_name":"weizhu",
    "last_name":"wang",
    "age":18,"city":"anhui"
}
print(people["first_name"])
print(people["last_name"])
print(people["age"])
print(people["city"])

#6.2 喜欢的数 1
print("\n=============6.2 喜欢的数 1=============")
favorite_num = {"wwz":17,"wwl":7,"wwf":9}
print(favorite_num)

#6.3 词汇表 1
print("\n=============6.3 词汇表 1=============")
Programming_terms = {"Lists":"A list stores a series of items in a particular order. You access items using an index, or within a loop.","Tuples":"Tuples are similar to lists, but the items in a tuple can't be modified.","If_statements":"If statements are used to test for particular conditions and respond appropriately."}
print(f"\nLists:{Programming_terms["Lists"]}")
print(f"\nTuples:{Programming_terms["Tuples"]}")
print(f"\nIf_statements:{Programming_terms["If_statements"]}")

#6.4 词汇表 2
print("\n=============6.4 词汇表 2=============")
Programming_terms = {"Lists":"A list stores a series of items in a particular order. You access items using an index, or within a loop.","Tuples":"Tuples are similar to lists, but the items in a tuple can't be modified.","If_statements":"If statements are used to test for particular conditions and respond appropriately."}
for name,language in Programming_terms.items():
    print(f"\n{name}:{language}")

#6.5 河流
print("\n=============6.5 河流=============")
rivers = {"nile":"egypt","mississippi":"united states","huanghe":"china", }
for name,country in rivers.items():
    print(f"The {name} runs through {country}")

#6.6 调查
print("\n=============6.6 调查=============")
favorite_languages = {'wwz': 'a','wwl': 'b','wwf': 'c', 'zsl': 'd', }
print(favorite_languages)
people = ["wwz","wwl","wwf","zsl","dyc","fch"]
for name in people:
    if name in favorite_languages:
        print(f"thanks {name}")
    else:
        print(f"please {name}")

#6.7 人们
print("\n=============6.7 人们=============")
people = []
person = {"first_name":"weizhu","last_name":"wang","age":18,"city":"anhui"}
people.append(person)
person = {"first_name":"weilin","last_name":"wang","age":19,"city":"anhui"}
people.append(person)
person = {"first_name":"weifang","last_name":"wang","age":16,"city":"anhui"}
people.append(person)
for person in people:
    print(f"{person['last_name']}{person['first_name']}")
    print(person["age"])
    print(person["city"])

#6.8 宠物
print("\n=============6.8 宠物=============")
pets = []
pet = {'animal type': 'dog','name': 'ruyu','owner': 'wwz','weight': 10,'eats': 'food',}
pets.append(pet)
pet = {'animal type': 'dog','name': 'jixiang','owner': 'wwz','weight': 60,'eats': 'food',}
pets.append(pet)
print(pets)

#6.9 喜欢的地方
print("\n=============6.9 喜欢的地方=============")
favorite_places = {'wwz': ['a', 'b', 'c'],'wwl': ['f', 'e'],'wwf': ['g', 'h']}
for name,places in favorite_places.items():
    print(f"{name} like：")
    for place in places:
        print(place)

#6.10 喜欢的数 2
print("\n=============6.10 喜欢的数 2=============")
favorite_num = {"wwz":17,"wwl":7,"wwf":9}