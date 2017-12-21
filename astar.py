from math import inf, sqrt

def hypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def heuristic_cost_estimate(src, dest):
    return hypot(dest[0] - src[0], dest[1] - src[1])

def a_star(grid):
    nodes = grid.get_nodes()
    closed_set = []
    open_set = [grid.src]

    prev = {node : None for node in nodes}

    g_score = {node : inf for node in nodes}
    g_score[grid.src] = 0

    f_score = {node : inf for node in nodes}
    f_score[grid.src] = heuristic_cost_estimate(grid.src, grid.dest)

    while open_set:
        u = min(open_set, key = f_score.__getitem__)
        if u == grid.dest:
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
                f_score[v] = g_score[v] + heuristic_cost_estimate(v, grid.dest)
                prev[v] = u

    path = [grid.dest]
    cur = grid.dest

    while prev[cur]:
        path.append(prev[cur])
        cur = prev[cur]

    return list(reversed(path))
