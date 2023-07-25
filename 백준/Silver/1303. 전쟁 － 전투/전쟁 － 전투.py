from collections import deque

n, m = map(int, input().split())

graph = [list(input()) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    cnt = 0
    que = deque()
    que.append((x, y))
    visited[y][x] = True

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == color and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((nx, ny))
                    cnt += 1
    return cnt + 1

w, b = 0, 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            w += bfs(j, i, 'W') ** 2
        if graph[i][j] == 'B' and not visited[i][j]:
            b += bfs(j, i, 'B') ** 2

print(w, b) 