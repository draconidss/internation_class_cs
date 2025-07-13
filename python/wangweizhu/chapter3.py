# list
bikes = ["trek", "redline", "giant"]
print(bikes)
list1 = [1.0, "str1", True]
print(list1)
print(list1[0]) # result: 1.0
print(list1[2]) # result: True
print(list1[-1]) # result: True

# list modifed

print()
# list append insert
list2 = []
print(list2) # result: []
list2.append(1)
list2.append(2)
print(list2) # result: [1, 2]
list2.insert(0, 0)
print(list2) # result: [0, 1, 2]
list2.insert(2, 1.5)
print(list2) # [0, 1, 1.5, 2]