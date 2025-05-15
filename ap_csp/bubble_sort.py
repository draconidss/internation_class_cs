1. 相邻比较值，并根据正序逆序决定交换的条件是比大还是比小

什么时候


#第一轮


46 24 22 39 22 9 50
1:
46 24 39 22 22 9 50
46 24 39 22 22 50 9

2:
46 39 24 22 22 50 9
46 39 24 22 50 22 9

3:
46 39 24 50 22 22 9

4: 
46 39 50 24 22 22 9

5:
46 50 39 24 22 22 9

6:
50 46 39 24 22 22 9

7:
50 46 39 24 22 22 9 




1 2 1 3 5

swapped = False
1 1 2 3 5


















def bubble_sort_verbose(arr):
    n = len(arr)
    print(f"初始数组: {arr}")
    
    for i in range(n - 1):  # 外层循环控制排序的轮数
        print(f"\n第 {i + 1} 轮排序开始")
        swapped = False  # 标志变量，用于检测是否发生了交换
        
        for j in range(n - 1 - i):  # 内层循环控制每轮的比较次数
            print(f"  比较索引 {j} 和 {j + 1} 的值: {arr[j]} 和 {arr[j + 1]}")
            
            if arr[j] > arr[j + 1]:  # 如果相邻元素逆序
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                # arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换它们的位置
                swapped = True  # 设置标志变量为 True
                print(f"  交换后数组: {arr}")

        if swapped == False:  # 如果没有发生交换，说明数组已经有序
            print(f"第 {i + 1} 轮排序后，数组已有序，提前退出排序")
            break  # 提前退出外层循环
        else:
            print(f"第 {i + 1} 轮排序结束，当前数组状态: {arr}")
    
    print("\n排序完成，最终数组: ", arr)

# 测试代码
array = [5, 3, 8, 4, 2]
bubble_sort_verbose(array)