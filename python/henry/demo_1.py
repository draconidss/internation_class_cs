arr = []
number = 1
for row in range(3):
    arr.append([])
    for column in range(3):
        arr[row].append(number)
        number += 1

print()


def print_2d_array(arr):
    result = ""
    # item is secondary array
    for item in arr:
        join_string = " || ".join([str(x) for x in item])
        result += "| " + join_string + " |\n"
    return result


result = print_2d_array(arr)
print(result)

print(type(100) == int)
