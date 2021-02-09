
def find(x):
    if x == s[x]:
        return x
    
    s[x] = find(s[x])
    return s[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x== y:
        return
    s[y] = x
    cnt[x] += cnt[y]
    

t = int(input())
for i in range(t):
    n = int(input())
    s = dict()
    cnt = dict()

    for r in range(n):
        a, b = input().split()
        if a not in s:
            s[a] = a
            cnt[a] = 1
        if b not in s:
            s[b] = b
            cnt[b] = 1
        union(a, b)
        print(cnt[s[a]])
        print(s)