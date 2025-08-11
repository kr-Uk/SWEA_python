MSG_FORMAT = '#{} {}'

def dfs(cnt, idx):
    global result
    
    if cnt == n//2: # 반으로 나뉘면
        a_score = 0
        b_score = 0
        a = list(temp)
        b = list(food - temp) # 이거 때문에 set으로 !
        
        for i in range(cnt-1):
            for j in range(i+1, cnt):
                a_score += score[a[i]][a[j]] + score[a[j]][a[i]]
                b_score += score[b[i]][b[j]] + score[b[j]][b[i]]
        
        result = min(result, abs(a_score-b_score))
        return
    
    for i in range(idx, n): # idx를 통해 중복x (1,2), (2,1) ...
        temp.add(i)
        dfs(cnt+1, i+1)
        temp.remove(i)


t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]

    food = {i for i in range(n)} # set으로 만들기
    temp = set() # 음식을 잠시 나눌 변수
    result = 1e9

    dfs(0, 0)

    print(MSG_FORMAT.format(test_case, result))