"""Module providing a function for finding components of the graph"""


def read_graph(filename: str) -> tuple:
    """
    Read the graph from the file, 
    which contains a number of vertices of the graph and its adjacency list

    Args:
        filename (str): Name of the file, which contains information about the graph

    Returns:
        tuple: Tuple of number of vertices and adjacency list of the graph
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        n = int(f.readline())
        adj_list = [[int(num) - 1 for num in line.split(' ')[:-1]]
                    for line in f]
        return n, adj_list


def find_component(start: int, graph: list, component: list, visited: set):
    """
    Finds the graph component that owns the starting vertex using depth-first search algorithm

    Args:
        start (int): Starting vertex for dfs algorithm
        graph (list): Adjacency list of the graph
        component (list): Desired component of the graph (initially empty)
        visited (set): List of visited vertices
    """
    visited.add(start)
    component.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            find_component(neighbor, graph, component, visited)


def main():
    """
    Reads the graph from the in.txt file, finds all its components,
    and then writes them to the out.txt file with their total number
    """
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
