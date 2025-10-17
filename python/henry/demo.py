def display_message():
    print("happy python")


display_message()


def make_shirt(size, word):
    print(f"The T-shirt size is {size}, there will be {word} on it.")


make_shirt(word="Love you man", size=35)
make_shirt(36, "Love you man")


def make_shirt(size, word="I love Python"):
    print(f"The T-shirt size is {size}, there will be {word} on it.")


make_shirt(80)
make_shirt(1)
make_shirt(40, "love you Man")


def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")


describe_city("Hong Kong", "China")
describe_city("Iceice")
describe_city("Icecream")


def make_album(singer, album, number_of_songs=None):
    result = {"singer": singer, "album": album}
    if number_of_songs:
        result["number_of_songs"] = number_of_songs
    return result


print(make_album("a", "b"))
print(make_album("c", "d"))
print(make_album("e", "f"))
print(make_album("g", "i", 10))

i = 3.0
print(i * 2, 2**i, 3 * 2, 2.0 * 3, 3**2, 2.0**3)

i = 4.0
print(17 // i, 17.0 / 4, 18 // 7, 18.0 // 7)
t1 = (1,)
print(t1)

tl = 3, 4, 5
t2 = 9, 5, 2
t3 = 3, 4
t4 = 9, 4, 3
t5 = (2,)
t6 = t3 + t5
l = [tl, t2, t3, t4, t5, t6]
l.sort()
for v in l:
    print(v, end=".")

print()
filter_code = ""
for c in "01Python":
    if c in "0123456789":
        filter_code += c
print(filter_code)

board = ["1", "o"]
print(all(cell in ["x", "o"] for cell in board))

nums = "1, 2, 3 4 5"
print(nums.split(", "))

order = True
print("True") if order else print("False")
print(11.14 % 10)

number = 1012
sum = 0
while number > 0:
    remainder = number % 10
    sum = sum + remainder
    number = number / 10
    print(number)
print("Output", sum)

str_2 = "abcd"
print(str_2[1 : len(str_2) + 1])
print(str_2[1:3][::-1])

for i in range(1, 10):
    print(i)


def rev(x, words):
    result = x.split(" ")
    for index, item in enumerate(result):
        if item in words:
            result[index] = item[::-1]
    return " ".join(result)


print(rev("Kit kitty kit cat", ["kit", "cat"]))
