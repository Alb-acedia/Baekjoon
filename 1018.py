n, m = map(int, input().split())
i_board = []
o_board = []
for x in range(n):
    i_board.append(input())

for i in range(n - 7):
    for j in range(m - 7):  # 8 * 8만큼 고정
        f_white = 0
        f_black = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if i_board[a][b] != "W":
                        f_white += 1
                    if i_board[a][b] != "B":
                        f_black += 1
                else:
                    if i_board[a][b] != "B":
                        f_white += 1
                    if i_board[a][b] != "W":
                        f_black += 1
        o_board.append(f_white)
        o_board.append(f_black)

print(min(o_board))
