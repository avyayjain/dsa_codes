def linear_search(arr, length, item):

    for i in range(0, length):
        if arr[i] == item:
            return i + 1

    return -1


arr = [10, 13, 32, 23, 23, 20, 24, 24]

item = int(input("input the value you want to search"))

length = len(arr)

ans = linear_search(arr, length, item)

print(ans)
