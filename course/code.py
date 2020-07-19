p = int(input())
q = int(input())
r = int(input())
s = int(input())
ctr = 0
for i in range(p,q+1):
    for j in range(r,s+1):
        n = j
        m = i
        while m >= n > 0:
            n = max(m,n) - min(m,n)
            m = max(m,n)
            ctr += 1