n = int(input())
_max = 0

for _ in range(n):
    nl = list(map(int, input().split()))
    if nl[0] == nl[1] and nl[1] == nl[2]:
        result = 10000 + nl[0] * 1000
    elif nl[0] == nl[1]:
        eq = nl[0]
        result = 1000 + eq * 100
    elif nl[1] == nl[2]:
        eq = nl[1]
        result = 1000 + eq * 100
    elif nl[2] == nl[0]:
        eq = nl[2]
        result = 1000 + eq * 100
    else:
        result = max(nl) * 100

    if _max < result:
        _max = result

print(_max)
