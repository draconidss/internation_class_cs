# 1. List constants are surrounded by square brackets and the elements in the list are separated by commas.
# 2. A list element can be any Python object - even another list

list_1 = [1, 'a', [], [2,'b'],True]
print(list_1)
# built-in function: len max min sum
print(len(list_1)) # Output: 5
print("------------------------------------------------------------------------")

# 3. A list can be empty
empty_list = []
print(empty_list)
print("------------------------------------------------------------------------")

# 4. using a list by foreach
for i in list_1:
    print(i)
print("------------------------------------------------------------------------")

# 5. using a list by index
list_5 = [ 'Joseph', 'Glenn', 'Sally' ]
print(list_5[0])

print(list_5[0]) # Joseph
print(list_5[1]) # Glenn
print(list_5[2]) # Sally
# print(list_5[3]) # IndexError: list index out of range
print("------------------------------------------------------------------------")

# 6. insert()/extend()/append() element into a list
list_6 = [1,2, '3']
list_6.append(4)
print(list_6)
# list_6.insert(1,[])
# list_6.extend([1,2])
# list_6.extend(4)  # TypeError: 'int' object is not iterable
# [1,2, '3',1,2]

# list_6.append(4)  # Append 4 to the end of the list
# list_6.insert(0, 0)  # Insert 0 at index 0, shifting other elements
# list_6.extend([5, 6])  # Extend the list with [5, 6]
# list_6.extend('four')  # Extend the list with the string 'four' (adds each character)
# list_6.extend(4)  # TypeError: 'int' object is not iterable

print("list_6:",list_6)  # Output: [0, 1, 2, 3, 4, 5, 6]
print("------------------------------------------------------------------------")

# 7. modify element
list_7 = [1, 2]
list_7[0] = 10  # Modify the first element
list_7[0] = 20  # Modify the second element
print("list_7:",list_7)  # Output: [10, 20]
print("------------------------------------------------------------------------")


# 8. find element:in,not in, index, count
list_8 = [1, 2, 2, 3, 3, 4, 5]
# print(1 in list_8)  # Output: True
# print(1 not in list_8)  # Output: True

# input number until number is not repeat
# while True:
#     num_8 = int(input("Please enter a number: "))
#     if num_8 in list_8:
#         print(f"{num_8} is in the list.")
#     else:
#         print(f"{num_8} is not in the list.")
#         break

# print(list_8.index(3))  # index of first occurrence of 3
# print(list_8.index(0))  # ValueError: 0 is not in list
# print(list_8.count(2))  # Output: 2 (number of occurrences of 2)


print("------------------------------------------------------------------------")

# 9. delete element
list_9 = ['a', 'b', 'c', 'd']
# del list_9[0]  # Delete the first element
# list_9.remove('a')  # Remove the first occurrence of 'a'
# list_9.pop()  # Remove and return the last element
# list_9.pop(1)  # Remove and return the element at index 1
# list_9.clear()  # Clear the entire list
print("list_9:",list_9)  # Output: [2, 4]
print("------------------------------------------------------------------------")

# 10. sort element: sort,reverse
list_10 = [5, 2, 9, 1, 5, 6]
# list_10.sort()  # Sort the list in ascending order
# list_10.reverse()  # Reverse the list
# list_10.sort(reverse=True)  # Sort the list in descending order

# 11. list-deductive formula
# formula: [expr for variable in iterable/range], in with range and iterable
# list_11 = [1, 2, 3, 4, 5]
# [print(x) for x in list_11]  # Output: [2, 4, 6, 8, 10]
# list_11 = []
# for x in range(1, 11):
#     list_11.append(x)
# [list_11.append(x) for x in range(1,11)]
# list_10 = [x for x in range(1, 11)]
