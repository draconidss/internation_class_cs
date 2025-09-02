print("\n=============3.1姓名=============")
names = ['a','b','c']
print(names)
print(names[0])
print(names[1])
print(names[2])

print("\n=============演示代码2-1=============")
name = 'iTuring'
print(f'hello {name}')

print("\n=============演示代码2-2=============")
print('Python Rust') 
print() 
print('Python\tRust')
print() 
print('Python\nRust')

print("\n=============演示代码2-3=============")
msg1, msg2 = 'hello world', ' iTuring' 
print(f'{msg1.title()}\n{msg1.upper()}') 
print(f'{msg2}\n{msg2.strip()}') 
print('fname.txt'.removesuffix('.txt'))

print("\n=============演示代码2-4=============")
print(1, 1_000_000, 1.5) 
print(True, False)
print(1 + 1, 1.0 + 1.0, 1 + 1.0) 
print(3 ** 2, 3 / 2, 3 // 2, 5 % 2)

print("\n=============演示代码3-1=============")
bikes = ['trek', 'redline', 'giant'] 
print(bikes) 
print(bikes[0])
print(bikes[2], bikes[-1])

print("\n=============演示代码3-2=============")
bikes = ['trek']
bikes[0] = 'giant'
print(bikes)

print("\n=============演示代码3-3=============")
bikes = []
bikes.append('redline')
bikes.insert(0, 'trek')
print(bikes)

print("\n=============演示代码3-4=============")
bikes = ['giant', 'trek', 'redline']
bikes.pop(0)
print(bikes.pop())
print(bikes)

print("\n=============演示代码3-5=============")
bikes = ['giant', 'trek', 'redline']
del bikes[0]
bikes.remove('trek')
print(bikes)

print("\n=============演示代码3-6=============")
nums = [9, 6, 1, 4, 2] 
print(len(nums)) 
print(sorted(nums)) 
print(nums)
nums.sort() 
print(nums)  
nums.sort(reverse=True) 
print(nums) 
nums.reverse() 
print(nums)

print("\n=============演示代码4-1=============")
bikes = ['trek', 'redline']
for bike in bikes:
    print(bike.title())

print("\n=============演示代码4-2=============")
print(range(2))
print(list(range(2)))
squares = []
for value in range(2,5):
    squares.append(value ** 2)
squares_comp = [value ** 2 for value in range(2,5)]
print(squares == squares_comp)
print(squares)
print(min(squares), max(squares), sum(squares))

print("\n=============演示代码4-3=============")
bikes = ['trek', 'redline', 'giant']  
print(bikes[1:])  
print(bikes[:-1])  
print(bikes[0:1]) 
bikes_copy = bikes[:]
bikes_copy.reverse() 
print(bikes) 
print(bikes_copy)

print("\n=============演示代码4-4=============")
dimensions = (200, 50) 
for value in dimensions: 
    print(value) 
dimensions = (300, 100) 
print(dimensions) 
dimensions = 100 
print(dimensions)

print("\n=============演示代码5-1=============")
condition1 = (100 == 100)
condition2 = (100 != 100)
condition3 = (100 < 200)
condition4 = (100 >= 200)
condition5 = ('a' in ['a'])
condition6 = ('a' not in ['a'])
condition7 = condition1 or condition2
condition8 = condition1 and condition2

print("\n=============演示代码5-2=============")
age, vip = 12, False 
if 0 <= age < 4 and vip: 
    ticket_price = 0 
elif age < 18: 
    ticket_price = 25 
elif age < 65: 
    ticket_price = 40 
else: 
    ticket_price = 20 
print(f'Ticket price is {ticket_price}.')

print("\n=============演示代码6-1=============")
alien = {'color': 'green', 'points': 5} 
print(alien['color'], alien.get('color'))

print("\n=============演示代码6-2=============")
alien = {'color': 'green', 'points': 5} 
alien['color'] = 'red' 
alien['position'] = (0, 25) 
print(alien)

print("\n=============演示代码6-3=============")
d = {'a': 1, 'b': 2, 'c': 3} 
del d['a'] 
print(d.pop('c')) 
print(d)

print("\n=============演示代码6-4=============")
favorites = {'jen': 'python', 'edward': 'rust'} 
print(len(favorites)) 
for name, language in favorites.items(): 
    print(f"{name} loves {language}.") 
 
print(list(favorites.keys())) 
print(list(favorites.values()))

print("\n=============演示代码6-5=============")
squares = {x: x ** 2 for x in range(4)} 
keys, vals = [0, 1, 2, 3], [0, 1, 4, 9] 
squares_zip = {key: val 
               for key, val in zip(keys, vals)}
print(squares == squares_zip, squares)

print("\n=============演示代码7-1=============")
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

print("\n=============演示代码7-2=============")
age = input("How old are you? ")
age = int(age)
print(type(age), type(int(age)))
pi = float(input("What's the value of pi? "))

print("\n=============演示代码7-3=============")
current_number = 0 
while True:
    current_number += 1
    if current_number > 5:
        break
    if current_number % 2 == 0:
        continue
    print(current_number)

print("\n=============演示代码8-1=============")
def describe_pet(animal, name, color='yellow'):
    print(f"My {animal}'s name is {name}, color is {color}.")
    
discribe_pet('hamster', 'harry')
describe_pet(name='willie', color='black', animal='dog')

print("\n=============演示代码8-2=============")
def add_if_same_or_sub(x, y): 
    if x == y: 
        return x + y 
    return x - y 
val1 = add_if_same_or_sub(5, 2) 
val2 = add_if_same_or_sub(2, 2) 
print(val1, val2)

print("\n=============演示代码8-3=============")
def func(*args, **kwargs): 
    print(f"args: {args}\nkwargs: {kwargs}")  
func(1, 2, k='v')

print("\n=============演示代码练习3.1  姓名=============")
names = ['a', 'b', 'c']
print(names(0))
print(names(1))
print(names(2))

print("\n=============演示代码练习3.2  问候语=============")
names = ['a', 'b', 'c']
message = f"Hello,{names[0].title()}!"
print(message)
message = f"Hello,{names[1].title()}!"
print(message)
message = f"Hello,{names[2].title()}!"
print(message)

print("\n=============演示代码练习3.4  嘉宾名单 =============")
guests = ['a', 'b', 'c']
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)

print("\n=============演示代码练习3.5  修改嘉宾名单=============")
guests = ['a', 'b', 'c']
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
print(f"{guests[0].title()} cannot enjoy the dinner.")
del guests[0]
guests.insert(0, 'd')
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"

print("\n=============演示代码练习3.6  添加嘉宾=============")
guests = ['a', 'b', 'c']
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print(message)
print(f"{guests[0].title()} cannot enjoy the dinner.")
del guests[0]
guests.insert(0, 'd')
message = f"{guests[0].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[1].title()}, I want to enjoy the dinner with you!"
print(message)
message = f"{guests[2].title()}, I want to enjoy the dinner with you!"
print("We find a bigger table!")
 