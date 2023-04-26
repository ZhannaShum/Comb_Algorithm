import heapq


def create_graph(n, edges_list):
    graph = {}
    for i in range(n):
        edges = list(map(int, edges_list[i].split()))[:-1]
        graph[i + 1] = [(edges[j], edges[j + 1]) for j in
                        range(0, len(edges), 2)]
    return graph


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    paths = {start: []}
    heap = [(0, start)]
    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(heap, (distance, neighbor))
    if distances[end] != float('inf'):
        return ('Y', paths[end], distances[end])
    else:
        return ('N', [], 0)


def main():
    with open('int.txt', 'r') as f:
        n = int(f.readline())
        edges_list = [f.readline() for i in range(n)]
        start = int(f.readline())
        end = int(f.readline())

    graph = create_graph(n, edges_list)
    result = dijkstra(graph, start, end)

    with open('out.txt', 'w') as f:
        f.write(result[0] + '\n')
        if result[0] == 'Y':
            f.write(' '.join(map(str, [start] + result[1])) + '\n')
            f.write(str(result[2]))


if __name__ == '__main__':
    main()
