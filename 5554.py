total = 0
for x in range(4):
    total += int(input())

min, sec = divmod(total, 60)

print(min)
print(sec)