msg_FORMAT = '#{} {}'
n = int(input())

def dfs(n):
    global result
    if n == cnt:
        result = max(result, int("".join(money)))
        return
    for i in range(len(money)-1):
        for j in range(i+1, len(money)):
            money[i], money[j] = money[j], money[i]
            chk = int("".join(money))
            if (n, chk) not in visited:
                dfs(n+1)
                visited.append((n, chk))
            money[j], money[i] = money[i], money[j]

for c in range(1, n+1):
    money, cnt = input().split()
    cnt = int(cnt)
    money = list(money)
    visited = []
    result = 0
    dfs(0)
    print(msg_FORMAT.format(c, result))