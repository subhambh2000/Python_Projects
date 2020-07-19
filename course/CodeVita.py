n = int(input())
b = list(input())
g = list(input())
# b = list(b)
# g = list(g)
ctr = n
n1 = n
i = 0
result = 0
while i < n1:
    if b[i] != g[i] and ctr > 0:
        # print(g)
        g.append(g[i])
        g.pop(i)
        # print(g)
        ctr -= 1
        if ctr > 0:
            continue
        else:
            result = len(b)
            break
    else:
        # print("before",b)
        b.pop(i)
        # print("after", b)
        # print("before", g)
        g.pop(i)
        # print("after", g)
        n1 -= 1
        # print(n1)
        ctr = n1
print(result)
