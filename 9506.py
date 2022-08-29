n = 0
divisor = []

while n != -1:
    n = int(input())
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    result = str(n) + " = 1"
    if sum(divisor) == n:
        for i in range(1, len(divisor)):
            result += " + " + str(divisor[i])
        print(result)
    else:
        print("%d is NOT perfect." % (n))

    divisor.clear()
