from collections import deque

MSG_FORMAT = '#{} {}'

def bfs(x, y):
    sec = 0
    
    q = deque([(x, y)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        # 소용돌이 생성 및 잠잠..
        for _x, _y in soyong:
                if graph[_y][_x] != 1:
                    if sec%3 == 2:
                        graph[_y][_x] = 0
                    else:
                        graph[_y][_x] = 2
        
        # q에 있는만큼 반복 -> sec표현
        l = len(q)
        for _ in range(l):
            x, y = q.popleft()
            
            # 목적지 도착 시
            if x == dest[1] and y == dest[0]:
                return sec
            
            # 좌우상하
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[ny][nx]:
                        # 그냥 이동
                        if graph[ny][nx] == 0:
                            q.append((nx, ny))
                            visited[ny][nx] = True
                        # 소용돌이 앞에서 멈춤
                        elif graph[ny][nx] == 2:
                            q.append((x, y))
        sec += 1
    return -1

t = int(input())

for test_case in range(1, t+1):
    
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    soyong = []
    
    for x in range(n):
        for y in range(n):
            if graph[y][x] == 2:
                soyong.append([x, y])
    
    print(MSG_FORMAT.format(test_case, bfs(start[1], start[0])))
