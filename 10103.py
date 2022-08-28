n = int(input())
a, b = 100, 100
for _ in range(n):
    s_1, s_2 = map(int, input().split())
    if s_1 < s_2:
        a -= s_2
    elif s_1 > s_2:
        b -= s_1

print(a)
print(b)
