n = int(input())
i = 1
index = 1
prev = 0
cnt = 1
while True:
    if n >= 6 * (index + 1) - 4 and n <= 6 * index + 1:
        print("True")
        print(index)
        break
    else:
        i += 1
        index = index + i
        print("index")
        print(index)
    cnt += 1

print(cnt)
