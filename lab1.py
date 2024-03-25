"""Module providing a function to check if the given graph is bipartite"""


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
        adj_matrix = [[int(num) for num in line.split(' ')] for line in f]
        return n, adj_matrix


def is_bipartite(start: int, n: int, graph: list) -> tuple:
    """
    Checks if the given connected graph is bipartite or not using breadth-first search algorithm

    Args:
        start (int): Starting vertex for bfs algorithm
        n (int): Number of vertices in the graph
        graph (list): Adjacency matrix of the graph

    Returns:
        tuple: Tuple that contains boolean value, which indicates if the given graph is bipartite,
        and dictionary with colors of vertices
    """
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
    """
    Reads the graph from the in.txt file, checks if its bipartite,
    and then writes the result in the out.txt file
    """
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
