a, b, c = map(int, input().split())
d = int(input())

b = b + d // 60
c = c + d % 60

while c > 59:
    c = c - 60
    b += 1
while b > 59:
    b = b - 60
    a += 1
    if a > 23:
        a -= 24

print(a, b, c)
