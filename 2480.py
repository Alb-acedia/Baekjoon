nl = list(map(int, input().split()))

if nl[0] == nl[1] and nl[1] == nl[2]:
    print(10000 + nl[0] * 1000)
elif nl[0] == nl[1]:
    eq = nl[0]
    print(1000 + eq * 100)
elif nl[1] == nl[2]:
    eq = nl[1]
    print(1000 + eq * 100)
elif nl[2] == nl[0]:
    eq = nl[2]
    print(1000 + eq * 100)
else:
    print(max(nl) * 100)
