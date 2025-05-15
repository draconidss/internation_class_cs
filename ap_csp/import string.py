import string
temp = 0
done = False
def count(strng):
    letters = {" ": 0}
    for character in string.ascii_lowercase:
        letters[character] = 0
    for char in strng:
        letters[char] += 1
    for character in string.ascii_lowercase:
        if letters[character] == 0:
            del letters[character]
            print(letters)
            
while done == False:
    count(input("What string woud you like counted? "))
done = False
temp = input("Are you done?(yes/no) ")
if temp == "yes":
    done = True
else:
    done = False