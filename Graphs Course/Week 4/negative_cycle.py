#Uses python3

import sys

def negative_cycle(adj, cost): # noqa
    #write your code here
    dist = [sys.maxsize] * len(adj)
    dist[0] = 0
    pred = [-sys.maxsize] * len(adj)
    for j in range(len(adj)-1):
        for i in range(len(adj)):
            # u = extract_min(adj, dist, q)
            # print('u',u)
            c = 0
            for _ in (adj[i]):
                if dist[_] > dist[i] + cost[i][c]:
                    dist[_] = dist[i] + cost[i][c]
                    # pred.insert(_, i)
                    # v = _
                else:
                    c += 1
    for u in range(len(adj)):
        s = 0
        for v in adj[u]:
            if dist[v] > dist[u]+cost[u][s]:
                return 1
            else:
                s += 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read() # noqa
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
