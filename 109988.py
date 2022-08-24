letter = list(input())
cnt = 0
for i in range(len(letter)):
    if letter[i] == letter[len(letter) - 1 - i]:
        cnt += 1

if cnt == len(letter):
    print(1)
else:
    print(0)
