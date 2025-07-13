message = "my name is draco"
print(message)
message = "hello world"
print(message)

# variable name format
message = "aaa"
my_name = "draco"

print()

# string
string1 = "string1"
string2 = 'string2'
string3 = """aaa
bbb"""

print(string1)
print(string2)
print(string3)

name = "abc def"
print(name.title())
print(name.upper())
print(name.lower())

name1 = f"aaa {name.title()} bbb {name.upper()}"
print(name1)

name2 = "abc\n\ndef"
print(name2)

#remove string blank
name3 = " iTuring "
print(name3)

# remove string right blank
name4 = " iTuring "
print(name4.rstrip())

# remove string left blank
name5 = " iTuring "
print(name5.lstrip())

# remove string two side blank
name6 = " iTuring "
print(name6.strip())

# string removeprefix
url = "https://www.baidu.com"
url = url.removeprefix("https://")
print("url: " + url)

url1 = "https://www.baidu.com"
url1 = url1.removeprefix("aabb")
print("url1: " + url1)

# string syntax
str1 = "life\'s pathetic\""
print("str1:" + str1)

# string addition
str2 = "Hello" + "ITuring"
print("str2:" + str2)
# equal "Hello" + "Hello" + "Hello"
str3 = "Hello" * 3
print("str3:" + str3)

# number: integer and float
integer1 = 1_000_000
float1 = 1_000_000.5
print("integer1:" + str(integer1))
print("float1:" + str(float1))

# number: multi operate
print(3 * 3)
print(2.5 * 2)
print(1.5 * 1.5)

# number: divide operate
print(3 / 3) # 1.0
print(2.5 / 2) # 1.25
print(2 / 4) # 0.5
print(3 // 3) # 1
print(1 // 2) # 0
print(2.5 // 2) # 1.0

# number: double multi operate
print(3 ** 3) # 27
print(2.5 ** 2) # 6.25

# boolean
bool1 = True
bool2 = False
print("bool1: " + str(bool1))
print("bool2: " + str(bool2))

# multi variable
a,b,c = 0,"b",True

# constant
MAX_CONNECTIONS = 100 # comment