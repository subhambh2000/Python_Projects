#Uses python3

import sys

def dfs(adj1,v,temp,visited):
    visited[v] = True
    temp.append(v)

    for i in adj1[v]:
        if visited[i] is False:
            temp = dfs(adj1,i,temp,visited)
    return temp
def number_of_components(adj1):
    visited = [False] * len(adj1)
    queue = list()
    
    # queue.append(x1)
    # visited[x1] = True
    # while queue:
    #     pred = queue.pop(0)
    #     if pred == y1:
    #         return 1
    #     else:
    for v in range(len(adj1)):
        if visited[v] is False:
            temp = list()
            queue.append(dfs(adj1,v,temp,visited))
    return len(queue)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
    print(number_of_components(adj))
