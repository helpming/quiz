import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())

graph = [list(0 for _ in range(m)) for _ in range(n)]

for _ in range(k):
    i, j = map(int, input().split()) # i는 세로, j는 가로
    graph[i-1][j-1] = 1

def dfs(x, y):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if graph[y][x] == 1:
        graph[y][x] = 0
        cnt += 1

        dfs(x -1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


cnts = []

for i in range(n): # 세로
    for j in range(m): # 가로
        cnt = 0
        if dfs(j, i) == True:
            cnts.append(cnt)

print(max(cnts))