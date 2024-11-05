def read_graph(filename: str) -> tuple:
    with open(filename, mode='r', encoding='utf-8') as f:
        n = int(f.readline())
        adj_list = [[int(num) - 1 for num in line.split(' ')[:-1]]
                    for line in f]
        return n, adj_list


def find_component(node: int, graph: list, component: list, visited: set):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            find_component(neighbor, graph, component, visited)


def main():
    n, adj_list = read_graph('in.txt')
    visited = set()
    components = []
    output = ''

    for vertex in range(n):
        if vertex not in visited:
            components.append([])
            find_component(vertex, adj_list, components[-1], visited)

    output += str(len(components)) + '\n'
    for component in components:
        output += ' '.join(map(lambda x: str(x + 1), sorted(component))) + '\n'
    output = output[:-1]

    with open('out.txt', mode='w', encoding='utf-8') as f:
        f.write(output)


if __name__ == '__main__':
    main()
