raw_building = [["~"] * 3] * 3
print(raw_building)

N = int(input("n = "))
W = int(input("W = "))
H = input("h = ").split(",")
Roof = input("roof = ").split(",")
int_list = [int(x) for x in H]
max_height = max(int_list)
raw_building = [["~"] * (W*N+N-1) for _ in range(max_height)]

print(int_list)
# i = 0, 1, 2
for i in range(0, len(int_list)):
    height = max_height - int_list[i]
    print("height:", height)
    for j in range(height, max_height):
        for k in range(i * (W + 1), i * (W + 1) + W):
            raw_building[j][k] = "#"

for item in raw_building:
    print(item)
