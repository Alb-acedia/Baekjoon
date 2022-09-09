from sys import stdin

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    idx = list(range(len(priority)))
    target = idx[m]

    order = 0

    while True:
        if priority[0] == max(priority):
            order += 1
            if idx[0] == target:
                print(order)
                break
            else:
                priority.pop(0)
                idx.pop(0)
        else:
            priority.append(priority[0])
            priority.pop(0)
            idx.append(idx[0])
            idx.pop(0)
