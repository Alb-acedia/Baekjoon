n = int(input())
cnt = 0
n_cnt = 0

for _ in range(n):
    answer = int(input())
    if answer == 1:
        cnt += 1
    else:
        n_cnt += 1

if cnt > n_cnt:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
