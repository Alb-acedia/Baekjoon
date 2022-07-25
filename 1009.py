t = int(input())

# for _ in range(t):
#    a, b = map(int, input().split())
#    n = pow(a, b) % 10
#    print(n)
# 시간 초과

for _ in range(t):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 1:
            print(a)
        else:
            print(a * a % 10)
    else:
        b = b % 4
        if b == 0:
            print(pow(a, 4) % 10)
        else:
            print(pow(a, b) % 10)
