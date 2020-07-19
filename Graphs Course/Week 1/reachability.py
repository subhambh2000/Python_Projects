#Uses python3

import sys

def reach(adj1, x1, y1):
    visited = [False]*len(adj1)
    queue = list()
    queue.append(x1)
    visited[x1] = True
    while queue:
        pred = queue.pop(0)
        if pred == y1:
            return 1
        else:
            for i in adj1[pred]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
    return 0


if __name__ == '__main__':
    input = sys.stdin.read() # noqa
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    # print(data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # print(edges)
    # print(data)
    x, y = data[2 * m:]
    # print(x,y)
    adj = [[] for _ in range(n)]
    # print(adj)
    x, y = x - 1, y - 1
    # print(x,y)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
    print(reach(adj, x, y))
