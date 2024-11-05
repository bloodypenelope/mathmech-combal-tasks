def read_graph(filename: str) -> tuple:
    with open(filename, mode='r', encoding='utf-8') as f:
        n = int(f.readline())
        adj_matrix = [[int(num) for num in line.split(' ')] for line in f]
        return n, adj_matrix


def is_bipartite(start: int, n: int, graph: list) -> tuple:
    colors = {}
    queue = [start]
    colors[start] = 0

    while queue:
        node = queue.pop(0)

        for neighbor in range(n):
            if graph[node][neighbor] == 0:
                continue

            if neighbor not in colors:
                colors[neighbor] = 1 - colors[node]
                queue.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False, colors
    return True, colors


def main():
    n, adj_matrix = read_graph('in.txt')
    result, colors = is_bipartite(0, n, adj_matrix)
    output = str()

    if not result:
        output = 'N'
    else:
        part1 = [str(v + 1) for v in range(n) if colors[v] == 0]
        part2 = [str(v + 1) for v in range(n) if colors[v] == 1]
        output = 'Y\n' + ' '.join(part1) + '\n' + ' '.join(part2)

    with open('out.txt', mode='w', encoding='utf-8') as f:
        f.write(output)


if __name__ == '__main__':
    main()
