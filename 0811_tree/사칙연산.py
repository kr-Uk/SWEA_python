MSG_FORMAT = '#{} {}'

def postOrder(node):
    
    if tree[node][0] != 0:
        left_child = postOrder(tree[node][0])
        right_child = postOrder(tree[node][1])
        if node_to_cal[node] == '-':
            return left_child - right_child
        elif node_to_cal[node] == '+':
            return left_child + right_child
        elif node_to_cal[node] == '*':
            return left_child * right_child
        elif node_to_cal[node] == '/':
            return int(left_child / right_child)
    
    return node_to_num[node]

for test_case in range(1, 11):
    n = int(input())
    tree = [[0, 0] for _ in range(n+1)]
    node_to_cal = dict()
    node_to_num = dict()
    
    for _ in range(n):
        temp = list(input().split())
        if len(temp) == 2:
            node_to_num[int(temp[0])] = int(temp[1])
        elif len(temp) == 4:
            node_to_cal[int(temp[0])] = temp[1]
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[0])][1] = int(temp[3])
    
    print(MSG_FORMAT.format(test_case, postOrder(1)))