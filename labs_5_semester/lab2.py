from collections import deque
import functools
import copy


def read_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        n = int(file.readline())
        graph = []

        for _ in range(n):
            line = list(map(int, file.readline().split()))
            graph.append(line)

        s = int(file.readline())
        t = int(file.readline())

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


def write_file(filename, graph, remaining_graph, max_flow):
    n = len(graph)
    flow_graph = [[0 for _ in range(n)] for _ in range(n)]
    output = ""

    for i in range(n):
        for j in range(n):
            flow = graph[i][j] - remaining_graph[i][j]
            if flow > 0:
                flow_graph[i][j] = flow
        output += " ".join(map(str, flow_graph[i])) + '\n'
    output += str(max_flow)

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(output)


def main():
    graph, s, t = read_file("in.txt")
    remaining_graph = copy.deepcopy(graph)
    max_flow = ford_fulkerson(remaining_graph, s - 1, t - 1)
    write_file("out.txt", graph, remaining_graph, max_flow)


if __name__ == "__main__":
    main()
