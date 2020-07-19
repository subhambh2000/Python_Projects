#Uses python3

import sys


def acyclic(adj1):
    count = 0
    # visited = [False] * len(adj1)
    queue = list()
    indegree = [0]*len(adj1)
    for v in range(len(adj1)):
        for e in adj1[v]:
            indegree[e] += 1
    for v1 in range(len(indegree)):
        if indegree[v1] == 0:
            queue.append(v1)
    while queue:
        pred = queue.pop(0)
        for i in adj1[pred]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
        count += 1
    if count != len(adj1):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    # print(adj)
    print(acyclic(adj))
