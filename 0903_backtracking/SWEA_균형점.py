TMSG_FORMAT = '#{}'
RMSG_FORMAT = '{:.10f}'

def manpower(start, end, idx):
    epsilon = 1e-12

    while end - start > epsilon:
        x = (start + end) / 2

        mp1 = 0
        mp2 = 0
        
        for i in range(idx):
            d1 = abs(x - magnetic[i][0])
            mp1 += magnetic[i][1] / (d1*d1)
            
        for i in range(idx, n, 1):
            d2 = abs(x - magnetic[i][0])
            mp2 += magnetic[i][1] / (d2*d2)

        if mp1 > mp2:
            start = x
        else:
            end = x

    return x


t = int(input())

for test_case in range(1, t+1):
    result = []
    
    n = int(input())
    temp = list(map(int, input().split()))
    magnetic = []
    
    for i in range(n):
        magnetic.append((temp[i], temp[i+n]))
    
    magnetic.sort(key = lambda x:x[0])
    
    for i in range(n-1):
        result.append(manpower(magnetic[i][0], magnetic[i+1][0], i+1))
    
    print(TMSG_FORMAT.format(test_case), end = ' ')
    for r in result:
        print(RMSG_FORMAT.format(r), end = ' ')
    print()