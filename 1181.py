n = int(input())
letter_list = []
for _ in range(n):
    letter_list.append(input())
set_list = set(letter_list)
letter_list = list(set_list)
letter_list.sort()
letter_list.sort(key=len)
for i in range(len(letter_list)):
    print(letter_list[i])
