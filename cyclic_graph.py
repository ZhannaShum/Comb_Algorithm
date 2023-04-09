def read_input_file(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        adj_list = [[] for _ in range(n+1)]
        for i in range(1, n+1):
            adj_list[i] = list(map(int, f.readline().split()))[:-1]
    return n, adj_list


def write_output_file(file_name, result):
    with open(file_name, 'w') as f:
        if result[0] == 'A':
            f.write('A')
        else:
            f.write('N\n')
            f.write(' '.join(map(str, result[1])))


def dfs(vertex, visited, parent, adj_list, cycle):
    visited[vertex] = True
    for neighbour in adj_list[vertex]:
        if not visited[neighbour]:
            parent[neighbour] = vertex
            if dfs(neighbour, visited, parent, adj_list, cycle):
                return True
        elif parent[vertex] != neighbour:
            # Найден цикл
            cycle.append(neighbour)
            while vertex != neighbour:
                cycle.append(vertex)
                vertex = parent[vertex]
            cycle.append(neighbour)
            return True
    return False


def find_cycle(n, adj_list):
    visited = [False]*(n+1)
    parent = [0]*(n+1)
    cycle = []

    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, visited, parent, adj_list, cycle):
                cycle.reverse()
                return 'N', cycle[:-1]

    return 'A', []


def main():
    input_file_name = "in.txt"
    output_file_name = "out.txt"
    n, adj_list = read_input_file(input_file_name)
    result = find_cycle(n, adj_list)
    write_output_file(output_file_name, result)


if __name__ == '__main__':
    main()
