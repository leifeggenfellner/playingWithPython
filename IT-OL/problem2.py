N = int(input())


def BFS(G, r):
    Q = []
    Q.append(r)

    while len(Q) != 0:
        v = Q.pop()
        if v == G:
            return v
