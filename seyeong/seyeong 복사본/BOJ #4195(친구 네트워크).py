import collections
t = int(input())


def dfs(start):
    cnt = 1
    stack = [start]
    visited = collections.defaultdict(str)
    visited[start] = True
    while stack:
        node = stack.pop()
        for e in network[node]:
            if not visited[e]:
                visited[e] = True
                stack.append(e)
                cnt += 1
    return cnt

for _ in range(t):

    num_rel = int(input())
    network = collections.defaultdict(list)
    for _ in range(num_rel):
        a, b = input().split(" ")
        network[a].append(b)
        network[b].append(a)

        # print("n :" , network[a])
        print(dfs(a))


