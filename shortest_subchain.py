def main() -> None:
    n = int(input())
    p = {}
    best = {}

    current = -1

    tokens = []
    while len(tokens) < n:
        tokens.extend(list(map(int, input().split())))

    finish = tokens[-1]

    for next_tokens in tokens:
        if current == -1:
            p[next_tokens] = [(0, next_tokens, None)]
            tmp = p[next_tokens][0]
            best[next_tokens] = tmp
        else:
            if next_tokens not in p:
                p[next_tokens] = []
            tmp = (best[current][0] + 1, next_tokens, best[current])
            p[next_tokens].append(tmp)
            if next_tokens not in best or tmp < best[next_tokens]:
                best[next_tokens] = tmp
        current = next_tokens

    c = best[finish]

    result = []
    while c:
        result.append(str(c[1]))
        c = c[2]
    (result.reverse())
    print(*result)


if __name__ == '__main__':
    main()
