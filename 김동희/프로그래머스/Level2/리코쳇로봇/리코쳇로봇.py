from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(board):
    answer = 0
    board_rowlength = len(board)
    board_collength = len(board[0])
    find = 0
    for r in range(board_rowlength):
        for c in range(board_collength):
            if board[r][c] == "R":
                answer = BFS(r, c, board, board_rowlength, board_collength)
                find = 1
                break
        if find:
            break

    return answer


def BFS(r, c, board, board_rowlength, board_collength):
    Q = deque()
    Q.append((r, c, 0))
    visited = [[[0,0,0,0] for b in range(board_collength)] for a in range(board_rowlength)]
    while Q:
        r, c, ans = Q.popleft()

        if board[r][c] == "G":
            return ans

        for d in range(4):
            sr = r
            sc = c
            while True:
                nr = sr + dr[d]
                nc = sc + dc[d]
                if nr < 0 or nr >= board_rowlength or nc < 0 or nc >= board_collength:
                    break
                if board[nr][nc] == "D":
                    break
                sr = nr
                sc = nc
            if not visited[sr][sc][d]:
                visited[sr][sc][d] = 1
                Q.append((sr, sc, ans + 1))
    return -1
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

