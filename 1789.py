s = int(input())
n = 1
cnt = 1
while s > n:
    n = n + cnt + 1
    cnt += 1
if n > s:
    print(cnt - 1)
else:
    print(cnt)
