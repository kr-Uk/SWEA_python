MSG_FORMAT = '#{} {}'
t = int(input())

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (graph[y][x] + _map[ny][nx]) < graph[ny][nx]:
                    q.append((nx, ny))
                    graph[ny][nx] = graph[y][x] + _map[ny][nx]
                
    return graph[n-1][n-1]
        

for test_num in range(1, t+1):
    n = int(input())
    _map = [list(map(int, input())) for _ in range(n)]
    graph = [[1e9] * n for _ in range(n)]
    
    print(MSG_FORMAT.format(test_num, bfs(0, 0)))