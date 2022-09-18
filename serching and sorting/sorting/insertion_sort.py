def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

ans = insertion_sort(arr)

print(ans)
