def hash(chars: str) -> int:
    s = 0
    for c in chars:
        s = (17 * (s + ord(c))) % 256
    return s


def create_map(guides: list[list[str]]) -> dict[int, list[list]]:
    syms: dict[int, list[list]] = {}
    for g in guides:
        key = hash(g[0])
        if g[1].isdigit():
            arr = syms.get(key, [])
            e = next((x for x in arr if x[0] == g[0]), None)
            if not e:
                arr.append([g[0], int(g[1])])
            else:
                e[1] = int(g[1])
            syms[key] = arr
        else:
            arr = syms.get(key, [])
            arr = list(filter(lambda x: x[0] != g[0], arr))
            syms[key] = arr
    return syms


if __name__ == "__main__":
    from sys import stdin
    guides = stdin.readline().rstrip().split(",")
    print(sum(map(hash, guides)))  # part 1
    guides = [g.split("=") if '=' in g else g.split("-") for g in guides]
    s = 0
    for key, value in create_map(guides).items():
        for i in range(len(value)):
            s += (key + 1) * (i + 1) * value[i][1]
    print(s)  # part 2
