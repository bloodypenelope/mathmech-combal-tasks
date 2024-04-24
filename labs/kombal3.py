# def dijkstra(V,s):
#     d=[]
#     used=[]
#     for v in V:
#         d[v] = float("inf")
#         used[v] = False
#     d[s]=0
#     for i in range(len(V)):
#         v = 0
#         for j in range(len(V)):
#             if not used[j] and (v == 0 or d[j]<d[i]):
#                 v = j
#         if d[v] == float("inf"):
#             break
#         used[v] = True
#         for
def get_graph(filename):
    INF = float("inf")
    with open(filename, 'r') as f:
        size = int(f.readline())
        graph = []
        for i in range(size):
            graph.append([0] * size)
        for i in range(size):
            string = f.readline()
            arr = string.split()
            for j in range(len(arr)-2):
                if (j % 2 == 0):
                    graph[int(arr[j])-1][i] = int(arr[j+1])
        for i in range(size):
            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    graph[i][j] = INF
        start = int(f.readline())
        end = int(f.readline())
    return [start, end, size, graph]


def dijkstra(graph, start, size):
    INF = float("inf")
    n = size
    w = graph
    dist = [INF] * n
    dist[start] = 0
    arr1 = [str(start+1)]
    arr2 = [""] * (n-1)
    path = arr1 + arr2
    used = [False] * n
    min_dist = 0
    min_vertex = start
    while min_dist < INF:
        i = min_vertex
        used[i] = True
        for j in range(n):
            if dist[i] + w[i][j] < dist[j]:
                dist[j] = dist[i] + w[i][j]
                path[j] = path[i] + " " + str(j+1)
        min_dist = INF
        for j in range(n):
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j
    return [dist, path]


def write_result(result, end):
    with open('out.txt', 'w') as f:
        dist = result[0]
        path = result[1]
        if path[end] != "":
            f.write("Y\n")
            f.write(path[end]+"\n")
            f.write(str(dist[end])+"\n")
            f.close()
        else:
            f.write("N")
            f.close()


if __name__ == '__main__':
    arr = get_graph('in.txt')
    start = arr[0]-1
    end = arr[1]-1
    size = arr[2]
    graph = arr[3]
    write_result(dijkstra(graph, start, size), end)
