n = int(input())
i = 1
index = 0
cnt = 2
while True:
    if n == 1:
        cnt = 1
        break
    if n >= 6 * (index + 1) - 4 and n <= 6 * (index + i) + 1:
        break
    else:
        index = index + i
        i += 1
        cnt += 1


print(cnt)
