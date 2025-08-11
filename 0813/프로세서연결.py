MSG_FORMAT = '#{} {}'
t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(idx, connected, length):
    global core, line

    if connected + (total_core - idx) < core:
        return

    if idx == total_core:
        if connected > core or (connected == core and length < line):
            core = connected
            line = length
        return

    x, y = cores[idx]

    for i in range(4):
        path = []
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = 3
            path.append((nx, ny))
            nx += dx[i]
            ny += dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            dfs(idx + 1, connected + 1, length + len(path))
        
        for px, py in path:
            graph[py][px] = 0

    dfs(idx + 1, connected, length)


for test_case in range(1, t + 1):
    line = 0
    core = 0
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    cores = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    continue
                cores.append((j, i))

    total_core = len(cores)
    dfs(0, 0, 0)

    print(MSG_FORMAT.format(test_case, line))