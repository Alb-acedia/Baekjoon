n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in b:
    start, end = 0, n - 1
    isFound = False

    while start <= end:
        mid = (start + end) // 2
        if i == a[mid]:
            isFound = True
            print(1)
            break
        elif i > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not isFound:
        print(0)
