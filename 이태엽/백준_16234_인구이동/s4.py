import sys
sys.stdin = open('input.txt')

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def connected_values(matrix, L, R):

    def is_valid(i, j, ni, nj):
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            return False
        diff = abs(matrix[i][j] - matrix[ni][nj])
        return L <= diff <= R

    def traverse(i, j, visited, total, count):
        visited.add((i, j))
        total += matrix[i][j]
        count += 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (ni, nj) not in visited and is_valid(i, j, ni, nj):
                total, count = traverse(ni, nj, visited, total, count)

        return total, count

    connected_matrix = [[0] * N for _ in range(N)]
    visited = set()

    for i in range(N):
        for j in range(N):
            if (i, j) in visited and connected_matrix[i][j] == True:
                continue
            if (i, j) not in visited:
                visited.clear()
                total, count = traverse(i, j, visited, 0, 0)
                avg = total // count
                for ni, nj in visited:
                    connected_matrix[ni][nj] = avg

    for i in range(N):
        for j in range(N):
            if connected_matrix[i][j] == 0:
                connected_matrix[i][j] = matrix[i][j]

    return connected_matrix



def find_connected_elements(matrix, L, R):
    connected_lists = []
    visited = [[0] * N for _ in range(N)]

    def dfs(row, col, connected_list):
        visited[row][col] = True
        connected_list.append(matrix[row][col])

        if row > 0 and visited[row-1][col] == 0:
            neighbor_element = matrix[row-1][col]
            if L <= abs(matrix[row][col] - neighbor_element) <= R:
                dfs(row-1, col, connected_list)

        if row < N-1 and visited[row+1][col] == 0:
            neighbor_element = matrix[row+1][col]
            if L <= abs(matrix[row][col] - neighbor_element) <= R:
                dfs(row+1, col, connected_list)

        if col > 0 and visited[row][col-1] == 0:
            neighbor_element = matrix[row][col-1]
            if L <= abs(matrix[row][col] - neighbor_element) <= R:
                dfs(row, col-1, connected_list)

        if col < N-1 and visited[row][col+1] == 0:
            neighbor_element = matrix[row][col+1]
            if L <= abs(matrix[row][col] - neighbor_element) <= R:
                dfs(row, col+1, connected_list)

    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                connected_list = []
                dfs(row, col, connected_list)
                connected_lists.append(connected_list)

    return connected_lists


ans = 0
while True:
    if len(find_connected_elements(matrix, L, R)) == N*N:
        break
    else:
        matrix = connected_values(matrix, L, R)
        ans += 1
print(ans)