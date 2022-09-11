n = int(input())
result = 0
num_list = list(map(int, input().split()))
for i in num_list:
    isOrder = False
    for x in range(2, i):
        if i % x == 0:
            isOrder = True

    if not isOrder:
        result += 1

print(result)
