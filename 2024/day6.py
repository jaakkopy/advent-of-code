def in_bounds(n, m, pos):
    (i,j) = pos
    return (i >= 0 and i < n) and (j >= 0 and j < m)


def traverse(map, p, dir):
    n = len(map)
    m = len(map[0])
    
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    seen = set()

    num_distinct = 0
    while in_bounds(n, m, p):
        if (p,dir) in seen:
            return "loop"
        seen.add((p,dir))
        if map[p[0]][p[1]] != '*':
            num_distinct += 1
            map[p[0]][p[1]] = '*'
        i = dirs.index(dir)
        for j in range(4):
            dir = dirs[(i + j) % 4] # try different directions starting from the current one
            p2 = (p[0] + dir[0], p[1] + dir[1])
            if not in_bounds(n,m,p2):
                p = p2
                break
            if map[p2[0]][p2[1]] != '#':
                p = p2
                break
    
    return (num_distinct, seen)


if __name__ == "__main__":
    from sys import stdin

    map = [list(line)[:-1] if line[-1] == '\n' else list(line) for line in stdin.readlines()]

    n = len(map)
    m = len(map[0])

    dirs = {
        '<': (0,-1),
        '>': (0,1),
        '^': (-1,0),
        'v': (1,0)
    }

    for i in range(n):
        for j in range(m):
            if map[i][j] in dirs.keys():
                start = (i,j)
                dir = dirs[map[i][j]]
                break
    
    (part1, seen) = traverse(map, start, dir)
    print(part1)

    unique_pos = set([x[0] for x in seen])
    # For part 2: The obstruction must be placed on the path
    # here simply every possible obstruction is tried (dumb but works)
    loops = 0
    for p in unique_pos:
        map[p[0]][p[1]] = '#'
        part2 = traverse(map, start, dir)
        if part2 == "loop":
            loops += 1
        map[p[0]][p[1]] = '.'
    
    print(loops)