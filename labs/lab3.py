import heapq


def read_file(filename: str) -> tuple:
    with open(filename, mode='r', encoding='utf-8') as file:
        n = int(file.readline())
        graph = {}
        for vertex in range(1, n + 1):
            line = iter(file.readline().split()[:-1])
            graph[vertex] = [(int(neighbor), int(next(line)))
                             for neighbor in line]
        source = int(file.readline())
        target = int(file.readline())
    return graph, source, target


def write_file(filename: str, result: str, path: list, distance: int) -> None:
    with open(filename, mode='w', encoding='utf-8') as file:
        if result == 'N':
            file.write(result)
        else:
            path = " ".join(map(str, path))
            file.write(f'{result}\n{path}\n{distance}')


def minmax(graph: dict, source: int, target: int) -> tuple:
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {}
    visited = set()

    queue = [(0, source)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        if current_vertex == target:
            path = []
            while current_vertex in predecessors:
                path.append(current_vertex)
                current_vertex = predecessors[current_vertex]
            path.append(source)
            path.reverse()
            return 'Y', path, distances[target]

        for neighbor, weight in graph[current_vertex]:
            new_distance = max(current_distance, weight)

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(queue, (new_distance, neighbor))

    return 'N', [], None


def main():
    graph, source, target = read_file('in.txt')
    result, path, distance = minmax(graph, source, target)
    write_file('out.txt', result, path, distance)


if __name__ == '__main__':
    main()
