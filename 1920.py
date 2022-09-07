n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()


for l in b:
    st, end = 0, n - 1
    isFound = False

    while st <= end:
        mid = (st + end) // 2
        if l == a[mid]:
            isFound = True
            print("1")
            break
        elif l > a[mid]:
            st = mid + 1
        else:
            end = mid - 1
    if not isFound:
        print("0")
