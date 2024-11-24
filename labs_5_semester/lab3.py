from collections import deque
import functools


def read_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        graph = []
        n = int(file.readline())

        line = [0] + list(map(int, file.readline().split())) + [0]
        graph.append(line)

        for _ in range(n):
            line = [0] + list(map(int, file.readline().split()))
            graph.append(line)

        line = [0] * (n + 2)
        graph.append(line)

        s = 0
        t = n + 1

    return graph, s, t


def bfs(graph, s, t):
    queue = deque([[s, [s]]])
    visited = set()
    visited.add(s)

    while queue:
        vertex, path = queue.popleft()

        if vertex == t:
            return path

        for neighbor, capacity in enumerate(graph[vertex]):
            if capacity > 0 and neighbor not in visited:
                queue.append([neighbor, path + [neighbor]])
                visited.add(neighbor)

    return []


def ford_fulkerson(graph, s, t):
    path = bfs(graph, s, t)

    while path:
        capacities = [graph[i][j] for i, j in zip(path, path[1:])]
        min_capacity = min(capacities)

        for i, j in zip(path, path[1:]):
            graph[i][j] -= min_capacity
            graph[j][i] += min_capacity

        path = bfs(graph, s, t)

    max_flow = functools.reduce(lambda x, y: x + y, graph[t], 0)
    return max_flow


def write_file(filename, max_flow):
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(str(max_flow))


def main():
    graph, s, t = read_file("in.txt")
    max_flow = ford_fulkerson(graph, s, t)
    write_file("out.txt", max_flow)


if __name__ == "__main__":
    main()
