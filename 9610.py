n = int(input())
cnt1 = cnt2 = cnt3 = cnt4 = axis = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 and y > 0:
        cnt2 += 1
    elif x < 0 and y < 0:
        cnt3 += 1
    elif x > 0 and y < 0:
        cnt4 += 1
    else:
        axis += 1

print("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d" % (cnt1, cnt2, cnt3, cnt4, axis))
