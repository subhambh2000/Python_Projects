#Uses python3

import sys
import queue # noqa

def bipartite(adj): # noqa
    #write your code here
    visited = [-1] * len(adj)
    queue = list() # noqa
    queue.append(0)
    visited[0] = 1
    while queue:
        pred = queue.pop(0)
        # print(pred)
        for i in adj[pred]:
            if visited[i] == -1:
                visited[i] = 1 - visited[pred]
                queue.append(i)
            else:
                if visited[i] == visited[pred]:
                    return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read() # noqa
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
