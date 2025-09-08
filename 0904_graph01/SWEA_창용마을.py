"""
n명인데 1~n까지 번호
"""

from collections import deque
MSG_FORMAT = '#{} {}'

def bfs(start):
    global visited
    q = deque([start])
    
    while q:
        curr = q.popleft()
        if not visited[curr]:
            visited[curr] = 1
            q.extend(graph[curr])
    

t = int(input())

for test_case in range(1, t+1):
    result = 0
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            result += 1

    print(MSG_FORMAT.format(test_case, result))