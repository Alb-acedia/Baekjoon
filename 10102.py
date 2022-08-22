v = int(input())
ab = list(input())
a_cnt = 0
b_cnt = 0

for i in range(v):
    if ab[i] == "A":
        a_cnt += 1
    else:
        b_cnt += 1

if a_cnt < b_cnt:
    print("B")
elif a_cnt > b_cnt:
    print("A")
else:
    print("Tie")
