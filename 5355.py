t = int(input())

for _ in range(t):
    s = list(input().split())
    n = float(s.pop(0))
    for i in range(len(s)):
        if s[i] == "@":
            n *= 3
        elif s[i] == "%":
            n += 5
        elif s[i] == "#":
            n -= 7
    print("%.2f" % n)
