MSG_FORMAT = '#{} {} {}'

def makeTable(node, depth, parent):
    depth_and_parent[node][0] = depth
    depth_and_parent[node][1] = parent
    if tree[node][0] != 0:
        makeTable(tree[node][0], depth+1, node)
    if tree[node][1] != 0:
        makeTable(tree[node][1], depth+1, node)

def LCA(a, b): 
    cnt = 0 
    while depth_and_parent[a][0] > depth_and_parent[b][0]:
        a = depth_and_parent[a][1]
    while depth_and_parent[a][0] < depth_and_parent[b][0]:
        b = depth_and_parent[b][1]
    
    while depth_and_parent[a][1] != depth_and_parent[b][1]:
        a = depth_and_parent[a][1]
        b = depth_and_parent[b][1]
    
    return depth_and_parent[a][1]

def nodeSize(node):
    global size
    if tree[node][0] != 0:
        nodeSize(tree[node][0])
    if tree[node][1] != 0:
        nodeSize(tree[node][1])
    size += 1

t = int(input())

for test_case in range(1, t+1):
    v, e, node1, node2 = map(int, input().split())
    tree = [[0, 0] for _ in range(v+1)]
    temp = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        if tree[temp[i]][0] == 0:
            tree[temp[i]][0] = temp[i+1]
        else:
            tree[temp[i]][1] = temp[i+1]
    
    depth_and_parent = [[0, 0] for _ in range(v+1)]
    makeTable(1, 0, 0)
    common_ancestor_node = LCA(node1, node2)
    size = 0
    nodeSize(common_ancestor_node)
    
    print(MSG_FORMAT.format(test_case, common_ancestor_node, size))