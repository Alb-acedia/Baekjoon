t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    Max = 0
    for _ in range(n):

        S, L = input().split()
        if Max < int(L):
            result = S
            Max = int(L)

    print(result)
