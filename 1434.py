from collections import deque


S = [[] for _ in range(1001)]


class Node:
    def __init__(self):
        self.v = False
        self.s = []
        self.p = None


nodes = [Node() for _ in range(100001)]

N, M = map(int, input().split())

for i in range(1, N + 1):
    stops = list(map(int, input().split()))
    k = stops[0]
    for x in stops[1:]:
        nodes[x].s.append(i)
        S[i].append(x)

a, b = map(int, input().split())

Q = deque([a])
nodes[a].v = True

while Q:
    j = Q.popleft()
    for s in nodes[j].s:
        for x in S[s]:
            if not nodes[x].v:
                Q.append(x)
                nodes[x].p = j
                nodes[x].v = True

        S[s].clear()

if not nodes[b].v:
    print(-1)
else:
    out = []
    p = b
    while p:
        out.append(p)
        p = nodes[p].p

    print(len(out) - 1)
    for i in reversed(out):
        print(i, end=" ")
