MSG_FORMAT = '#{} {}'

def searchSize(x, y):
    cnt_x = x
    cnt_y = y
    while cnt_x < n and graph[y][cnt_x] != 0:
        cnt_x += 1
    while cnt_y < n and graph[cnt_y][x] != 0:
        cnt_y += 1
    return (cnt_y - y, cnt_x - x)

def sequenceSort(m):
    mapping = {r: c for r, c in m}
    all_rows = {r for r, _ in m}
    all_cols = {c for _, c in m}
    
    start = None
    for r in all_rows:
        if r not in all_cols:
            start = r
            break
    
    seq = [start]
    while start in mapping:
        start = mapping[start]
        seq.append(start)
    return seq

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    matrices = []
    
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 0 and not visited[y][x]:
                h, w = searchSize(x, y)
                matrices.append((h, w))
                for _y in range(y, y+h):
                    for _x in range(x, x+w):
                        visited[_y][_x] = True
    
    dims = sequenceSort(matrices)
    m_len = len(dims) - 1
    dp = [[0]*(m_len+1) for _ in range(m_len+1)]
    
    for diag in range(2, m_len+1):
        for i in range(1, m_len-diag+2):
            j = i + diag - 1
            dp[i][j] = 1e9
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],
                            dp[i][k] + dp[k+1][j] + dims[i-1]*dims[k]*dims[j])
    
    print(MSG_FORMAT.format(test_case, dp[1][m_len]))
