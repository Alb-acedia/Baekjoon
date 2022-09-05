import sys

lan = []
total = 0
k, n = map(int, input().split())
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

# 이분탐색
st, end = 1, max(lan)
while st <= end:
    mid = (st + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid

    if cnt >= n:
        st = mid + 1
    else:
        end = mid - 1

print(end)
