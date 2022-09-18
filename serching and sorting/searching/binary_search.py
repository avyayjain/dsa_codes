def binary_search(array, x):

    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if array[mid] < x:
            low = mid + 1

        elif array[mid] > x:
            high = mid - 1

        else:
            return mid+1

    return -1


arr = [2, 3, 4, 4, 40]
x = 4

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
