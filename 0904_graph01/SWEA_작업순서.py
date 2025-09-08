from collections import deque

t = 10

for test_case in range(1, t+1):
    v, e = map(int, input().split())
    degree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    temp = list(map(int, input().split()))
    
    for i in range(0, 2*e, 2):
        graph[temp[i]].append(temp[i+1])
        degree[temp[i+1]] += 1
    
    print('#{} '.format(test_case), end = "")

    q = deque([])
    visited = [0] * (v+1)
    
    while True:
        for i in range(1, v+1):
            if degree[i] == 0 and not visited[i]:
                visited[i] = 1
                q.append(i)
        
        if not q:
            break
        
        for _ in range(len(q)):
            curr = q.popleft()
            print(curr, end=' ')
            for c in graph[curr]:
                degree[c] -= 1

    print()
        