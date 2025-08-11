MSG_FORMAT = '#{} {}'

def inOrder(node):
    global result
    
    if node == 0:
        return
    
    inOrder(tree[node][0])
    result += num_to_alpha[node]
    inOrder(tree[node][1])
    

for test_case in range(1, 11):
    result = ''
    n = int(input())
    tree = [[0, 0] for _ in range(n+1)]
    num_to_alpha = dict()
    
    for _ in range(n):
        temp = list(input().split())
        num_to_alpha[int(temp[0])] = temp[1]
        if len(temp) >= 3:
            tree[int(temp[0])][0] = int(temp[2])
            if len(temp) >= 4:
                tree[int(temp[0])][1] = int(temp[3])
    
    inOrder(1)
        
    print(MSG_FORMAT.format(test_case, result))