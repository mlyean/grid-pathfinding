from grid import Grid
from dijkstra import dijkstra
from astar import a_star

def main():
    g = Grid(7, 7, obstacles = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])
    src = (0, 0)
    dest = (6, 6)

    print("Grid visualization: ")
    print(g)

    print("\nLegend:\n\tS = Start\n\tE = End\n\tX = Obstacle\n\t_ = Empty space")

    print("\nPath by Dijkstra's algorithm:")
    print(g.plot_path(dijkstra(g, src, dest)))

    print("\nPath by A* search algorithm:")
    print(g.plot_path(a_star(g, src, dest)))

if __name__ == "__main__":
    main()
