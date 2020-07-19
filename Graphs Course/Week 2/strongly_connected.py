#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj1, used, x, count):
    #write your code here
    used[x] = 1
    count += 1
    # print(adj1)
    # print(adj1[x])
    # print(x)
    for i in adj1[x]:
        # print(i)
        if used[i] == 0:
            dfs(adj1,used,i,count)
    # order.insert(0,x)
    return count
def fill(adj1, v, used, order):
    used[v] = 1
    for i in adj1[v]:
        if used[i] == 0:
            fill(adj1,i,used,order)
    order.append(v)
def transpose(adj1):
    adj2 = [[] for _ in range(len(adj1))]
    for i in range(len(adj1)):
        for j in adj1[i]:
            adj2[j].append(i)

    return adj2
def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    used = [0] * len(adj)
    order = list()
    # write your code here
    for _ in range(len(adj)):
        if used[_] == 0:
            fill(adj,_,used,order)

    adj_2 = transpose(adj)
    used = [0] * len(adj)
    while order:
        i = order.pop()
        if used[i] == 0:
            result = dfs(adj_2, used, i, result)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
