#Uses python3
import sys
from math import pow,sqrt
def dist(x1,y1,x2,y2):
    s = pow(x1-x2,2)+pow(y1-y2,2)
    return sqrt(s)
def min_key(dst,mstSet):
    index = 0
    min = sys.maxsize
    for v in range(n):
        if dst[v] < min and mstSet[v] == 0:
            min = dst[v]
            index = v
    return index
def minimum_distance(x, y):
    result = 0.
    mstSet = [0]*n
    dst = [float(sys.maxsize)]*n
    dst[0] = 0.
    i = n
    while i >= 0:
        u = min_key(dst,mstSet)
        mstSet[u] = 1
        for v in range(n):
            if mstSet[v] == 0 and dst[v] > dist(x[u],y[u],x[v],y[v]):
                dst[v] = dist(x[u],y[u],x[v],y[v])
        i -= 1
    result = sum(dst[i] for i in range(n))
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # print(data)
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    # print('x:',x,'y:',y)
    print("{0:.9f}".format(minimum_distance(x, y)))
