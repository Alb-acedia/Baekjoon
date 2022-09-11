n = int(input())
result = 0
num_list = list(map(int, input().split()))
for i in num_list:
    isPrim = True
    if i == 1:
        isPrim = False
    for x in range(2, i):
        if i % x == 0:
            isPrim = False

    if isPrim:
        result += 1

print(result)
