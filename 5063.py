n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    pay = e - c
    if r < pay:
        print("advertise")
    elif r == pay:
        print("does not matter")
    else:
        print("do not advertise")
