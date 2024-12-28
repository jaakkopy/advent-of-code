DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

def in_bounds(pos, n, m):
    return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m


def neigbors(garden, u):
    s = []
    for d in DIRS:
        w = (u[0] + d[0], u[1] + d[1])
        if in_bounds(w, len(garden), len(garden[0])) and garden[u[0]][u[1]] == garden[w[0]][w[1]]:
            s.append(w)
    return s


def dfs(garden, v, visited):
    S = [v]
    comp = set()
    type_of_v = garden[v[0]][v[1]]
    
    while len(S) > 0:
        u = S.pop()
        type_of_u = garden[u[0]][u[1]]
        if u not in visited and type_of_v == type_of_u:
            visited.add(u)
            comp.add(u)
            for w in neigbors(garden, u):
                S.append(w)
    return (comp, visited)


def connected_components(garden):
    visited = set()
    components = []

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i,j) not in visited:
                (comp, visited) = dfs(garden, (i,j), visited)
                components.append(comp)

    return components


if __name__ == "__main__":
    from sys import stdin

    garden = [[x for x in l.strip()] for l in stdin.readlines()]
    comps = connected_components(garden)
    part1 = 0

    for c in comps:
        area = len(c)
        perimeter = 0
        sides = []
        for p in c:
            n = neigbors(garden, p)
            perimeter += (4 - len(n))

        part1 += area * perimeter
    
    print(part1)