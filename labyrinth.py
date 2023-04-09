from collections import deque


def read_input(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        m = int(f.readline())
        labyrinth = [list(map(int, f.readline().split())) for _ in range(n)]
        start = tuple(map(int, f.readline().split()))
        end = tuple(map(int, f.readline().split()))

    return n, m, labyrinth, start, end


def find_path(labyrinth, start, end):
    # определяем размер лабиринта
    n, m = len(labyrinth), len(labyrinth[0])
    
    # создаем матрицу для хранения расстояний от начала до каждой ячейки лабиринта
    dist = [[-1] * m for _ in range(n)]
    
    # устанавливаем расстояние до начала равным 0
    dist[start[0]][start[1]] = 0
    
    # создаем очередь для поиска в ширину
    queue = deque()
    queue.append(start)
    
    # производим поиск в ширину
    while queue:
        x, y = queue.popleft()
        
        # если достигли конца, возвращаем найденный путь
        if (x, y) == end:
            path = [(x, y)]
            while path[-1] != start:
                x, y = path[-1]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + dx < n and 0 <= y + dy < m and dist[x + dx][y + dy] == dist[x][y] - 1:
                        path.append((x + dx, y + dy))
                        break
            path.reverse()
            return path
        
        # иначе продолжаем поиск
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < m and labyrinth[x + dx][y + dy] == 0 and dist[x + dx][y + dy] == -1:
                dist[x + dx][y + dy] = dist[x][y] + 1
                queue.append((x + dx, y + dy))
    
    # если путь не найден, возвращаем None
    return None


def output(path, filename):
    steps = []
    with open(filename, "w") as f:
        if path is None:
            f.write("N")
        else:
            f.write("Y\n")
            for x, y in path:
                steps.append(f"{x + 1} {y + 1}")
        f.write("\n".join(steps))


def main():
    input_file_name = "in.txt"
    output_file_name = "out.txt"
    # считываем входные данные
    n, m, labyrinth, start, end = read_input(input_file_name)

    # находим путь
    path = find_path(labyrinth, tuple(map(lambda x: x - 1, start)), tuple(map(lambda x: x - 1, end)))

    # выводим результат
    output(path, output_file_name)


if __name__ == "__main__":
    main()
