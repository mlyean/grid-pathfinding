from math import inf, sqrt

def hypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def heuristic_cost_estimate(src, dest):
    return hypot(dest[0] - src[0], dest[1] - src[1])

def a_star(grid, src, dest):
    nodes = grid.get_nodes()
    closed_set = []
    open_set = [src]

    prev = {node : None for node in nodes}

    g_score = {node : inf for node in nodes}
    g_score[src] = 0

    f_score = {node : inf for node in nodes}
    f_score[src] = heuristic_cost_estimate(src, dest)

    while open_set:
        u = min(open_set, key = f_score.__getitem__)
        if u == dest:
            break

        open_set.remove(u)
        closed_set.append(u)

        for v in grid.get_adjacent(u):
            if v in closed_set:
                continue

            if v not in open_set:
                open_set.append(v)

            alt_g = g_score[u] + 1
            if alt_g < g_score[v]:
                g_score[v] = alt_g
                f_score[v] = g_score[v] + heuristic_cost_estimate(v, dest)
                prev[v] = u

    path = [dest]
    cur = dest

    while prev[cur]:
        path.append(prev[cur])
        cur = prev[cur]

    return list(reversed(path))
