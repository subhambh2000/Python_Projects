#Uses python3

import sys
import queue # noqa

def extract_min(adj,dist,q): # noqa
    min = sys.maxsize
    index = 0
    for i in range(len(adj)):
        # print('i',i,'dist',dist[i])
        if dist[i] < min and q[i] == 0:
            min = dist[i]
            index = i
    # print(index)
    return index
# def printPath(u,v,dist,pred):
#
#     if v == u:
#         print('(',u+1,dist[u],')',end='')
#     else:
#         printPath(u,pred[v],dist,pred)
#         print('->', '(', v + 1, dist[v], ')',end='')
#     return
def distance(adj, cost, s, t): # noqa
    #write your code here
    dist = [sys.maxsize]*len(adj)
    dist[s] = 0
    q = [0] * len(adj)
    pred = [-sys.maxsize]*len(adj)
    for i in range(len(adj)):
        u = extract_min(adj,dist,q)
        # print('u',u)
        q[u] = 1
        for _ in range(len(adj[u])):
            # print('_',_,adj[u][_])
            if q[adj[u][_]] == 0 and dist[adj[u][_]] > dist[u] + cost[u][_]:
                dist[adj[u][_]] = dist[u] + cost[u][_]
                pred.insert(adj[u][_],u)
    # printPath(s,t,dist,pred)
    # print(pred)
    if dist[t] == sys.maxsize:
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read() # noqa
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # print(edges)
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    # print(adj)
    # print(cost)
    print(distance(adj, cost, s, t))
