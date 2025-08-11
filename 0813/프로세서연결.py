MSG_FORMAT = '#{} {}'
t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(idx, connected, length):
    global core, line

    # 연결된 것과 남은 것을 합쳐도 총 코어 개수를 못넘기면 아예 따지지 않음
    if connected + (total_core - idx) < core:
        return

    # 모든 경우의 수를 탐색하면 (idx == total_core) 
    if idx == total_core:
        if connected > core or (connected == core and length < line):
            core = connected
            line = length
        return

    x, y = cores[idx]

    for i in range(4):
        path = []
        nx, ny = x + dx[i], y + dy[i]
        # 상하좌우 한방향으로 쭉~
        while 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = 3
            path.append((nx, ny))
            nx += dx[i]
            ny += dy[i]

        # 끝까지 갔다는 거니까 추가하기
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            dfs(idx + 1, connected + 1, length + len(path))
        
        # 복구하기 (끝까지 안가도 복구 가능)  
        for px, py in path:
            graph[py][px] = 0
    
    # 연결 안하고 넘기기
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
                # 가장자리에 있는 코어는 이미 연결
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    continue
                cores.append((j, i))

    total_core = len(cores)
    dfs(0, 0, 0) # (idx, connected, length)

    print(MSG_FORMAT.format(test_case, line))