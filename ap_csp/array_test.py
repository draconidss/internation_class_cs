import array as arr

def arr_test_1():
    a = [1,'a']
    index = 1
    print(a[index])

    # colours = ['red', 'yellow', 'black', 'green', 'blue', 'white', 'orange', 'purple',
    # 'grey', 'maroon']
    # for index in range(len(colours)):
    #     print(colours[index])

    # # numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # # for count in range(0, 5):
    # #     numbers[count] = int(input("Enter a number"))
    # # print(numbers)

    # values = []
    # # insert code to populate array
    # ValueToFind = int(input("Enter the value to find"))
    # for count in range(0, 50):
    #     if ValueToFind in values[count]:
    #         print("Found it")

    # arrayData = [[0] * 5 for i in range(5)]
    # print(arrayData[4][1])

    arrayData = [[0] * 10 for i in range(3)]
    print(arrayData)
    #insert code to populate array
    for row in range(3):
        for column in range(10):
            print(arrayData[row][column])

arr_test_1()