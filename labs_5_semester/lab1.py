import heapq


def l1_norm(p1: tuple[int], p2: tuple[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def prim(n, points):
    if n == 0:
        return [], 0

    edges = []
    mst_edges = []
    visited = set()
    total_weight = 0

    visited.add(0)
    for i in range(n):
        heapq.heappush(edges, (l1_norm(points[0], points[i]), 0, i))

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v in visited:
            continue
        visited.add(v)

        total_weight += weight
        mst_edges.append((u, v))

        for next_vertex in range(n):
            if next_vertex not in visited:
                heapq.heappush(edges, (l1_norm(points[v], points[next_vertex]),
                                       v, next_vertex))

    adjacency_list = [[] for _ in range(n)]
    for u, v in mst_edges:
        adjacency_list[u].append(v + 1)
        adjacency_list[v].append(u + 1)

    return adjacency_list, total_weight


def main():
    with open("in.txt", mode="r", encoding="utf-8") as file:
        n = int(file.readline())
        points = [tuple(map(int, file.readline().split())) for _ in range(n)]

    adjacency_list, total_weight = prim(n, points)
    output = ""

    for i in range(n):
        adjacency_list[i].sort()
        output += ' '.join(map(str, adjacency_list[i])) + ' 0\n'
    output += str(total_weight)

    with open("out.txt", mode="w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
