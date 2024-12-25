def in_bounds(pos, n, m):
    return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m


def bfs(pos, target, map, condition, part2):
    count = 0
    visited = set(pos)
    Q = [pos] 
    n = len(map)
    m = len(map[0])

    while len(Q) > 0:
        p = Q.pop()
        if map[p[0]][p[1]] == target:
            count += 1
            continue
        ok = 0
        for d in [(0,1), (0,-1), (-1,0), (1,0)]:
            p2 = (p[0] + d[0], p[1] + d[1])
            if not part2 and p2 in visited:
                continue
            if in_bounds(p2, n, m) and condition(p, p2, map):
                ok += 1
                Q.append(p2)
                visited.add(p2)

    return count


if __name__ == "__main__":
    from sys import stdin

    lines = [[int(x) for x in l.strip()] for l in stdin.readlines()]

    part1 = 0
    part2 = 0
    cond = lambda p1, p2, map:  map[p2[0]][p2[1]] == map[p1[0]][p1[1]] + 1

    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 0:
                part1 += bfs((i,j), 9, lines, cond, False)
                part2 += bfs((i,j), 9, lines, cond, True)

    print(part1)
    print(part2)