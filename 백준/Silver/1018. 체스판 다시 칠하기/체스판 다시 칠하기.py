N, M = map(int, input().split())
chess_board = []
result = []
for i in range(N):
    chess_board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0
        draw2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if chess_board[a][b] != 'B':
                        draw1 = draw1 + 1
                    if chess_board[a][b] != 'W':
                        draw2 = draw2 + 1
                else:
                    if chess_board[a][b] != 'W':
                        draw1 = draw1 + 1
                    if chess_board[a][b] != 'B':
                        draw2 = draw2 + 1
        result.append(min(draw1, draw2))

print(min(result))