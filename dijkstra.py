from math import inf

def dijkstra(grid):
    Q = grid.get_nodes()
    dist = {node : inf for node in Q}
    prev = {node : None for node in Q}

    dist[grid.src] = 0

    while Q:
        u = min(Q, key = dist.__getitem__)
        Q.remove(u)

        for v in grid.get_adjacent(u):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    path = [grid.dest]
    cur = grid.dest

    while prev[cur]:
        path.append(prev[cur])
        cur = prev[cur]

    return list(reversed(path))
