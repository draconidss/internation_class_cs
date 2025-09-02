list_1 = ["redline", "giant", "trek"]
print(f"list_1[2] : {list_1[2]}") # trek
print(f"list_1[-3] : {list_1[-3]}") # redline

list_1[2] = "draco"
print(f"list_1[2] : {list_1[2]}") # draco
print(f"list_1 : {list_1}") # ['redline', 'giant', 'draco']

list_1.append(4)
print(f"list_1 : {list_1}") # ['redline', 'giant', 'draco', 4]

list_1.insert(-2, "insert_value")
print(f"list_1 : {list_1}") # ['redline', 'giant', 'insert_value', 'draco', 4]

del list_1[-2]
print(f"list_1 : {list_1}") # ['redline', 'giant', 'insert_value', 4]

pop_value = list_1.pop()
print(f"pop_value: {pop_value}") # 4
print(f"list_1 : {list_1}") # ['redline', 'giant', 'insert_value']

pop_value_2 = list_1.pop(0)
print(f"pop_value_2: {pop_value_2}") # 'redline'
print(f"list_1 : {list_1}") # ['giant', 'insert_value']

# sort
nums = [9, 6 ,1, 4, 2]
print(f"sorted(nums): {sorted(nums)}") # [1, 2, 4, 6, 9]
print(f"nums: {nums}") # [9, 6 ,1, 4, 2]
nums.sort()
print(f"nums: {nums}") # [1, 2, 4, 6, 9]
nums.sort(reverse=True)
print(f"nums: {nums}") # [9, 6, 4, 2, 1]
print(f"sorted(reverse=True, nums)：{sorted(nums, reverse=True)}") # [9, 6, 4, 2, 1]