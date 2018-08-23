def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    lst = [1, 45, 34, 98, 32, 45]
    print(bubbleSort(lst))