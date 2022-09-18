def largestHistRow(arr):
    result = []
    top_val = 0
    max_area = 0

    area = 0

    i = 0
    while i < len(arr):
        if (len(result) == 0) or (arr[result[-1]] <= arr[i]):
            result.append(i)
            i += 1
        else:
            top_val = arr[result.pop()]
            area = top_val * i

            if len(result):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)

    while len(result):
        top_val = arr[result.pop()]
        area = top_val * i
        if len(result):
            area = top_val * (i - result[-1] - 1)

        max_area = max(area, max_area)

    return max_area


def maxRectangle(arr):
    result = largestHistRow(arr[0])

    for i in range(1, len(arr)):

        for j in range(len(arr[i])):
            if arr[i][j]:
                arr[i][j] += arr[i - 1][j]

        result = max(result, largestHistRow(arr[i]))

    return result


# Driver code
arr = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]

print("Maximum rectangle is: ", maxRectangle(arr))