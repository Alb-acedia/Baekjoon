import sys


T = int(input())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [x for x in range(1, n + 1)]  # 0층 리스트
    for floor in range(k):
        for i in range(1, n):
            f0[i] += f0[i - 1]

    print(f0[n - 1])
