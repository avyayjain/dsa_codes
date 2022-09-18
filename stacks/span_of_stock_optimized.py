from collections import deque


def stockSpan(arr):
    stack = deque()
    stack.append(0)
    print(1, end=" ")

    for i in range(1, len(arr)):
        while len(stack) != 0 and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if len(stack) == 0:
            print(i + 1, end=" ")
        else:
            print(i - stack[-1], end=" ")

        stack.append(i)


# Driver code
arr = [100, 20, 30, 60, 132, 36, 32, 55, 80, 50, 120]
stockSpan(arr)
