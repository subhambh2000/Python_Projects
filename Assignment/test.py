def comp(p):
    m = len(p)
    r1 = ['']*(m+1)
    r1[1:] = p
    # print(r)
    s = [0]*(m+1)
    s[0] = -1

    k = 0
    for q in range(2,m+1):
        # print('q',q)
        # print('k',k)
        # print('pi',s)
        while k > 0 and r1[k+1] != r1[q]:
            k = s[k]
        if r1[k+1] == r1[q]:
            k = k + 1
        s[q] = k
    return s
def kmp(t,p):
    n = len(t)
    r = [''] * (n + 1)
    r[1:] = t
    m = len(p)
    v = [''] * (m + 1)
    v[1:] = p
    s = comp(p)
    # print(s)
    # print('v',v)
    # print('r',r)
    q = 0
    for i in range(1,n+1):
        # print('i',i)
        # print('before q',q)
        while q > 0 and v[q+1] != r[i]:
            q = s[q]
        if v[q+1] == r[i]:
            q = q + 1
        # print('after q',q)
        if q == m:
            print("Pattern occurs with shift:",i-m)
            q = s[q]
if __name__ == '__main__':
    pat = input("Pattern: ")
    print(comp(pat)[1:])
    text = input("Text: ")
    kmp(text,pat)
