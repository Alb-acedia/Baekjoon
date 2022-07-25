l, p = map(int, input().split()) 
n = list(map(int, input().split()))

for x in n:
    print(x-l*p, end=' ')

