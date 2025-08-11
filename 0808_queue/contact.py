from collections import deque

MSG_FORMAT = '#{} {}'

def bfs(node):
    visited = [False] * 101
    q = deque([node])
    visited[node] = True
    
    while q:
        l = len(q)
        for _ in range(l):
            curr = q.popleft()
            for g in graph[curr]:
                if not visited[g]:
                    q.append(g)
                    visited[g] = True
            
        if len(q) == 0:
            return prev_q
        
        prev_q = []
        for temp in q:
            prev_q.append(temp)
        
for test_case in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    ilst = list(map(int, input().split()))
    for i in range(0, n, 2):
        graph[ilst[i]].append(ilst[i+1])
    
    print(MSG_FORMAT.format(test_case, max(bfs(start))))