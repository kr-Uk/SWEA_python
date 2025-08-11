MSG_FORMAT = '#{} {}'
def dfs(cnt, k):
    global result
    
    if cnt == n-1:
        result[0] = max(result[0], k)
        result[1] = min(result[1], k)
        return 
    if op[0] > 0:
        op[0] -= 1
        dfs(cnt+1, k + nums[cnt+1])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(cnt+1, k - nums[cnt+1])
        op[1] += 1 
    if op[2] > 0:
        op[2] -= 1
        dfs(cnt+1, k * nums[cnt+1])
        op[2] += 1
    if op[3] > 0:  
        op[3] -= 1
        dfs(cnt+1, int(k / nums[cnt+1]))
        op[3] += 1

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    result = [-1e9, 1e9]
    dfs(0, nums[0]) # 백트래킹

    print(MSG_FORMAT.format(test_case, int(result[0]) - int(result[1])))