
# Chapter3
# 3.5 修改嘉宾名单
print("\n========== Practice 3.5 修改嘉宾名单 ==========")
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack 无法赴约，转而邀请 Gary
# equal guests[1] = "gary snyder"
del(guests[1])
print("del(guests[1]) :",guests)
guests.insert(1, 'gary snyder')
print("guests.insert(1, 'gary snyder') :",guests)