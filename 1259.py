while True:
    pel = input()
    cnt = 0
    if pel == "0":
        break

    for i in range(len(pel)):
        if pel[i] == pel[len(pel) - 1 - i]:
            cnt += 1

    if cnt == len(pel):
        print("yes")
    else:
        print("no")
