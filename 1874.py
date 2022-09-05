n = int(input())
result = []
st = []
num = 0
answer = True

for i in range(n):
    x = int(input())

    while num < x:
        num += 1
        st.append(num)
        result.append("+")
    if st[-1] == x:
        st.pop()
        result.append("-")
    else:
        answer = False

if answer == False:
    print("NO")
else:
    print("\n".join(result))
