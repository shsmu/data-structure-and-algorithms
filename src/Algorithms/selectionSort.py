def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        # 记录最小数的索引
        minIndex  = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

if __name__ == '__main__':
    lst = [1, 45, 34, 98, 32, 45, 77]
    print(selectionSort(lst))