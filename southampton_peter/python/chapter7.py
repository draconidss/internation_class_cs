# print("Please enter your name:")
# name = input()
# print(name)

# print("Please enter a number:")
# number = input() # number is a string
# number **= 2 # number = number ** 2
# print(number) # TypeError

# print("Please enter a number:")
# number_1 = int(input()) # number is a integer
# number_1 **= 2 # number = number ** 2
# print(number_1)

print(f"int(True): {int(True)}") # integer of 1
print(f"int(\"10\"): {int("10")}") # integer of 10
print(f"int(\"1.5\"): {int(1.5)}") # integer of 1
# print(f"int(\"abc100\"): {int("abc100")}") # TypeError
print(f"bool(\"True\"): {bool("True")}") # True

message = ""
while message != "quit":
    message = input("tell me: ")
    print(message)